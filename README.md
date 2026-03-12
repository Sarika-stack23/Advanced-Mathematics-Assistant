<div align="center">

# ∫ Advanced Mathematics Assistant

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://advanced-mathematics-assistant-zvlizldwugwffind.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-RAG-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)](https://langchain.com)
[![Groq](https://img.shields.io/badge/Groq-LLaMA%203.3-F55036?style=for-the-badge)](https://groq.com)

**An AI-powered mathematics assistant that solves problems step-by-step from Class 1 to JEE level.**

[**🚀 Try Live Demo**](https://advanced-mathematics-assistant-zvlizldwugwffind.streamlit.app/) · [Report Bug](https://github.com/sarika-stack23/AdvMAthAI/issues) · [Request Feature](https://github.com/sarika-stack23/AdvMAthAI/issues)

</div>

---

## 📸 Screenshots

| Dark Mode | Light Mode |
|---|---|
| ![Dark](https://via.placeholder.com/400x250/0d1220/60a5fa?text=Dark+Mode) | ![Light](https://via.placeholder.com/400x250/f8fafc/2563eb?text=Light+Mode) |

> Replace placeholders above with real screenshots from your live app.

---

## ✨ Features

- 🧮 **Step-by-step solutions** — NCERT/CBSE style, auto-detects difficulty (Class 1–12 / JEE)
- ⚡ **Symbolic computation** — exact derivatives, integrals, equation solving via SymPy
- 📈 **Graph plotter** — visualize any mathematical function instantly
- 📄 **PDF upload** — upload textbooks or question papers and ask anything
- 📷 **Camera / image scan** — snap a photo of a handwritten problem, auto-solves
- 💬 **Chat memory** — remembers conversation context (MongoDB or in-memory)
- 🌗 **Dark / light theme** — toggle in sidebar
- 🔄 **Auto model fallback** — if Groq daily limit hit, silently switches to backup model
- 🔒 **Secure** — no `eval()` on user input, all API keys via environment variables

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| UI | Streamlit |
| LLM | Groq (llama-3.3-70b-versatile) |
| Embeddings | HuggingFace sentence-transformers/all-MiniLM-L6-v2 |
| Vector DB | ChromaDB (default) or FAISS |
| Symbolic Math | SymPy |
| OCR | Tesseract + pytesseract |
| Memory | MongoDB Atlas (optional) or in-memory |
| RAG Framework | LangChain |

---

## ⚙️ Local Setup

### Prerequisites

- Python 3.11+
- [Groq API key](https://console.groq.com) (free)

### 1. Clone the repo

```bash
git clone https://github.com/sarika-stack23/AdvMAthAI.git
cd AdvMAthAI
```

### 2. Create virtual environment

```bash
python3.11 -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Tesseract (for camera scan)

```bash
# macOS
brew install tesseract

# Linux
sudo apt install tesseract-ocr

# Windows — download installer:
# https://github.com/UB-Mannheim/tesseract/wiki
```

### 5. Configure `.env`

```bash
cp .env.example .env
```

Edit `.env` and fill in your keys:

```env
GROQ_API_KEY=your_groq_api_key_here        # Free at console.groq.com
HUGGINGFACE_API_TOKEN=your_token_here      # Free at huggingface.co
MONGODB_URI=                               # Optional — leave empty for in-memory
```

### 6. Run

```bash
python3.11 -m streamlit run main.py
```

Open **http://localhost:8501** 🎉

---

## 🔑 Getting a Free Groq API Key

1. Go to [console.groq.com](https://console.groq.com)
2. Sign up (free)
3. Go to **API Keys** → **Create API Key**
4. Paste in `.env` as `GROQ_API_KEY=gsk_...`

**Free tier limits — app handles all of this automatically:**

| Model | Tokens/Day | Role |
|---|---|---|
| llama-3.3-70b-versatile | 100,000 | Primary (best quality) |
| llama3-8b-8192 | 500,000 | Fallback 1 (auto-switch) |
| mixtral-8x7b-32768 | 500,000 | Fallback 2 (auto-switch) |

> When the primary model hits its daily limit, the app **automatically switches** to the next model and switches back the next day. No manual changes needed.

---

## ☁️ Deploy to Streamlit Cloud

1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io) → **New app**
3. Select your repo → set main file to `main.py`
4. Go to **Settings → Secrets** and paste:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
HUGGINGFACE_API_TOKEN = "your_token_here"
LLM_MODEL = "llama-3.3-70b-versatile"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
VECTOR_DB_TYPE = "chroma"
CHROMA_PERSIST_DIR = "./chroma_db"
FAISS_INDEX_PATH = "./faiss_index"
MONGODB_URI = ""
MONGODB_DB_NAME = "math_assistant"
MONGODB_COLLECTION = "chat_history"
CHUNK_SIZE = "1000"
CHUNK_OVERLAP = "200"
TOP_K_RESULTS = "5"
APP_TITLE = "Advanced Mathematics Assistant"
DEBUG = "False"
```

5. Click **Deploy** 🚀

---

## 📁 Project Structure

```
AdvMAthAI/
├── main.py               # All 7 pipeline steps in one file
├── .env                  # Your API keys (never commit this)
├── .env.example          # Template — safe to commit
├── .gitignore            # Excludes .env, venv, chroma_db etc.
├── requirements.txt      # Python dependencies
├── README.md             # This file
├── chroma_db/            # Vector DB (auto-created, gitignored)
└── faiss_index/          # FAISS index (auto-created, gitignored)
```

---

## 🧪 CLI Commands

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
| Daily token limit | App auto-switches model — just keep using it |
| ChromaDB error | Delete `chroma_db/` folder and restart |
| Slow first load | Normal — embedding model downloads once, then instant |
| Meta tensor error on startup | Pinned versions in `requirements.txt` fix this — run `pip install -r requirements.txt` |
| OCR / camera scan not working | Run `pip install pytesseract` then `brew install tesseract` (Mac) |
| Wrong image shows pytesseract error | Fixed in v1.2.0 — update to latest `main.py` |
| Math symbols look broken (π, ∑) | Fixed in v1.2.0 — app now uses plain Unicode, no LaTeX |
| App crashes on startup | Make sure you run with `python3.11 -m streamlit run main.py` |

---

## 📝 Changelog

### v1.2.0 — March 2026
- ✅ Fixed OCR logic — wrong image no longer shows pytesseract install error
- ✅ Fixed tesseract binary path for macOS Apple Silicon (`/opt/homebrew/bin/tesseract`)
- ✅ Added `pytesseract` to `requirements.txt` — no more missing package on fresh install
- ✅ OS-tabbed install instructions (macOS / Linux / Windows) in sidebar
- ✅ Replaced broken LaTeX (`$\frac{\pi^2}{6}$`) with clean Unicode (π²/6)
- ✅ Pinned `sentence-transformers==2.7.0` + `transformers==4.40.2` — fixes meta tensor crash
- ✅ Added `numpy<2.0.0` pin — fixes torch 2.2.x compatibility

### v1.1.0 — March 2026
- ✅ Auto model fallback (70B → 8B → Mixtral) on daily token limit
- ✅ Streamlit Cloud secrets support (`st.secrets` auto-loaded)
- ✅ Fixed widget key bug — questions always get answers now
- ✅ Fixed LangChain template crash on math content with `{ }` braces
- ✅ `load_dotenv` uses explicit path — works from any launch directory
- ✅ Module-level caching for embeddings, LLM, pipeline (fast reruns)
- ✅ `ast.literal_eval` replaces unsafe `eval()` in matrix operations
- ✅ `datetime.now(timezone.utc)` replaces deprecated `utcnow()`
- ✅ Temp file collision fix using `tempfile.mkstemp()`
- ✅ WebBaseLoader 15s timeout
- ✅ Smart error messages with exact retry time from Groq

### v1.0.0 — Initial Release
- 🎉 Full RAG pipeline with ChromaDB / FAISS
- 🎉 Streamlit UI with dark/light theme
- 🎉 Symbolic math via SymPy
- 🎉 PDF upload, camera scan, graph plotter
- 🎉 MongoDB chat memory

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