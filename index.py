#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Myanmar TTS Video Bot with HTML Subtitle Editor & Subscription System
- Users must buy subscription (10d / 15d / 1m / 3m / 5m / 1y)
- Admin can edit prices, set KPay/Wave numbers, manage users
- Web HTML integration for custom subtitle editing & preview
"""

import os
import logging
import asyncio
import time
import subprocess
import re
import json
import sys
import warnings
import sqlite3
import html
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from asyncio import Semaphore

warnings.filterwarnings("ignore")

for logger_name in ['urllib3', 'requests', 'telebot', 'edge_tts', 'asyncio', 'httpx', 'httpcore', 'telegram', 'moviepy', 'yt_dlp', 'whisper']:
    logging.getLogger(logger_name).setLevel(logging.CRITICAL)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

from telegram import Update, InputFile, InlineKeyboardButton, InlineKeyboardMarkup, MessageEntity, WebAppInfo
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler, ApplicationHandlerStop
from telegram.constants import ParseMode

from moviepy.editor import VideoFileClip, AudioFileClip
from pydub import AudioSegment
import yt_dlp
import whisper
from deep_translator import GoogleTranslator
import edge_tts

# =========================================================
# CONFIG - CHANGE THESE
# =========================================================
BOT_TOKEN = "8840689115:AAGv4QXodzIJ4UO17sWY-x_pKNtB3hdAviM"   # <-- your bot token
WEBAPP_URL = "https://yourdomain.com/index.html"                 # <-- Web App HTML URL (Hosting address)

# Admin Telegram user IDs (add your own ID here)
ADMIN_IDS = [7308292609]

DEFAULT_KPAY = "09xxxxxxxxx"
DEFAULT_WAVE = "09xxxxxxxxx"

DEFAULT_PLANS = {
    "10d":  {"name": "၁၀ ရက်",   "days": 10,  "price": 3000},
    "15d":  {"name": "၁၅ ရက်",   "days": 15,  "price": 4000},
    "1m":   {"name": "၁ လ",      "days": 30,  "price": 7000},
    "3m":   {"name": "၃ လ",      "days": 90,  "price": 18000},
    "5m":   {"name": "၅ လ",      "days": 150, "price": 28000},
    "1y":   {"name": "၁ နှစ်",    "days": 365, "price": 50000},
}

PREMIUM_EMOJI_IDS = {
    "✅": "6087158252703850104",
    "⏳": "6224324157924975216",
    "⌛": "6224324157924975216",
    "❌": "6086616567133509891",
    "📦": "6185914385655930182",
    "🎬": "5375464961822695044",
    "📝": "6102503603916774694",
    "🛒": "6221954521388556644",
    "⚙️": "6102446132959387332",
    "💰": "6102775243418378788",
    "✨": "6224324157924975216",
    "🚀": "6221964464237846356",
}

EMOJI_SLOTS = {
    "1":  {"key": "success",    "name": "✅ ပြီးဆုံး / Success", "default": "✅"},
    "2":  {"key": "processing", "name": "⏳ စောင့်ဆိုင်း",         "default": "⏳"},
    "3":  {"key": "error",      "name": "❌ အမှား",               "default": "❌"},
    "4":  {"key": "package",    "name": "📦 Package",             "default": "📦"},
    "5":  {"key": "video",      "name": "🎬 Video",               "default": "🎬"},
    "6":  {"key": "text",       "name": "📝 စာသား",              "default": "📝"},
    "7":  {"key": "buy",        "name": "🛒 ဝယ်ယူ",               "default": "🛒"},
    "8":  {"key": "settings",   "name": "⚙️ ဆက်တင်",             "default": "⚙️"},
}
pending_emoji_for_admin = {}

def premium_emoji_html(emoji_id, fallback="✨") -> str:
    if emoji_id:
        return f'<tg-emoji emoji-id="{html.escape(str(emoji_id), quote=True)}">{fallback}</tg-emoji>'
    return fallback

def premiumize_text(text: str) -> str:
    if not text or "<tg-emoji" in text:
        return text
    result = text
    for emoji_char in sorted(PREMIUM_EMOJI_IDS.keys(), key=len, reverse=True):
        eid = PREMIUM_EMOJI_IDS[emoji_char]
        tag = premium_emoji_html(eid, emoji_char)
        result = result.replace(emoji_char, tag)
    return result

# =========================================================
# GLOBALS & DATABASE
# =========================================================
executor = ThreadPoolExecutor(max_workers=10)
TEMP_FOLDER = "temp_files"
os.makedirs(TEMP_FOLDER, exist_ok=True)

whisper_model = None
whisper_lock = asyncio.Lock()
DB_FILE = "cook_data.db"

VOICES = {
    "thiha": {"id": "my-MM-ThihaNeural", "name": "Thiha", "gender": "ကျား", "emoji": "👨"},
    "nilar": {"id": "my-MM-NilarNeural", "name": "Nilar", "gender": "မ", "emoji": "👩"}
}
DEFAULT_VOICE = "thiha"
DEFAULT_SPEED = 1.4

def get_db_connection():
    return sqlite3.connect(DB_FILE, timeout=60, check_same_thread=False)

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, username TEXT, first_name TEXT, voice TEXT DEFAULT 'thiha', speed REAL DEFAULT 1.4, mode TEXT DEFAULT 'auto', is_banned INTEGER DEFAULT 0, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS plans (plan_id TEXT PRIMARY KEY, name TEXT NOT NULL, days INTEGER NOT NULL, price INTEGER NOT NULL, is_active INTEGER DEFAULT 1)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS subscriptions (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER NOT NULL, plan_id TEXT, start_date TIMESTAMP, end_date TIMESTAMP, is_active INTEGER DEFAULT 1, activated_by TEXT DEFAULT 'admin', note TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS settings (key TEXT PRIMARY KEY, value TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS payments (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, plan_id TEXT, amount INTEGER, method TEXT, status TEXT DEFAULT 'pending', screenshot_file_id TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS sessions (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, video_path TEXT, audio_path TEXT, srt_path TEXT, transcript_text TEXT, translated_text TEXT, edited_text TEXT, video_duration REAL, is_voice BOOLEAN DEFAULT 0, mode TEXT DEFAULT 'auto', created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

def ensure_user(user_id, username=None, first_name=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT user_id FROM users WHERE user_id = ?', (user_id,))
    if not cursor.fetchone():
        cursor.execute('INSERT INTO users (user_id, username, first_name) VALUES (?, ?, ?)', (user_id, username, first_name))
    conn.commit()
    conn.close()

def get_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT voice, speed, mode, is_banned, username, first_name FROM users WHERE user_id = ?', (user_id,))
    r = cursor.fetchone()
    conn.close()
    if r:
        return {'voice': r[0], 'speed': r[1], 'mode': r[2] or 'auto', 'is_banned': bool(r[3]), 'username': r[4], 'first_name': r[5]}
    return None

def is_admin(user_id):
    return user_id in ADMIN_IDS

def get_active_subscription(user_id):
    if is_admin(user_id):
        return True
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM subscriptions WHERE user_id = ? AND is_active = 1 AND end_date > datetime('now')", (user_id,))
    r = cursor.fetchone()
    conn.close()
    return r is not None

def get_setting(key, default=""):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT value FROM settings WHERE key = ?', (key,))
    r = cursor.fetchone()
    conn.close()
    return r[0] if r else default

def set_setting(key, value):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT OR REPLACE INTO settings (key, value) VALUES (?, ?)', (key, value))
    conn.commit()
    conn.close()

def get_session(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT video_path, audio_path, srt_path, edited_text, video_duration FROM sessions WHERE user_id = ? ORDER BY created_at DESC LIMIT 1', (user_id,))
    r = cursor.fetchone()
    conn.close()
    if r:
        return {'video_path': r[0], 'audio_path': r[1], 'srt_path': r[2], 'edited_text': r[3], 'video_duration': r[4]}
    return None

# =========================================================
# HANDLERS & WEB APP INTEGRATION
# =========================================================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    ensure_user(user.id, user.username, user.first_name)
    
    keyboard = [
        [InlineKeyboardButton("🎬 ဗီဒီယို စာတန်းထိုးပြင်ရန် (HTML Web App)", web_app=WebAppInfo(url=WEBAPP_URL))],
        [InlineKeyboardButton("🛒 Package ဝယ်ရန်", callback_data="show_buy")],
        [InlineKeyboardButton("⚙️ ဆက်တင်များ", callback_data="show_settings")]
    ]
    
    text = (
        f"👋 မင်္ဂလာပါ Bro <b>{html.escape(user.first_name or 'User')}</b>!\n\n"
        f"🎬 <b>YouTube / TikTok / Video</b> များကို မြန်မာလို အသံသွင်းခြင်းနှင့် **HTML Web App** ဖြင့် စာတန်းထိုးများိတ်ကြိုက် တည်းဖြတ်နိုင်ပါပြီ။\n\n"
        f"အောက်ပါခလုတ်ကိုနှိပ်၍ စာတန်းထိုးများကို စိတ်ကြိုက်ပြင်ဆင်နိုင်ပါသည်။"
    )
    await update.message.reply_text(premiumize_text(text), reply_markup=InlineKeyboardMarkup(keyboard), parse_mode=ParseMode.HTML)

# =========================================================
# MAIN ENTRY
# =========================================================
def main():
    init_db()
    application = Application.builder().token(BOT_TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    
    logger.info("Bot is running with HTML WebApp integration...")
    application.run_polling()

if __name__ == "__main__":
    main()
