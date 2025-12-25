# Surah Walker

**Surah Walker** is a minimalist, browser-based experience for engaging with the Qur’an **word by word**, at a calm and human pace.

It randomly selects a surah and lets you advance through its words by tapping or clicking — encouraging presence, reflection, and slow reading rather than scrolling or completionism.

---

## ✨ Features

- 📖 **Word-by-word Qur’anic reading**
- 🔀 **Random surah selection** on each session
- 🌐 Optional **English meaning**
- 🔊 Optional **transliteration**
- 🗣️ Optional **Arabic text-to-speech** (browser-based)
- ⏸️ **Verse pauses** that briefly display the full ayah
- 🎨 Atmospheric pixel-art background
- 📱 Works on **desktop and mobile browsers**
- ⚡ No build step, no framework, no backend

---

## 🧠 How It Works

- Pure **HTML, CSS, and JavaScript**
- Qur’anic data is fetched live from the **Quran.com API**
- Words are flattened and displayed one at a time
- Speech synthesis uses the browser’s native TTS (if available)
- All logic runs client-side

No accounts, no storage, no tracking.

---

## 🚀 Getting Started

### Option 1 — Run locally
1. Clone or download this repository
2. Open `index.html` in your browser  
   *(Some browsers may restrict API calls when opened directly — see Option 2 if that happens)*

### Option 2 — GitHub Pages (recommended)
1. Push the repo to GitHub
2. Enable **GitHub Pages** (Settings → Pages → deploy from main branch)
3. Visit the provided URL

---

## 📁 Project Structure

/
├─ index.html # Main app (everything lives here)
├─ assets/ # Backgrounds and images
│ └─ bg/
└─ README.md
---

## 🛠️ Notes & Limitations

- Arabic audio quality depends on the voices installed on the user’s device
- Requires an active internet connection (Quran.com API)
- Designed as a **demo / contemplative tool**, not a full Qur’an reader

---

## 🌱 Philosophy

Surah Walker is intentionally simple.

It’s not about speed, progress, or productivity —  
but about **walking slowly through meaning**, one word at a time.

---

## 📜 License

This project is open-source and provided as-is.  
Feel free to fork, adapt, or remix it for personal or educational use.

