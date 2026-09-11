<!DOCTYPE html>
<html lang="my">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Myanmar TTS Video Bot Dashboard</title>
<!-- Tailwind CSS CDN -->
<script src="[https://cdn.tailwindcss.com](https://cdn.tailwindcss.com)"></script>
<!-- FontAwesome CDN -->
<link rel="stylesheet" href="[https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css](https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css)">
<!-- Google Fonts (Pyidaungsu / Noto Sans Myanmar) -->
<link href="[https://fonts.googleapis.com/css2?family=Pyidaungsu:wght@400;700&display=swap](https://fonts.googleapis.com/css2?family=Pyidaungsu:wght@400;700&display=swap)" rel="stylesheet">
<style>
body {
font-family: 'Pyidaungsu', sans-serif;
background-color: #0f172a;
color: #f8fafc;
}
.glass-card {
background: rgba(30, 41, 59, 0.7);
backdrop-filter: blur(12px);
border: 1px solid rgba(255, 255, 255, 0.1);
}
</style>
</head>
<body class="min-h-screen flex flex-col">
<!-- Top Navigation -->
<header class="glass-card sticky top-0 z-50 border-b border-slate-800">
<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
<div class="flex items-center space-x-3">
<div class="bg-indigo-600 p-2 rounded-xl text-white shadow-lg shadow-indigo-500/30">
<i class="fa-solid fa-video text-xl"></i>
</div>
<div>
<h1 class="font-bold text-lg tracking-wide text-white">MM TTS Video Bot</h1>
<p class="text-xs text-slate-400">Subscription & Management Dashboard</p>
</div>
</div>
<div class="flex items-center space-x-4">
<span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-medium bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
<span class="w-2 h-2 mr-2 bg-emerald-400 rounded-full animate-pulse"></span> Bot Active
</span>
</div>
</div>
</header>
<!-- Main Container -->
<main class="flex-grow max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
<!-- Stats Overview Grid -->
<section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
<!-- Total Users -->
<div class="glass-card rounded-2xl p-5 shadow-xl transition-all hover:scale-[1.02]">
<div class="flex items-center justify-between">
<div>
<p class="text-xs font-medium text-slate-400 uppercase tracking-wider">Total Users</p>
<h3 class="text-2xl font-bold mt-1 text-white">1,248</h3>
</div>
<div class="p-3 bg-blue-500/10 text-blue-400 rounded-xl border border-blue-500/20">
<i class="fa-solid fa-users text-xl"></i>
</div>
</div>
<div class="mt-4 flex items-center text-xs text-emerald-400">
<i class="fa-solid fa-arrow-trend-up mr-1"></i> +12% from last week
</div>
</div>
<!-- Active Subscriptions -->
<div class="glass-card rounded-2xl p-5 shadow-xl transition-all hover:scale-[1.02]">
<div class="flex items-center justify-between">
<div>
<p class="text-xs font-medium text-slate-400 uppercase tracking-wider">Active Subscriptions</p>
<h3 class="text-2xl font-bold mt-1 text-emerald-400">342</h3>
</div>
<div class="p-3 bg-emerald-500/10 text-emerald-400 rounded-xl border border-emerald-500/20">
<i class="fa-solid fa-crown text-xl"></i>
</div>
</div>
<div class="mt-4 flex items-center text-xs text-slate-400">
<i class="fa-solid fa-circle-check mr-1 text-emerald-400"></i> Fully operational
</div>
</div>
<!-- Pending Payments -->
<div class="glass-card rounded-2xl p-5 shadow-xl transition-all hover:scale-[1.02]">
<div class="flex items-center justify-between">
<div>
<p class="text-xs font-medium text-slate-400 uppercase tracking-wider">Pending Payments</p>
<h3 class="text-2xl font-bold mt-1 text-amber-400">7</h3>
</div>
<div class="p-3 bg-amber-500/10 text-amber-400 rounded-xl border border-amber-500/20">
<i class="fa-solid fa-clock text-xl"></i>
</div>
</div>
<div class="mt-4 flex items-center text-xs text-amber-400">
<i class="fa-solid fa-triangle-exclamation mr-1"></i> Requires approval
</div>
</div>
<!-- System Revenue -->
<div class="glass-card rounded-2xl p-5 shadow-xl transition-all hover:scale-[1.02]">
<div class="flex items-center justify-between">
<div>
<p class="text-xs font-medium text-slate-400 uppercase tracking-wider">Total Revenue</p>
<h3 class="text-2xl font-bold mt-1 text-indigo-400">2,450,000 Ks</h3>
</div>
<div class="p-3 bg-indigo-500/10 text-indigo-400 rounded-xl border border-indigo-500/20">
<i class="fa-solid fa-wallet text-xl"></i>
</div>
</div>
<div class="mt-4 flex items-center text-xs text-indigo-400">
<i class="fa-solid fa-arrow-trend-up mr-1"></i> KPay & Wave Money
</div>
</div>
</section>
<!-- Configuration & Plans Management -->
<section class="grid grid-cols-1 lg:grid-cols-3 gap-8">
<!-- Payment Gateway Settings -->
<div class="glass-card rounded-2xl p-6 shadow-xl space-y-6">
<div class="flex items-center justify-between border-b border-slate-800 pb-4">
<h2 class="text-lg font-bold text-white flex items-center">
<i class="fa-solid fa-gear text-indigo-400 mr-2"></i> Payment Settings
</h2>
</div>
<form class="space-y-4">
<div>
<label class="block text-xs font-medium text-slate-400 mb-1">KPay Phone Number</label>
<div class="relative">
<span class="absolute inset-y-0 left-0 pl-3 flex items-center text-slate-500">
<i class="fa-solid fa-mobile-screen"></i>
</span>
<input type="text" value="09977889966" class="w-full bg-slate-900 border border-slate-700 rounded-xl pl-10 pr-4 py-2.5 text-sm text-white focus:outline-none focus:border-indigo-500">
</div>
</div>
<div>
<label class="block text-xs font-medium text-slate-400 mb-1">Wave Money Phone Number</label>
<div class="relative">
<span class="absolute inset-y-0 left-0 pl-3 flex items-center text-slate-500">
<i class="fa-solid fa-wallet"></i>
</span>
<input type="text" value="09443322111" class="w-full bg-slate-900 border border-slate-700 rounded-xl pl-10 pr-4 py-2.5 text-sm text-white focus:outline-none focus:border-indigo-500">
</div>
</div>
<button type="button" class="w-full bg-indigo-600 hover:bg-indigo-700 text-white font-medium py-2.5 rounded-xl transition-all shadow-lg shadow-indigo-600/30 text-sm">
<i class="fa-solid fa-floppy-disk mr-2"></i> Save Settings
</button>
</form>
</div>
<!-- Subscription Plans Pricing -->
<div class="glass-card rounded-2xl p-6 shadow-xl space-y-6 lg:col-span-2">
<div class="flex items-center justify-between border-b border-slate-800 pb-4">
<h2 class="text-lg font-bold text-white flex items-center">
<i class="fa-solid fa-box-archive text-emerald-400 mr-2"></i> Subscription Plans & Pricing
</h2>
<span class="text-xs text-slate-400">Editable Tiers</span>
</div>
<div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
<!-- 10d Plan -->
<div class="bg-slate-900/60 border border-slate-800 rounded-xl p-4 flex flex-col justify-between">
<div>
<span class="text-xs text-indigo-400 font-semibold">10 Days</span>
<h4 class="text-base font-bold text-white mt-1">၁၀ ရက်</h4>
<p class="text-xl font-extrabold text-emerald-400 mt-2">3,000 ကျပ်</p>
</div>
<button class="mt-4 bg-slate-800 hover:bg-slate-700 text-xs text-slate-300 py-1.5 px-3 rounded-lg border border-slate-700 transition-all">
Edit Price
</button>
</div>
<!-- 15d Plan -->
<div class="bg-slate-900/60 border border-slate-800 rounded-xl p-4 flex flex-col justify-between">
<div>
<span class="text-xs text-indigo-400 font-semibold">15 Days</span>
<h4 class="text-base font-bold text-white mt-1">၁၅ ရက်</h4>
<p class="text-xl font-extrabold text-emerald-400 mt-2">4,000 ကျပ်</p>
</div>
<button class="mt-4 bg-slate-800 hover:bg-slate-700 text-xs text-slate-300 py-1.5 px-3 rounded-lg border border-slate-700 transition-all">
Edit Price
</button>
</div>
<!-- 1m Plan -->
<div class="bg-slate-900/60 border border-slate-800 rounded-xl p-4 flex flex-col justify-between">
<div>
<span class="text-xs text-indigo-400 font-semibold">1 Month</span>
<h4 class="text-base font-bold text-white mt-1">၁ လ</h4>
<p class="text-xl font-extrabold text-emerald-400 mt-2">7,000 ကျပ်</p>
</div>
<button class="mt-4 bg-slate-800 hover:bg-slate-700 text-xs text-slate-300 py-1.5 px-3 rounded-lg border border-slate-700 transition-all">
Edit Price
</button>
</div>
<!-- 3m Plan -->
<div class="bg-slate-900/60 border border-slate-800 rounded-xl p-4 flex flex-col justify-between">
<div>
<span class="text-xs text-indigo-400 font-semibold">3 Months</span>
<h4 class="text-base font-bold text-white mt-1">၃ လ</h4>
<p class="text-xl font-extrabold text-emerald-400 mt-2">18,000 ကျပ်</p>
</div>
<button class="mt-4 bg-slate-800 hover:bg-slate-700 text-xs text-slate-300 py-1.5 px-3 rounded-lg border border-slate-700 transition-all">
Edit Price
</button>
</div>
<!-- 5m Plan -->
<div class="bg-slate-900/60 border border-slate-800 rounded-xl p-4 flex flex-col justify-between">
<div>
<span class="text-xs text-indigo-400 font-semibold">5 Months</span>
<h4 class="text-base font-bold text-white mt-1">၅ လ</h4>
<p class="text-xl font-extrabold text-emerald-400 mt-2">28,000 ကျပ်</p>
</div>
<button class="mt-4 bg-slate-800 hover:bg-slate-700 text-xs text-slate-300 py-1.5 px-3 rounded-lg border border-slate-700 transition-all">
Edit Price
</button>
</div>
<!-- 1y Plan -->
<div class="bg-slate-900/60 border border-slate-800 rounded-xl p-4 flex flex-col justify-between">
<div>
<span class="text-xs text-indigo-400 font-semibold">1 Year</span>
<h4 class="text-base font-bold text-white mt-1">၁ နှစ်</h4>
<p class="text-xl font-extrabold text-emerald-400 mt-2">50,000 ကျပ်</p>
</div>
<button class="mt-4 bg-slate-800 hover:bg-slate-700 text-xs text-slate-300 py-1.5 px-3 rounded-lg border border-slate-700 transition-all">
Edit Price
</button>
</div>
</div>
</div>
</section>
<!-- Recent Pending Payments Table -->
<section class="glass-card rounded-2xl p-6 shadow-xl space-y-6">
<div class="flex items-center justify-between border-b border-slate-800 pb-4">
<h2 class="text-lg font-bold text-white flex items-center">
<i class="fa-solid fa-list-check text-amber-400 mr-2"></i> Pending Payment Approvals
</h2>
<span class="text-xs px-2.5 py-1 rounded-full bg-amber-500/10 text-amber-400 border border-amber-500/20 font-medium">7 Pending</span>
</div>
<div class="overflow-x-auto">
<table class="w-full text-left text-sm">
<thead class="bg-slate-900/60 text-slate-400 uppercase text-xs tracking-wider border-b border-slate-800">
<tr>
<th class="py-3 px-4">Payment ID</th>
<th class="py-3 px-4">User ID / Name</th>
<th class="py-3 px-4">Package</th>
<th class="py-3 px-4">Amount</th>
<th class="py-3 px-4">Method</th>
<th class="py-3 px-4 text-center">Actions</th>
</tr>
</thead>
<tbody class="divide-y divide-slate-800 text-slate-300">
<tr class="hover:bg-slate-800/40 transition-colors">
<td class="py-3 px-4 font-mono text-indigo-400">#1042</td>
<td class="py-3 px-4"><code>7308292609</code>
<span class="text-xs text-slate-500">Kaung Sai Thu Aung</span></td>
<td class="py-3 px-4 font-semibold text-white">၁ လ (1m)</td>
<td class="py-3 px-4 text-emerald-400 font-bold">7,000 ကျပ်</td>
<td class="py-3 px-4"><span class="px-2 py-1 bg-blue-500/10 text-blue-400 rounded-md text-xs border border-blue-500/20">KPay</span></td>
<td class="py-3 px-4 text-center space-x-2">
<button class="px-3 py-1 bg-emerald-600 hover:bg-emerald-700 text-white rounded-lg text-xs font-medium shadow-md shadow-emerald-600/20 transition-all">
<i class="fa-solid fa-check mr-1"></i> Approve
</button>
<button class="px-3 py-1 bg-rose-600 hover:bg-rose-700 text-white rounded-lg text-xs font-medium shadow-md shadow-rose-600/20 transition-all">
<i class="fa-solid fa-xmark mr-1"></i> Reject
</button>
</td>
</tr>
<tr class="hover:bg-slate-800/40 transition-colors">
<td class="py-3 px-4 font-mono text-indigo-400">#1043</td>
<td class="py-3 px-4"><code>5892147302</code>
<span class="text-xs text-slate-500">Alex Tun</span></td>
<td class="py-3 px-4 font-semibold text-white">၃ လ (3m)</td>
<td class="py-3 px-4 text-emerald-400 font-bold">18,000 ကျပ်</td>
<td class="py-3 px-4"><span class="px-2 py-1 bg-amber-500/10 text-amber-400 rounded-md text-xs border border-amber-500/20">Wave Money</span></td>
<td class="py-3 px-4 text-center space-x-2">
<button class="px-3 py-1 bg-emerald-600 hover:bg-emerald-700 text-white rounded-lg text-xs font-medium shadow-md shadow-emerald-600/20 transition-all">
<i class="fa-solid fa-check mr-1"></i> Approve
</button>
<button class="px-3 py-1 bg-rose-600 hover:bg-rose-700 text-white rounded-lg text-xs font-medium shadow-md shadow-rose-600/20 transition-all">
<i class="fa-solid fa-xmark mr-1"></i> Reject
</button>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</main>
<!-- Footer -->
<footer class="glass-card mt-12 py-4 border-t border-slate-800 text-center text-xs text-slate-500">
Myanmar TTS Video Bot • Secure HTML Dashboard © 2026
</footer>
</body>
</html>
