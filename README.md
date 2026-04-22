<div align="center">

# ∫ Advanced Mathematics Assistant

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://advanced-mathematics-assistant-zvlizldwugwffind.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-RAG-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)](https://langchain.com)
[![Groq](https://img.shields.io/badge/Groq-LLaMA%203.3-F55036?style=for-the-badge)](https://groq.com)
[![NCERT](https://img.shields.io/badge/NCERT-Class%209--10-4CAF50?style=for-the-badge)](https://ncert.nic.in)
[![JEE](https://img.shields.io/badge/JEE-Advanced%20Level-FF9800?style=for-the-badge)](https://jeeadv.ac.in)

**505 NCERT exercise questions. 4 ways to get help. Zero typing required.**  
**Class 9 & 10 · Step-by-step · 24/7 · Free**

[**🚀 Try Live Demo**](https://advanced-mathematics-assistant-zvlizldwugwffind.streamlit.app/) · [Report Bug](https://github.com/sarika-stack23/AdvMAthAI/issues) · [Request Feature](https://github.com/sarika-stack23/AdvMAthAI/issues)

</div>

---

## 📸 Screenshots

| Dark Mode | Light Mode |
|---|---|
| ![Dark](screenshots/dark_mode.png) | ![Light](screenshots/light_mode.png) |

---

## 🎯 What This App Does

Most students studying alone get stuck on a question and have no one to ask.

**Vedantu / Byjus / Teachoo** → show the answer. Done. No explanation.

**This app** → you choose exactly how much help you need:

```
Q5. In △ABC, DE∥BC. Find EC.

[💡 Hint]    [📖 Steps]
[✅ Answer]  [❓ Ask AI]
```

| Button | What it does |
|---|---|
| 💡 Hint | One nudge. Just the first step. Nothing more. |
| 📖 Steps | The method only — no final answer. |
| ✅ Answer | Full step-by-step solution. |
| ❓ Ask AI | Pick exactly where you're stuck — no typing needed. |

When you tap ❓ Ask AI:

```
Where are you stuck?

[🔢 No idea where to start]
[➡️ Stuck in the middle]
[❌ My answer is different]
[🤔 Don't understand the concept]
[📐 Show a similar easier example]
```

No typing. One tap. AI gives exactly what you need.

After every response:

```
💬 Did that help?

[✅ Yes, got it!]    [🔁 Explain differently]
[❓ I have a doubt]  [✅ Full Answer]
```

If you didn't get it — AI explains using a completely different approach.  
Real-life analogy. Simpler method. Different example.

---

## ✨ What's New in v3.2

### 🧩 NCERT Quiz Mode

Pick any NCERT exercise question and get help your way.

```
Sidebar:
① Pick class (Class 9 or 10)
② Pick chapter (Ch1 · Real Numbers...)
③ Pick exercise (ex1.1, ex1.2...)
→ Questions appear with 4 help buttons
```

**Class 9** — All 12 chapters, 223 questions across 41 exercises  
**Class 10** — All 14 chapters, 282 questions across 46 exercises  
**Total** — 505 questions, all from official NCERT textbook

### 🎯 Smart Help System

- **No typing required** — all help options are buttons
- **Active question tracking** — always know which question you're on
- **Replace not stack** — clicking a new button replaces the previous answer, chat stays clean
- **Follow-up built in** — "Did that help?" appears after every response

### 🏠 New Welcome Screen

New students see 3 clear cards explaining exactly how to use the app:
- 📚 Practice NCERT → Use sidebar
- 💬 Ask Anything → Type below
- 📷 Scan Problem → Use sidebar

---

## ✨ What's New in Phase 3 (v3.0)

### ✍️ Whiteboard-Style Answers

Every answer looks like a teacher writing on a board — not an AI typing an essay.

**Before (v2):**
```
The Commutative Property of Addition states that when we add numbers,
the order does not matter. This means that 3+4 gives the same result...
```

**After (v3):**
```
Step 1 — Does order matter in addition?
   3 + 4 = 7
   4 + 3 = 7  ← same answer!
   ✓ Commutative Property.

✅ Answer: 3+4 = 4+3 = 7
Key thing: this works for any two numbers!
```

One rule drives every answer: **if a student can't follow in 5 seconds — it's wrong.**

---

## 🔧 Core Features

| Feature | Description |
|---|---|
| 📚 NCERT Quiz Mode | 505 questions, Class 9 & 10, pick your help level |
| 🧮 Step-by-step solutions | Whiteboard style, one idea per line |
| 💡 4 help modes | Hint / Steps / Answer / Ask AI |
| 🤔 Stuck menu | 5 options for where you're stuck — no typing |
| 🔁 Follow-up | AI adapts if you didn't understand |
| 📈 Interactive graphs | Zoom, pan, hover — powered by Plotly |
| ⚡ Symbolic compute | Exact derivatives, integrals, equation solving |
| 📷 Camera scan | Photo any handwritten problem — auto solved |
| 📄 PDF upload | Upload textbook pages and ask questions |
| 🌗 Dark/light mode | Toggle anytime |
| 🔥 Daily streak | Track your practice days |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| LLM | LLaMA 3.3 70B via Groq API |
| RAG Pipeline | LangChain + ChromaDB |
| Embeddings | HuggingFace sentence-transformers |
| Symbolic Math | SymPy |
| Graphs | Plotly |
| OCR | Tesseract + pytesseract |
| Memory | MongoDB Atlas |
| UI | Streamlit |
| Language | Python 3.11 |

---

## 🚀 Getting Started

### Prerequisites

```bash
python3.11 --version  # Need 3.11+
pip install -r requirements.txt
```

### Setup

```bash
# 1. Clone the repo
git clone https://github.com/sarika-stack23/AdvMAthAI.git
cd AdvMAthAI

# 2. Create .env file
echo "GROQ_API_KEY=your_key_here" > .env

# 3. Build knowledge base
python3.11 main.py --rebuild

# 4. Run
python3.11 -m streamlit run main.py
```

Get your free Groq API key at [console.groq.com](https://console.groq.com)

### Commands

```bash
python3.11 -m streamlit run main.py   # Launch UI
python3.11 main.py --setup            # Build knowledge base
python3.11 main.py --rebuild          # Force rebuild knowledge base
python3.11 main.py --test             # Run unit tests
python3.11 main.py --eval             # Evaluate RAG pipeline
```

---

## 🐛 Troubleshooting

| Problem | Fix |
|---|---|
| No answer shown | Check Groq API key in `.env` or Streamlit Cloud Secrets |
| Class 10 shows no exercises | Make sure you're using the latest `knowledge_base.py` (v3.2) |
| Daily token limit | App auto-switches model — just keep using it |
| ChromaDB error | Delete `chroma_db/` folder and run `--rebuild` |
| Slow first load | Normal — embedding model downloads once, then instant |
| knowledge_base import error | Make sure `knowledge_base.py` is in same folder as `main.py` |
| Plotly graph not showing | Run `pip install plotly` and add `plotly>=5.0.0` to `requirements.txt` |
| OCR / camera scan not working | Run `pip install pytesseract` then `brew install tesseract` (Mac) |
| App crashes on startup | Run with `python3.11 -m streamlit run main.py` |

---

## 📝 Changelog

### v3.2 — April 2026
- ✅ **NCERT Quiz Mode** — 505 questions, Class 9 & 10, all exercises
- ✅ **4 help modes** — Hint / Steps / Answer / Ask AI
- ✅ **Stuck menu** — 5 options, no typing required
- ✅ **Follow-up system** — "Did that help?" after every response
- ✅ **Replace not stack** — new button replaces previous answer
- ✅ **Active question card** — always visible, never lose track
- ✅ **Welcome screen** — 3-card guide for new students
- ✅ **Smart cache** — quiz map rebuilds only when knowledge base changes
- ✅ **HTML fix** — no more `</div>` leaking into chat

### v3.0 (Phase 3) — April 2026
- ✅ **Whiteboard-style answers** — short lines, one idea per line
- ✅ **5-second rule** — if student can't follow in 5 seconds, AI writes shorter
- ✅ **Share answer button** — one-click to copy full solution
- ✅ **Plotly interactive graphs** — zoom/pan/hover/download
- ✅ **Streak counter** — daily problems solved + 🔥 streak
- ✅ **Mobile tweaks** — bigger touch targets, responsive layout

### v2.0.0 — April 2026
- ✅ **Complete NCERT coverage** — 104 chapters from Class 6 to Class 12
- ✅ **JEE Advanced** — 8 topic groups, competition-level math
- ✅ **118 RAG documents** — 20x more knowledge than v1
- ✅ **3,500+ ChromaDB chunks** — improved retrieval accuracy
- ✅ **Metadata-rich documents** — tagged with class, chapter, topic, difficulty

### v1.2.0 — March 2026
- ✅ PDF upload — ask questions about any document
- ✅ Camera scan — photo any handwritten problem
- ✅ Dark/light mode toggle
- ✅ Edit any question mid-conversation

### v1.0.0 — Initial Release
- 🎉 Full RAG pipeline with ChromaDB / FAISS
- 🎉 Streamlit UI with dark/light theme
- 🎉 Symbolic math via SymPy
- 🎉 Graph plotter
- 🎉 MongoDB chat memory

---

## 🗺️ Roadmap

```
Now         v3.2 — NCERT Quiz Mode (505 questions) ✅
Next        v4.0 — Firebase Auth (student login + profiles)
Then        v4.1 — Progress tracking (questions attempted/solved)
Then        v5.0 — Class 11 & 12 exercises
Then        v6.0 — Mobile app (React Native)
```

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a branch: `git checkout -b fix/your-fix`
3. Commit: `git commit -m "fix: description"`
4. Push: `git push origin fix/your-fix`
5. Open a Pull Request

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

<div align="center">
  Made with ❤️ by <strong>Sarika</strong>
  <br><br>
  <a href="https://advanced-mathematics-assistant-zvlizldwugwffind.streamlit.app/">🚀 Live Demo</a> &nbsp;·&nbsp;
  <a href="https://github.com/sarika-stack23/AdvMAthAI/issues">🐛 Report Bug</a> &nbsp;·&nbsp;
  <a href="https://github.com/sarika-stack23/AdvMAthAI/issues">💡 Request Feature</a>
</div>