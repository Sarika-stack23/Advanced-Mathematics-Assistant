# ∫ Advanced Mathematics Assistant

> **Live Demo → [advanced-mathematics-assistant-zvlizldwugwffind.streamlit.app](https://advanced-mathematics-assistant-zvlizldwugwffind.streamlit.app/)**

An AI-powered mathematics assistant built with **Streamlit**, **LangChain**, **Groq LLM**, and **RAG**. Solves math problems step-by-step from Class 1 to JEE level with symbolic computation, graph plotting, PDF upload, and camera scan.

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

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| UI | Streamlit |
| LLM | Groq (llama-3.3-70b-versatile) |
| Embeddings | HuggingFace sentence-transformers/all-MiniLM-L6-v2 |
| Vector DB | ChromaDB (default) or FAISS |
| Symbolic Math | SymPy |
| Memory | MongoDB Atlas (optional) or in-memory |
| RAG Framework | LangChain |

---

## ⚙️ Local Setup

### 1. Clone the repo

```bash
git clone https://github.com/your-username/AdvMAthAI.git
cd AdvMAthAI
```

### 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure `.env`

```bash
cp .env.example .env
```

Edit `.env` and fill in your keys:

```env
GROQ_API_KEY=your_groq_api_key_here        # Free at console.groq.com
HUGGINGFACE_API_TOKEN=your_token_here      # Free at huggingface.co
MONGODB_URI=                               # Optional — leave empty for in-memory
```

### 5. Run

```bash
streamlit run main.py
```

Open **http://localhost:8501**

---

## 🔑 Getting a Free Groq API Key

1. Go to [console.groq.com](https://console.groq.com)
2. Sign up (free)
3. Go to **API Keys** → **Create API Key**
4. Paste in `.env` as `GROQ_API_KEY=...`

**Free tier limits:**

| Model | Tokens/Day | Auto-fallback |
|---|---|---|
| llama-3.3-70b-versatile | 100,000 | Primary |
| llama3-8b-8192 | 500,000 | Fallback 1 |
| mixtral-8x7b-32768 | 500,000 | Fallback 2 |

> The app **automatically switches** to fallback models if the daily limit is hit — no `.env` changes needed.

---

## ☁️ Deploy to Streamlit Cloud

1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io) → **New app**
3. Select your repo and `main.py`
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
├── .gitignore
├── requirements.txt
├── README.md
├── chroma_db/            # Vector DB (auto-created, gitignored)
└── faiss_index/          # FAISS index (auto-created, gitignored)
```

---

## 🧪 CLI Commands

```bash
streamlit run main.py        # Launch UI
python main.py --setup       # Build knowledge base
python main.py --rebuild     # Force rebuild knowledge base
python main.py --test        # Run unit tests
python main.py --eval        # Evaluate RAG pipeline
```

---

## 🐛 Troubleshooting

| Problem | Fix |
|---|---|
| No answer shown | Check Groq API key in Streamlit Cloud Secrets |
| Daily token limit | App auto-switches model — just keep using it |
| ChromaDB error | Delete `chroma_db/` folder and restart |
| Slow first load | Normal — embedding model downloads once then cached |
| OCR not working | `pip install pytesseract` + `brew install tesseract` |
| README disappears on push | Run `git add README.md && git commit -m "docs: readme"` |

---

## 📝 Changelog

### Latest fixes
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

---

## 🤝 Contributing

1. Fork the repo
2. Create a branch: `git checkout -b fix/your-fix`
3. Commit: `git commit -m "fix: description"`
4. Push and open a Pull Request

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

<div align="center">
  Made with ❤️ by Sarika &nbsp;·&nbsp;
  <a href="https://advanced-mathematics-assistant-zvlizldwugwffind.streamlit.app/">Live Demo</a>
</div>