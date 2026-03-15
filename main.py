"""
╔══════════════════════════════════════════════════════════════════════╗
║          ADVANCED MATHEMATICS ASSISTANT — main.py                   ║
║  All 7 pipeline steps in one file                                   ║
║                                                                      ║
║  USAGE:                                                              ║
║    python3.11 -m streamlit run main.py   → Launch UI                ║
║    python3.11 main.py --setup            → Build knowledge base     ║
║    python3.11 main.py --test             → Run all tests            ║
║    python3.11 main.py --eval             → Evaluate RAG pipeline    ║
║    python3.11 main.py --rebuild          → Force rebuild KB         ║
╚══════════════════════════════════════════════════════════════════════╝
"""

import os, re, sys, json, time, uuid, hashlib, logging, argparse, unittest, ast, tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple

from dotenv import load_dotenv
# Load .env locally — works regardless of launch directory
load_dotenv(dotenv_path=Path(__file__).parent / ".env", override=True)

# Streamlit Cloud: load secrets into environment variables
try:
    import streamlit as st
    for _k, _v in st.secrets.items():
        if _k not in os.environ:
            os.environ[_k] = str(_v)
except Exception:
    pass  # Not running on Streamlit Cloud or secrets not configured

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("math_assistant")

GROQ_API_KEY       = os.getenv("GROQ_API_KEY", "")
# llama-3.3-70b-versatile: powerful but low RPM on Groq free tier (30 RPM)
# llama3-8b-8192: higher RPM limit (30 RPM but faster + less likely to hit TPM limits)
# mixtral-8x7b-32768: good balance — use this if hitting rate limits
LLM_MODEL          = os.getenv("LLM_MODEL", "llama-3.3-70b-versatile")
EMBEDDING_MODEL    = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
VECTOR_DB_TYPE     = os.getenv("VECTOR_DB_TYPE", "chroma").lower()
CHROMA_PERSIST_DIR = os.getenv("CHROMA_PERSIST_DIR", "./chroma_db")
FAISS_INDEX_PATH   = os.getenv("FAISS_INDEX_PATH", "./faiss_index")
TOP_K_RESULTS      = int(os.getenv("TOP_K_RESULTS", "5"))
CHUNK_SIZE         = int(os.getenv("CHUNK_SIZE", "1000"))
CHUNK_OVERLAP      = int(os.getenv("CHUNK_OVERLAP", "200"))
MONGODB_URI        = os.getenv("MONGODB_URI", "")
MONGODB_DB_NAME    = os.getenv("MONGODB_DB_NAME", "math_assistant")
MONGODB_COLLECTION = os.getenv("MONGODB_COLLECTION", "chat_history")
COLLECTION_NAME    = "math_knowledge_base"

try:
    from langchain_core.documents import Document
except ImportError:
    try:
        from langchain.schema import Document
    except ImportError:
        class Document:
            def __init__(self, page_content: str, metadata: dict = None):
                self.page_content = page_content
                self.metadata = metadata or {}

try:
    from langchain_core.messages import HumanMessage, AIMessage
except ImportError:
    from langchain.schema import HumanMessage, AIMessage

try:
    from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
except ImportError:
    from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder


# ╔══════════════════════════════════════════════════════════════════════╗
# ║  STEP 1 — DATA SOURCES                                              ║
# ╚══════════════════════════════════════════════════════════════════════╝

MATH_KNOWLEDGE_BASE = [
    Document(page_content="""Calculus Fundamentals:
The derivative of f(x) measures the rate of change. Key rules:
- Power Rule: d/dx[x^n] = n*x^(n-1)
- Product Rule: d/dx[f*g] = f'g + fg'
- Chain Rule: d/dx[f(g(x))] = f'(g(x)) * g'(x)
- Quotient Rule: d/dx[f/g] = (f'g - fg') / g^2
Common derivatives:
- d/dx[sin(x)] = cos(x)
- d/dx[cos(x)] = -sin(x)
- d/dx[e^x] = e^x
- d/dx[ln(x)] = 1/x
Integration (antiderivative):
- integral(x^n dx) = x^(n+1)/(n+1) + C
- integral(e^x dx) = e^x + C
- integral(sin(x) dx) = -cos(x) + C
- integral(cos(x) dx) = sin(x) + C
Fundamental Theorem of Calculus:
integral[a to b] f(x) dx = F(b) - F(a)  where F'(x) = f(x)""",
    metadata={"source": "knowledge_base", "topic": "calculus"}),

    Document(page_content="""Linear Algebra Essentials:
Matrix Operations:
- Matrix multiplication (A*B): row-by-column dot products
- Transpose (A^T): flip rows and columns
- Determinant of 2x2: det([[a,b],[c,d]]) = ad - bc
- Inverse: A^(-1) exists iff det(A) != 0
Eigenvalues and Eigenvectors:
- Av = lambda*v  where lambda = eigenvalue, v = eigenvector
- Find eigenvalues: det(A - lambda*I) = 0 (characteristic equation)
- Eigenvectors: solve (A - lambda*I)v = 0
Vector Spaces:
- Span, basis, dimension
- Linear independence: no vector is a combination of others
- Rank-Nullity Theorem: rank(A) + nullity(A) = n (columns)
Dot Product & Norms:
- u dot v = |u||v|cos(theta)
- ||v|| = sqrt(v1^2 + v2^2 + ... + vn^2)
- Orthogonal: u dot v = 0""",
    metadata={"source": "knowledge_base", "topic": "linear_algebra"}),

    Document(page_content="""Statistics & Probability:
Descriptive Statistics:
- Mean: mu = sum(x) / n
- Variance: sigma^2 = sum((x - mu)^2) / n
- Standard Deviation: sigma = sqrt(variance)
- Median: middle value when sorted
- Mode: most frequent value
Probability Rules:
- P(A union B) = P(A) + P(B) - P(A intersection B)
- P(A | B) = P(A intersection B) / P(B)
- Bayes Theorem: P(A|B) = P(B|A)*P(A) / P(B)
- Independent events: P(A intersection B) = P(A) * P(B)
Distributions:
- Normal: bell curve, described by mu and sigma
- Binomial: P(X=k) = C(n,k) * p^k * (1-p)^(n-k)
- Poisson: P(X=k) = (lambda^k * e^(-lambda)) / k!
Central Limit Theorem:
Sample means approach normal distribution as n approaches infinity""",
    metadata={"source": "knowledge_base", "topic": "statistics"}),

    Document(page_content="""Algebra & Number Theory:
Quadratic Formula:
x = (-b +/- sqrt(b^2 - 4ac)) / 2a  for ax^2 + bx + c = 0
Discriminant: D = b^2 - 4ac
- D > 0: two real roots
- D = 0: one real root (repeated)
- D < 0: two complex roots
Logarithm Rules:
- log(ab) = log(a) + log(b)
- log(a/b) = log(a) - log(b)
- log(a^n) = n*log(a)
- log_b(x) = ln(x) / ln(b)
Polynomial Factoring Patterns:
- a^2 - b^2 = (a+b)(a-b)
- a^3 + b^3 = (a+b)(a^2 - ab + b^2)
- a^3 - b^3 = (a-b)(a^2 + ab + b^2)
Sequences & Series:
- Arithmetic: a_n = a_1 + (n-1)d,  Sum = n(a_1 + a_n)/2
- Geometric: a_n = a_1 * r^(n-1),  Sum = a_1(1-r^n)/(1-r)
- Infinite geometric (|r|<1): Sum = a_1 / (1-r)""",
    metadata={"source": "knowledge_base", "topic": "algebra"}),

    Document(page_content="""Trigonometry:
Unit Circle & Basic Identities:
- sin^2(x) + cos^2(x) = 1
- tan(x) = sin(x)/cos(x)
- sec(x) = 1/cos(x),  csc(x) = 1/sin(x),  cot(x) = 1/tan(x)
Angle Sum Formulas:
- sin(A+B) = sin(A)cos(B) + cos(A)sin(B)
- cos(A+B) = cos(A)cos(B) - sin(A)sin(B)
Double Angle:
- sin(2x) = 2sin(x)cos(x)
- cos(2x) = cos^2(x) - sin^2(x)
Key Values:
- sin(0)=0, sin(pi/6)=1/2, sin(pi/4)=sqrt(2)/2, sin(pi/3)=sqrt(3)/2, sin(pi/2)=1
- cos(0)=1, cos(pi/6)=sqrt(3)/2, cos(pi/4)=sqrt(2)/2, cos(pi/3)=1/2, cos(pi/2)=0
Law of Sines: a/sin(A) = b/sin(B) = c/sin(C)
Law of Cosines: c^2 = a^2 + b^2 - 2ab*cos(C)""",
    metadata={"source": "knowledge_base", "topic": "trigonometry"}),

    Document(page_content="""Discrete Mathematics:
Combinatorics:
- Permutations (ordered): P(n,r) = n! / (n-r)!
- Combinations (unordered): C(n,r) = n! / (r!(n-r)!)
- Pigeonhole Principle: n+1 objects in n boxes means at least one box has 2+ objects
Graph Theory:
- Euler path: visits every edge once (exists if 0 or 2 odd-degree vertices)
- Hamiltonian path: visits every vertex once
- Tree: connected graph with n-1 edges for n vertices
- Degree sum = 2 * number of edges
Number Theory:
- GCD(a,b) via Euclidean algorithm: GCD(a,b) = GCD(b, a mod b)
- LCM(a,b) = a*b / GCD(a,b)
- Modular arithmetic: a congruent to b (mod n) means n divides (a-b)
- Fermat's Little Theorem: a^(p-1) congruent to 1 (mod p) for prime p
Logic:
- De Morgan's: NOT(A AND B) = NOT(A) OR NOT(B)
- De Morgan's: NOT(A OR B) = NOT(A) AND NOT(B)""",
    metadata={"source": "knowledge_base", "topic": "discrete_math"}),
]


class MathDataLoader:
    def __init__(self):
        self.documents = []

    def load_builtin_knowledge(self):
        logger.info(f"Loading {len(MATH_KNOWLEDGE_BASE)} built-in knowledge documents")
        return list(MATH_KNOWLEDGE_BASE)

    def load_pdf(self, pdf_path: str):
        try:
            from langchain_community.document_loaders import PyPDFLoader
            docs = PyPDFLoader(pdf_path).load()
            logger.info(f"Loaded {len(docs)} pages from: {pdf_path}")
            return docs
        except Exception as e:
            logger.error(f"Failed to load PDF {pdf_path}: {e}")
            return []

    def load_pdfs_from_directory(self, dir_path: str):
        try:
            from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
            docs = DirectoryLoader(dir_path, glob="**/*.pdf", loader_cls=PyPDFLoader).load()
            logger.info(f"Loaded {len(docs)} documents from: {dir_path}")
            return docs
        except Exception as e:
            logger.error(f"Failed to load PDFs from {dir_path}: {e}")
            return []

    def load_web_pages(self, urls: List[str]):
        from langchain_community.document_loaders import WebBaseLoader
        import socket
        docs = []
        for url in urls:
            try:
                loader = WebBaseLoader(url)
                loader.requests_kwargs = {"timeout": 15}
                docs.extend(loader.load())
                logger.info(f"Loaded: {url}")
            except Exception as e:
                logger.warning(f"Failed URL {url}: {e}")
        return docs

    def load_text_file(self, file_path: str):
        try:
            if file_path.endswith(".md"):
                from langchain_community.document_loaders import UnstructuredMarkdownLoader
                loader = UnstructuredMarkdownLoader(file_path)
            else:
                from langchain_community.document_loaders import TextLoader
                loader = TextLoader(file_path, encoding="utf-8")
            docs = loader.load()
            logger.info(f"Loaded: {file_path}")
            return docs
        except Exception as e:
            logger.error(f"Failed to load {file_path}: {e}")
            return []

    def load_all(self, pdf_paths=None, urls=None, text_paths=None, pdf_directory=None):
        all_docs = self.load_builtin_knowledge()
        if pdf_paths:
            for p in pdf_paths: all_docs.extend(self.load_pdf(p))
        if pdf_directory and os.path.exists(pdf_directory):
            all_docs.extend(self.load_pdfs_from_directory(pdf_directory))
        if urls:
            all_docs.extend(self.load_web_pages(urls))
        if text_paths:
            for p in text_paths: all_docs.extend(self.load_text_file(p))
        logger.info(f"Total documents loaded: {len(all_docs)}")
        self.documents = all_docs
        return all_docs


# ╔══════════════════════════════════════════════════════════════════════╗
# ║  STEP 2 — DATA PREPROCESSING                                        ║
# ╚══════════════════════════════════════════════════════════════════════╝

class MathDataPreprocessor:
    TOPIC_KEYWORDS: Dict[str, List[str]] = {
        "calculus":       ["derivative", "integral", "differentiate", "integrate", "limit", "continuity", "taylor"],
        "linear_algebra": ["matrix", "vector", "eigenvalue", "determinant", "rank", "span", "basis"],
        "statistics":     ["probability", "distribution", "mean", "variance", "regression", "hypothesis"],
        "algebra":        ["polynomial", "equation", "quadratic", "factor", "root", "logarithm", "exponent"],
        "trigonometry":   ["sine", "cosine", "tangent", "angle", "radian", "unit circle", "trig"],
        "discrete_math":  ["graph", "combinatorics", "permutation", "combination", "modular", "prime"],
        "geometry":       ["triangle", "circle", "area", "volume", "perimeter", "pythagorean", "coordinate"],
        "number_theory":  ["prime", "divisor", "gcd", "lcm", "modular", "congruence", "integer"],
    }

    def __init__(self):
        self._seen_hashes: set = set()

    def _clean(self, text: str) -> str:
        text = re.sub(r"\n{3,}", "\n\n", text)
        text = re.sub(r"[ \t]{2,}", " ", text)
        text = re.sub(r"Page\s+\d+\s+of\s+\d+", "", text, flags=re.IGNORECASE)
        text = re.sub(r"https?://\S+", "[URL]", text)
        text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]", "", text)
        replacements = {
            "\u2019": "'", "\u201c": '"', "\u201d": '"',
            "\u2013": "-", "\u2014": "--", "\u00a0": " ",
            "\u03c0": "pi", "\u221e": "infinity",
            "\u2264": "<=", "\u2265": ">="
        }
        for old, new in replacements.items():
            text = text.replace(old, new)
        return text.strip()

    def _detect_topic(self, text: str) -> str:
        tl = text.lower()
        scores = {t: sum(1 for kw in kws if kw in tl) for t, kws in self.TOPIC_KEYWORDS.items()}
        scores = {k: v for k, v in scores.items() if v > 0}
        return max(scores, key=scores.get) if scores else "general_math"

    def _difficulty(self, text: str) -> str:
        adv = ["eigenvalue", "differential equation", "fourier", "laplace", "manifold", "tensor"]
        mid = ["derivative", "integral", "matrix", "probability", "polynomial", "logarithm"]
        tl = text.lower()
        if sum(1 for t in adv if t in tl) >= 2: return "advanced"
        if sum(1 for t in mid if t in tl) >= 2: return "intermediate"
        return "beginner"

    def preprocess_document(self, doc):
        text = doc.page_content
        if len(text.strip()) < 50:
            return None
        text = self._clean(text)
        h = hashlib.md5(text.strip().lower().encode()).hexdigest()
        if h in self._seen_hashes:
            return None
        self._seen_hashes.add(h)
        meta = doc.metadata.copy()
        meta.update({
            "topic":        meta.get("topic") or self._detect_topic(text),
            "difficulty":   self._difficulty(text),
            "char_count":   len(text),
            "word_count":   len(text.split()),
            "content_hash": h,
        })
        return Document(page_content=text, metadata=meta)

    def preprocess_documents(self, documents):
        logger.info(f"Preprocessing {len(documents)} documents...")
        self._seen_hashes.clear()
        processed = [r for doc in documents if (r := self.preprocess_document(doc)) is not None]
        logger.info(f"Done: {len(processed)} kept, {len(documents)-len(processed)} skipped")
        return processed


# ╔══════════════════════════════════════════════════════════════════════╗
# ║  STEP 3 — SPLITTING AND CHUNKING                                    ║
# ╚══════════════════════════════════════════════════════════════════════╝

class MathTextSplitter:
    def __init__(self, chunk_size: int = CHUNK_SIZE, chunk_overlap: int = CHUNK_OVERLAP):
        from langchain_text_splitters import RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.recursive = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size, chunk_overlap=chunk_overlap,
            separators=["\n\n", "\n", ". ", "! ", "? ", "; ", ": ", " ", ""])
        self.markdown_splitter = MarkdownHeaderTextSplitter(
            headers_to_split_on=[("#", "H1"), ("##", "H2"), ("###", "H3")])

    def split_document(self, doc):
        source = doc.metadata.get("source", "").lower()
        if source.endswith(".md") or "markdown" in source:
            try:
                splits = self.markdown_splitter.split_text(doc.page_content)
                chunks = [Document(page_content=s.page_content,
                                   metadata={**doc.metadata, **s.metadata}) for s in splits]
            except Exception:
                chunks = self.recursive.split_documents([doc])
        else:
            chunks = self.recursive.split_documents([doc])
        for i, chunk in enumerate(chunks):
            chunk.metadata.update({
                "chunk_index":  i,
                "total_chunks": len(chunks),
                "chunk_size":   len(chunk.page_content),
            })
        return chunks

    def split_documents(self, documents):
        logger.info(f"Splitting {len(documents)} documents...")
        all_chunks = []
        for doc in documents:
            all_chunks.extend(self.split_document(doc))
        logger.info(f"Created {len(all_chunks)} chunks")
        return all_chunks


# ╔══════════════════════════════════════════════════════════════════════╗
# ║  STEP 4 — EMBEDDINGS, VECTOR DB & KNOWLEDGE BASE                   ║
# ╚══════════════════════════════════════════════════════════════════════╝

_EMBEDDINGS_CACHE = {}
def get_embeddings():
    if "model" not in _EMBEDDINGS_CACHE:
        from langchain_huggingface import HuggingFaceEmbeddings
        logger.info(f"Loading embedding model: {EMBEDDING_MODEL}")
        _EMBEDDINGS_CACHE["model"] = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL,
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": True})
    return _EMBEDDINGS_CACHE["model"]


class MathVectorStore:
    def __init__(self):
        self.embeddings = get_embeddings()
        self.vectorstore = None
        self.db_type = VECTOR_DB_TYPE
        self._load_existing()

    def _load_existing(self):
        if self.db_type == "chroma":
            self._try_chroma()
        else:
            self._try_faiss()

    def _try_chroma(self, documents=None):
        try:
            from langchain_community.vectorstores import Chroma
            persist_path = Path(CHROMA_PERSIST_DIR)
            persist_path.mkdir(parents=True, exist_ok=True)
            if documents:
                self.vectorstore = Chroma.from_documents(
                    documents=documents, embedding=self.embeddings,
                    collection_name=COLLECTION_NAME,
                    persist_directory=str(persist_path))
                logger.info("ChromaDB created.")
            elif list(persist_path.glob("*.sqlite3")):
                self.vectorstore = Chroma(
                    collection_name=COLLECTION_NAME,
                    embedding_function=self.embeddings,
                    persist_directory=str(persist_path))
                logger.info(f"ChromaDB loaded ({self.vectorstore._collection.count()} docs)")
        except Exception as e:
            logger.warning(f"ChromaDB failed ({type(e).__name__}: {e}), switching to FAISS")
            self.db_type = "faiss"
            if documents:
                self._try_faiss(documents)

    def _try_faiss(self, documents=None):
        try:
            from langchain_community.vectorstores import FAISS
            index_path = Path(FAISS_INDEX_PATH)
            if documents:
                self.vectorstore = FAISS.from_documents(documents, self.embeddings)
                index_path.mkdir(parents=True, exist_ok=True)
                self.vectorstore.save_local(str(index_path))
                logger.info(f"FAISS saved to {index_path}")
            elif index_path.exists() and any(index_path.iterdir()):
                self.vectorstore = FAISS.load_local(
                    str(index_path), self.embeddings,
                    allow_dangerous_deserialization=True)
                logger.info("FAISS loaded.")
        except Exception as e:
            logger.error(f"FAISS failed: {e}")

    def build_knowledge_base(self, documents):
        logger.info(f"Building knowledge base with {len(documents)} chunks...")
        if self.db_type == "chroma":
            self._try_chroma(documents)
        else:
            self._try_faiss(documents)
        logger.info("Knowledge base ready.")

    def add_documents(self, documents):
        if self.vectorstore is None:
            self.build_knowledge_base(documents)
        else:
            self.vectorstore.add_documents(documents)

    def similarity_search(self, query: str, k: int = TOP_K_RESULTS, filter_topic: str = None):
        if self.vectorstore is None:
            return []
        try:
            if filter_topic and self.db_type == "chroma":
                return self.vectorstore.similarity_search(query, k=k, filter={"topic": filter_topic})
            return self.vectorstore.similarity_search(query, k=k)
        except Exception as e:
            logger.error(f"Search failed: {e}")
            return []

    def as_retriever(self, k: int = TOP_K_RESULTS):
        return self.vectorstore.as_retriever(search_kwargs={"k": k}) if self.vectorstore else None

    def get_document_count(self) -> int:
        if self.vectorstore is None:
            return 0
        try:
            return (self.vectorstore._collection.count() if self.db_type == "chroma"
                    else self.vectorstore.index.ntotal)
        except Exception as e:
            logger.error(f"get_document_count failed: {e}")
            return 0

    def is_ready(self) -> bool:
        return self.vectorstore is not None and self.get_document_count() > 0


_PIPELINE_CACHE = {}
def build_pipeline(pdf_paths=None, urls=None, text_paths=None, force_rebuild=False) -> MathVectorStore:
    """Cached — runs once per process. Embedding model + KB build only happens on cold start."""
    if "store" in _PIPELINE_CACHE and not force_rebuild:
        return _PIPELINE_CACHE["store"]
    store = MathVectorStore()
    if store.is_ready() and not force_rebuild:
        logger.info(f"Knowledge base already built ({store.get_document_count()} docs).")
        _PIPELINE_CACHE["store"] = store
        return store
    raw_docs   = MathDataLoader().load_all(pdf_paths=pdf_paths or [], urls=urls or [], text_paths=text_paths or [])
    clean_docs = MathDataPreprocessor().preprocess_documents(raw_docs)
    chunks     = MathTextSplitter().split_documents(clean_docs)
    store.build_knowledge_base(chunks)
    _PIPELINE_CACHE["store"] = store
    return store


# ╔══════════════════════════════════════════════════════════════════════╗
# ║  STEP 5 — QUERY PROCESSING & AI ENGINE                              ║
# ╚══════════════════════════════════════════════════════════════════════╝

SYSTEM_TEMPLATE = """You are an expert Indian mathematics teacher who teaches Class 1 to Class 12 (NCERT/CBSE syllabus) as well as JEE and competitive math.

⚠️ NON-MATH QUESTIONS — STRICT RULE:
If the question is NOT about mathematics (e.g. today's date, general knowledge, medicine, biology, history, news, food, sports, greetings, or anything unrelated to math), respond with ONLY this one line and nothing else:
"❌ I'm a Mathematics Assistant. I can only help with math questions. Please ask a math problem!"
Do NOT use the step format. Do NOT try to answer. Stop immediately after this one line.

Detect the difficulty level from the question and respond accordingly:
- Class 1–5: Use very simple language, basic steps, real-life examples
- Class 6–10: Clear step-by-step, show all working, NCERT style
- Class 11–12 / JEE: Detailed working, mention theorems/formulas used

EXACT FORMAT — follow this every time for math questions:

━━━━━━━━━━━━━━━━━━━━━━━━━━━
Question: [restate the question clearly]
━━━━━━━━━━━━━━━━━━━━━━━━━━━

Step 1 — [title]

   [working]

Step 2 — [title] (only if needed)

   [working]

━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Answer: [final answer, boxed and clear]
━━━━━━━━━━━━━━━━━━━━━━━━━━━

STRICT RULES:
- Always complete the full solution — never stop mid-answer
- Each step must be DIFFERENT — never repeat a step
- Use ONLY as many steps as the problem genuinely needs — 1 step for trivial problems, 2 for simple, 3–5 for medium, up to 8 for complex
- NEVER add fake or redundant steps just to reach a minimum count
- Each step must add NEW information only
- NEVER use LaTeX or $ symbols. Write all math in plain Unicode text only.
-- Use these Unicode symbols directly: π, ², ³, √, ∑, ∫, ∞, ±, ≤, ≥, ≠, ×, ÷, α, β, θ
- NEVER write sqrt() — always use √ symbol. Example: √(b² - 4ac) NOT sqrt(b² - 4ac)
- NEVER write ^2 or ^3 — always use ² ³. Example: x² NOT x^2
- NEVER write pi — always use π
- NEVER write +/- — always use ±
- Write fractions as: (numerator)/(denominator) e.g. (π²)/6
- Write powers as: x², x³, xⁿ or x^n
- Write summations as: ∑(n=1 to ∞) 1/n²
- Example answer: ✅ Answer: ∑(n=1 to ∞) 1/n² = π²/6
- NEVER repeat a step
- STOP after the answer — no extra notes or commentary
- If question is in Hindi or mixed language, answer in the same language

Context from knowledge base:
{context}
"""


class MongoDBChatMemory:
    def __init__(self, session_id: str = "default"):
        self.session_id = session_id
        self.collection = None
        self._memory: List[Dict] = []
        self._connect()

    def _connect(self):
        if not MONGODB_URI:
            return
        try:
            from pymongo import MongoClient
            client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=5000)
            client.admin.command("ping")
            self.collection = client[MONGODB_DB_NAME][MONGODB_COLLECTION]
            logger.info("MongoDB connected")
        except Exception as e:
            logger.warning(f"MongoDB unavailable ({e}), using in-memory history")

    def add_message(self, role: str, content: str):
        msg = {"session_id": self.session_id, "role": role,
               "content": content, "timestamp": datetime.now(timezone.utc)}
        if self.collection is not None:
            try:
                self.collection.insert_one(msg)
                return
            except Exception:
                pass
        self._memory.append(msg)

    def get_history(self, limit: int = 20) -> List[Dict]:
        if self.collection is not None:
            try:
                msgs = list(self.collection.find(
                    {"session_id": self.session_id}).sort("timestamp", -1).limit(limit))
                msgs.reverse()
                return msgs
            except Exception:
                pass
        return self._memory[-limit:]

    def get_langchain_messages(self, limit: int = 10):
        history = self.get_history(limit)
        result = []
        for msg in history:
            if msg["role"] == "human":
                result.append(HumanMessage(content=msg["content"]))
            elif msg["role"] == "assistant":
                result.append(AIMessage(content=msg["content"]))
        return result

    def clear_history(self):
        if self.collection is not None:
            try:
                self.collection.delete_many({"session_id": self.session_id})
            except Exception:
                pass
        self._memory.clear()


class SymbolicMathEngine:
    @staticmethod
    def differentiate(expression: str, variable: str = "x") -> Optional[str]:
        try:
            import sympy as sp
            var = sp.Symbol(variable)
            expr = sp.sympify(re.sub(r'\^', '**', expression.strip()))
            return f"d/d{variable}[{expression}] = {sp.simplify(sp.diff(expr, var))}"
        except Exception:
            return None

    @staticmethod
    def integrate(expression: str, variable: str = "x") -> Optional[str]:
        try:
            import sympy as sp
            var = sp.Symbol(variable)
            expr = sp.sympify(re.sub(r'\^', '**', expression.strip()))
            return f"integral({expression}) d{variable} = {sp.integrate(expr, var)} + C"
        except Exception:
            return None

    @staticmethod
    def solve_equation(equation: str, variable: str = "x") -> Optional[str]:
        try:
            import sympy as sp
            var = sp.Symbol(variable)
            eq_str = re.sub(r'\^', '**', equation.strip())
            if "=" in eq_str:
                lhs, rhs = eq_str.split("=", 1)
                eq = sp.Eq(sp.sympify(lhs), sp.sympify(rhs))
            else:
                eq = sp.sympify(eq_str)
            return f"Solutions for {variable}: {sp.solve(eq, var)}"
        except Exception:
            return None

    @staticmethod
    def try_solve(expression: str) -> Optional[str]:
        try:
            import sympy as sp
            x, y, z, t = sp.symbols('x y z t')
            expr_str = re.sub(r'\^', '**', expression.strip())
            result = sp.simplify(sp.sympify(expr_str, locals={
                'x': x, 'y': y, 'z': z, 't': t,
                'sin': sp.sin, 'cos': sp.cos, 'exp': sp.exp,
                'log': sp.log, 'sqrt': sp.sqrt, 'pi': sp.pi}))
            return str(result)
        except Exception:
            return None

    @staticmethod
    def matrix_operations(matrix_str: str) -> Optional[Dict[str, Any]]:
        try:
            import sympy as sp
            M = sp.Matrix(ast.literal_eval(matrix_str))
            return {"determinant": str(M.det()), "rank": M.rank(),
                    "eigenvalues": str(M.eigenvals()), "trace": str(M.trace())}
        except Exception:
            return None


_LLM_CACHE = {}
# Fallback model order — if primary hits daily token limit, auto-switch
GROQ_MODEL_FALLBACKS = [
    os.getenv("LLM_MODEL", "llama-3.3-70b-versatile"),
    "llama3-8b-8192",
    "mixtral-8x7b-32768",
]

def _get_llm(model=None):
    key = model or GROQ_MODEL_FALLBACKS[0]
    if key not in _LLM_CACHE:
        from langchain_groq import ChatGroq
        api_key = os.getenv("GROQ_API_KEY", "") or GROQ_API_KEY
        if not api_key:
            raise ValueError("GROQ_API_KEY not set. Add it to your .env file.")
        logger.info(f"Initializing Groq LLM: {key}")
        _LLM_CACHE[key] = ChatGroq(groq_api_key=api_key, model_name=key,
                                    temperature=0.1, max_tokens=2048)
    return _LLM_CACHE[key]

class MathAIEngine:
    def __init__(self, vector_store: MathVectorStore = None, session_id: str = "default"):
        self.llm          = self._init_llm()
        self.vector_store = vector_store
        self.memory       = MongoDBChatMemory(session_id=session_id)
        self.symbolic     = SymbolicMathEngine()
        self.session_id   = session_id

    def _init_llm(self):
        # Eagerly init the primary model; fallbacks are created on demand
        return _get_llm(GROQ_MODEL_FALLBACKS[0])

    def _retrieve_context(self, query: str) -> Tuple[list, str]:
        if not self.vector_store or not self.vector_store.is_ready():
            return [], "No knowledge base available. Using general mathematical knowledge."
        docs = self.vector_store.similarity_search(query, k=3)
        if not docs:
            return [], "No specific context found."
        parts = [f"[Reference {i+1} - {d.metadata.get('topic','math')}]\n{d.page_content}"
                 for i, d in enumerate(docs)]
        return docs, "\n\n---\n\n".join(parts)

    def _symbolic_hint(self, query: str) -> Optional[str]:
        ql = query.lower()
        for pattern, action in [
            (r"(?:differentiate|derivative of|d/dx)\s+(.+?)(?:\s+with respect|\s*$)", "diff"),
            (r"(?:integrate|integral of)\s+(.+?)(?:\s+with respect|\s+dx|\s*$)", "int"),
            (r"solve\s+(.+?)\s+(?:for|=)", "solve"),
        ]:
            m = re.search(pattern, ql)
            if m:
                expr = m.group(1).strip()
                result = (self.symbolic.differentiate(expr) if action == "diff"
                          else self.symbolic.integrate(expr) if action == "int"
                          else self.symbolic.solve_equation(expr))
                if result:
                    return f"[Symbolic verification: {result}]"
        return None

    def query(self, user_input: str) -> Dict[str, Any]:
        hint        = self._symbolic_hint(user_input)
        source_docs, context = self._retrieve_context(user_input)
        chat_history = self.memory.get_langchain_messages(limit=4)

        # Build the messages list manually — NEVER pass math content through
        # LangChain format_messages(), because curly braces in math (e.g. {x|x>0},
        # set notation, matrices) are treated as template variables and crash with
        # a KeyError, silently swallowed → user sees no answer at all.
        system_text = SYSTEM_TEMPLATE.replace("{context}", context)
        llm_messages = []
        # System message — use LangChain tuple form which bypasses brace parsing
        from langchain_core.messages import SystemMessage
        llm_messages.append(SystemMessage(content=system_text))
        # Inject chat history
        for msg in chat_history:
            llm_messages.append(msg)
        # Current user question
        llm_messages.append(HumanMessage(content=user_input))

        # Store human message BEFORE LLM call so history order is correct
        self.memory.add_message("human", user_input)

        # Auto-retry with model fallback — if daily limit hit, switch to next model
        answer      = None
        last_error  = None
        used_models = []
        for model_name in GROQ_MODEL_FALLBACKS:
            if model_name in used_models:
                continue
            used_models.append(model_name)
            llm = _get_llm(model_name)
            for _attempt in range(2):  # 2 attempts per model
                try:
                    raw = llm.invoke(llm_messages).content
                    if raw and not any(p in raw.lower() for p in
                                       ["rate limit", "too many requests", "service unavailable"]):
                        answer = raw
                        if model_name != GROQ_MODEL_FALLBACKS[0]:
                            answer = f"*(Using fallback model: {model_name})*\n\n" + answer
                        break
                    else:
                        raise Exception(raw or "Empty response")
                except Exception as e:
                    last_error = e
                    err = str(e).lower()
                    full_err = str(e)
                    logger.warning(f"Model {model_name} attempt {_attempt+1} failed: {e}")
                    if "per day" in full_err or "tokens per day" in full_err:
                        # Daily limit — skip to next model immediately
                        logger.info(f"Daily limit on {model_name}, trying next model...")
                        break
                    elif "429" in full_err or "rate_limit" in err:
                        time.sleep(2 ** _attempt)
                        continue
                    elif "timeout" in err or "connect" in err or "503" in err:
                        time.sleep(1)
                        continue
                    else:
                        break  # non-retryable
            if answer:
                break

        if answer is None:
            full_err = str(last_error)
            err      = full_err.lower()
            logger.error(f"LLM failed: [{type(last_error).__name__}] {full_err}")

            if "401" in full_err or "invalid_api_key" in err:
                answer = "⚠️ Invalid API key. Check GROQ_API_KEY in your .env file."
            elif "429" in full_err or "rate_limit_exceeded" in err:
                # Extract the retry time from Groq's message if present
                import re as _re
                retry_match = _re.search(r'try again in (.+?)\.', full_err)
                retry_info  = f" Groq says: try again in **{retry_match.group(1)}**." if retry_match else ""
                # Check if it is TPD (daily) or TPM (per minute)
                if "per day" in full_err or "tokens per day" in full_err or "TPD" in full_err:
                    answer = f"⚠️ **Daily token limit reached** (Groq free tier: 100,000 tokens/day).{retry_info}\n\nTo keep using the app now, change your `.env`:\n```\nLLM_MODEL=llama3-8b-8192\n```\nThen restart Streamlit. The 8B model has a separate 500k/day quota."
                else:
                    answer = f"⚠️ **Rate limit hit** (too many requests per minute).{retry_info} Wait 20–30 seconds and try again."
            elif "context_length" in err or ("context" in err and "length" in err):
                answer = "⚠️ Question + context too long. Try a shorter question."
            elif "connect" in err or "connection" in err:
                answer = "⚠️ Cannot reach Groq API. Check your internet connection."
            elif "timeout" in err:
                answer = "⚠️ Request timed out. Try again."
            else:
                answer = f"⚠️ Error ({type(last_error).__name__}): {full_err}"

        self.memory.add_message("assistant", answer)

        sources = [{"topic":      d.metadata.get("topic", "unknown"),
                    "source":     d.metadata.get("source", "kb"),
                    "difficulty": d.metadata.get("difficulty", "unknown")}
                   for d in source_docs]

        return {"answer": answer, "sources": sources, "symbolic_hint": hint,
                "session_id": self.session_id, "context_docs": len(source_docs)}

    def clear_memory(self):
        self.memory.clear_history()

    def get_history(self):
        return self.memory.get_history(limit=50)


# ╔══════════════════════════════════════════════════════════════════════╗
# ║  OCR / IMAGE SCAN HELPER                                            ║
# ╚══════════════════════════════════════════════════════════════════════╝

def ocr_extract_text(image) -> str:
    try:
        from PIL import Image
        import PIL.ImageEnhance as enhance
        import pytesseract
        # Set tesseract binary path for common install locations
        for _tess_path in [
            "/opt/homebrew/bin/tesseract",   # macOS Apple Silicon (brew)
            "/usr/local/bin/tesseract",       # macOS Intel (brew)
            "/usr/bin/tesseract",             # Linux
        ]:
            if os.path.exists(_tess_path):
                pytesseract.pytesseract.tesseract_cmd = _tess_path
                break
        gray      = image.convert("L")
        contrast  = enhance.Contrast(gray).enhance(2.0)
        sharpened = enhance.Sharpness(contrast).enhance(2.0)
        text = pytesseract.image_to_string(sharpened, config='--psm 6').strip()
        text = ' '.join(text.replace('\n', ' ').split())
        return text
    except ImportError:
        return "ERROR_NO_PYTESSERACT"
    except Exception as e:
        logger.error(f"OCR error: {e}")
        return ""


# ╔══════════════════════════════════════════════════════════════════════╗
# ║  STEP 6 — STREAMLIT UI                                              ║
# ╚══════════════════════════════════════════════════════════════════════╝

def render_graph(expression: str, x_range: tuple = (-10, 10), title: str = ""):
    import streamlit as st
    try:
        import numpy as np
        import matplotlib.pyplot as plt
        _dark     = st.session_state.get("theme", "dark") == "dark"
        _fig_bg   = "#1e2235" if _dark else "#ffffff"
        _ax_bg    = "#0f1117" if _dark else "#f8fafc"
        _axis_col = "#4a5568" if _dark else "#cbd5e1"
        _tick_col = "#8892b0" if _dark else "#475569"
        _title_col= "#e8eaf6" if _dark else "#0f172a"
        _leg_face = "#1e2235" if _dark else "#ffffff"
        _leg_edge = "#2d3561" if _dark else "#e2e8f0"
        _leg_lbl  = "#e8eaf6" if _dark else "#0f172a"
        plt.style.use("dark_background" if _dark else "default")
        fig, ax = plt.subplots(figsize=(8, 5))
        fig.patch.set_facecolor(_fig_bg)
        ax.set_facecolor(_ax_bg)
        x = np.linspace(x_range[0], x_range[1], 1000)
        ns = {"__builtins__": {}, "x": x, "np": np,
              "sin": np.sin, "cos": np.cos, "tan": np.tan, "exp": np.exp,
              "log": np.log, "sqrt": np.sqrt, "abs": np.abs,
              "pi": np.pi, "e": np.e,
              "arcsin": np.arcsin, "arccos": np.arccos, "arctan": np.arctan}
        colors = ["#4f8ef7", "#4ecca3", "#f5c842", "#ff6b6b", "#c792ea"]
        for i, expr in enumerate(expression.split(",")[:5]):
            try:
                y = eval(re.sub(r'\^', '**', expr.strip()), ns)
                y = np.where(np.abs(y) > 1e10, np.nan, y)
                ax.plot(x, y, color=colors[i % len(colors)], linewidth=2.2,
                        label=f"y = {expr.strip()}", alpha=0.9)
            except Exception:
                st.warning(f"Could not plot: {expr.strip()}")
        ax.axhline(0, color=_axis_col, linewidth=0.8, alpha=0.7)
        ax.axvline(0, color=_axis_col, linewidth=0.8, alpha=0.7)
        ax.grid(True, alpha=0.15, color=_axis_col, linestyle="--")
        for spine in ax.spines.values():
            spine.set_color(_leg_edge)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.tick_params(colors=_tick_col)
        ax.set_xlabel("x", color=_tick_col, fontsize=11)
        ax.set_ylabel("y", color=_tick_col, fontsize=11)
        if title:
            ax.set_title(title, color=_title_col, fontsize=13, pad=15)
        if "," in expression:
            ax.legend(facecolor=_leg_face, edgecolor=_leg_edge,
                      labelcolor=_leg_lbl, fontsize=9)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)
    except Exception as e:
        st.error(f"Graph error: {e}")


def run_streamlit_app():
    import streamlit as st

    st.set_page_config(page_title="Advanced Mathematics Assistant",
                       page_icon="∫", layout="wide")

    # ── Theme: dark (default) or light ────────────────────────────────
    if "theme" not in st.session_state:
        st.session_state.theme = "dark"

    dark = st.session_state.theme == "dark"
    theme_vars = """
    :root {
        --bg:       #080c14;
        --bg2:      #0d1220;
        --card:     #111827;
        --card2:    #161f30;
        --blue:     #3b82f6;
        --blue2:    #60a5fa;
        --cyan:     #22d3ee;
        --green:    #10b981;
        --gold:     #f59e0b;
        --purple:   #8b5cf6;
        --tx:       #f1f5f9;
        --tx2:      #94a3b8;
        --tx3:      #475569;
        --border:   #1e293b;
        --border2:  #243044;
        --glow:     rgba(59,130,246,0.15);
    }""" if dark else """
    :root {
        --bg:       #f8fafc;
        --bg2:      #f1f5f9;
        --card:     #ffffff;
        --card2:    #f8fafc;
        --blue:     #2563eb;
        --blue2:    #1d4ed8;
        --cyan:     #0891b2;
        --green:    #059669;
        --gold:     #d97706;
        --purple:   #7c3aed;
        --tx:       #0f172a;
        --tx2:      #475569;
        --tx3:      #94a3b8;
        --border:   #e2e8f0;
        --border2:  #cbd5e1;
        --glow:     rgba(37,99,235,0.1);
    }"""

    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:wght@400;500&family=DM+Sans:wght@300;400;500;600&display=swap');
    {theme_vars}

    /* ── Base ── */
    .stApp {{ background-color: var(--bg) !important; color: var(--tx) !important; font-family: 'DM Sans', sans-serif; }}
    .main .block-container {{ padding-top: 1.5rem !important; max-width: 900px; }}
    section[data-testid="stSidebar"] {{ background: var(--bg2) !important; border-right: 1px solid var(--border) !important; }}
    section[data-testid="stSidebar"] .block-container {{ padding-top: 1.5rem !important; }}

    /* ── Light mode global text fixes ── */
    .stMarkdown p, .stMarkdown li, .stMarkdown span,
    .stMarkdown strong, .stMarkdown em,
    [data-testid="stMarkdownContainer"] p,
    [data-testid="stMarkdownContainer"] li,
    [data-testid="stMarkdownContainer"] span,
    [data-testid="stMarkdownContainer"] strong,
    [data-testid="stMarkdownContainer"] em {{
        color: var(--tx) !important;
    }}

    /* ── Hero Header ── */
    .hero-wrap {{
        text-align: center;
        padding: 2.5rem 1rem 1.5rem;
        position: relative;
    }}
    .hero-badge {{
        display: inline-block;
        font-family: 'DM Mono', monospace;
        font-size: 0.68rem;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        color: var(--cyan);
        background: rgba(34,211,238,0.12);
        border: 1px solid rgba(34,211,238,0.35);
        padding: 4px 14px;
        border-radius: 100px;
        margin-bottom: 1rem;
    }}
    .hero-title {{
        font-family: 'Syne', sans-serif;
        font-size: 2.6rem;
        font-weight: 800;
        letter-spacing: -0.03em;
        background: {'linear-gradient(135deg, #f1f5f9 0%, #60a5fa 50%, #22d3ee 100%)' if dark else 'linear-gradient(135deg, #0f172a 0%, #2563eb 50%, #0891b2 100%)'};
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 0 0 0.5rem;
        line-height: 1.15;
    }}
    .hero-sub {{
        font-size: 1rem;
        color: var(--tx2);
        font-weight: 300;
        letter-spacing: 0.01em;
        margin-bottom: 0.3rem;
    }}
    .hero-stats {{
        display: flex;
        justify-content: center;
        gap: 2rem;
        margin-top: 1.2rem;
        padding-top: 1.2rem;
        border-top: 1px solid var(--border);
    }}
    .stat-item {{ text-align: center; }}
    .stat-num {{
        font-family: 'Syne', sans-serif;
        font-size: 1.3rem;
        font-weight: 700;
        color: var(--blue2);
    }}
    .stat-label {{
        font-size: 0.7rem;
        color: var(--tx3);
        text-transform: uppercase;
        letter-spacing: 0.1em;
        font-family: 'DM Mono', monospace;
    }}

    /* ── Sidebar ── */
    .sidebar-logo {{
        font-family: 'Syne', sans-serif;
        font-size: 1.3rem;
        font-weight: 800;
        color: var(--tx);
        letter-spacing: -0.02em;
        display: flex;
        align-items: center;
        gap: 8px;
        margin-bottom: 0.2rem;
    }}
    .sidebar-logo span {{ color: var(--cyan); }}
    .sidebar-section {{
        font-family: 'DM Mono', monospace;
        font-size: 0.62rem;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        color: var(--tx3);
        margin: 1.2rem 0 0.6rem;
        padding-bottom: 0.4rem;
        border-bottom: 1px solid var(--border);
    }}
    .status-pill {{
        display: inline-flex;
        align-items: center;
        gap: 6px;
        font-size: 0.75rem;
        font-family: 'DM Mono', monospace;
        padding: 5px 12px;
        border-radius: 100px;
        width: 100%;
        margin-bottom: 0.5rem;
    }}
    .status-ok  {{ background: rgba(16,185,129,0.12); color: #059669; border: 1px solid rgba(16,185,129,0.35); }}
    .status-err {{ background: rgba(239,68,68,0.12);  color: #dc2626; border: 1px solid rgba(239,68,68,0.35); }}
    .dot {{ width: 6px; height: 6px; border-radius: 50%; background: currentColor; display: inline-block; }}
    .dot-pulse {{ animation: pulse 1.5s infinite; }}
    @keyframes pulse {{ 0%,100%{{opacity:1}} 50%{{opacity:0.4}} }}

    /* ── Chat Messages ── */
    .msg-user {{
        background: var(--card2);
        border: 1px solid var(--border2);
        border-left: 3px solid var(--blue);
        padding: 1rem 1.2rem;
        border-radius: 4px 16px 16px 16px;
        margin: 0.8rem 0;
        font-size: 0.95rem;
        line-height: 1.6;
        color: var(--tx);
    }}
    .msg-user-name {{
        font-family: 'DM Mono', monospace;
        font-size: 0.65rem;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        color: var(--blue2);
        margin-bottom: 0.4rem;
    }}
    .msg-ai-label {{
        display: flex;
        align-items: center;
        gap: 8px;
        margin: 1.5rem 0 0.5rem;
    }}
    .msg-ai-line {{
        flex: 1;
        height: 1px;
        background: linear-gradient(90deg, var(--green), transparent);
    }}
    .msg-ai-tag {{
        font-family: 'DM Mono', monospace;
        font-size: 0.62rem;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        color: var(--green);
    }}

    /* ── Topic Tags ── */
    .tag {{
        display: inline-block;
        background: rgba(59,130,246,0.12);
        color: var(--blue2);
        font-size: 0.65rem;
        font-family: 'DM Mono', monospace;
        padding: 3px 10px;
        border-radius: 100px;
        margin: 2px 3px;
        border: 1px solid rgba(59,130,246,0.35);
        letter-spacing: 0.05em;
    }}

    /* ── Input Area ── */
    .input-wrap {{
        background: var(--card);
        border: 1px solid var(--border2);
        border-radius: 16px;
        padding: 1rem 1.2rem 0.8rem;
        margin-top: 1rem;
        box-shadow: 0 0 40px rgba(59,130,246,0.05);
    }}
    .input-label {{
        font-family: 'DM Mono', monospace;
        font-size: 0.62rem;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        color: var(--tx3);
        margin-bottom: 0.5rem;
    }}

    /* ── Welcome Screen ── */
    .welcome-wrap {{
        text-align: center;
        padding: 3rem 1.5rem;
    }}
    .welcome-symbols {{
        font-size: 2.2rem;
        letter-spacing: 0.5rem;
        margin-bottom: 1.5rem;
        opacity: 0.6;
    }}
    .welcome-title {{
        font-family: 'Syne', sans-serif;
        font-size: 1.5rem;
        font-weight: 700;
        color: var(--tx);
        margin-bottom: 0.5rem;
    }}
    .welcome-sub {{
        color: var(--tx2);
        font-size: 0.9rem;
        line-height: 1.7;
        max-width: 500px;
        margin: 0 auto 1.5rem;
    }}
    .feature-grid {{
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 0.8rem;
        max-width: 500px;
        margin: 0 auto;
    }}
    .feature-card {{
        background: var(--card);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 0.9rem 1rem;
        text-align: left;
    }}
    .feature-icon {{ font-size: 1.3rem; margin-bottom: 0.3rem; }}
    .feature-title {{
        font-family: 'Syne', sans-serif;
        font-size: 0.8rem;
        font-weight: 700;
        color: var(--tx);
        margin-bottom: 0.2rem;
    }}
    .feature-desc {{ font-size: 0.72rem; color: var(--tx2); line-height: 1.4; }}

    /* ── Buttons ── */
    .stButton > button {{
        background: linear-gradient(135deg, #1d4ed8, #2563eb) !important;
        color: #fff !important;
        border: 1px solid rgba(96,165,250,0.3) !important;
        border-radius: 10px !important;
        font-family: 'DM Sans', sans-serif !important;
        font-weight: 500 !important;
        font-size: 0.85rem !important;
        letter-spacing: 0.01em !important;
        transition: all 0.2s !important;
        padding: 0.45rem 1rem !important;
    }}
    .stButton > button:hover {{
        background: linear-gradient(135deg, #2563eb, #3b82f6) !important;
        border-color: rgba(96,165,250,0.6) !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 20px rgba(59,130,246,0.3) !important;
    }}
    /* ── Sidebar buttons (Quick Examples, Plot, Compute etc) — ORIGINAL style ── */
    .stButton > button[kind="secondary"],
    [data-testid="baseButton-secondary"] {{
        background: var(--card2) !important;
        border: 1px solid var(--border2) !important;
        color: var(--tx2) !important;
    }}
    .stButton > button[kind="secondary"]:hover,
    [data-testid="baseButton-secondary"]:hover {{
        background: var(--border2) !important;
        color: var(--tx) !important;
    }}

    /* ── 4 specific buttons: 👍 👎 ✏️ Edit + theme toggle ── */
    .main [data-testid="baseButton-secondary"] {{
        background: {'#2d3748' if dark else 'transparent'} !important;
        border: 1px solid {'#4a5568' if dark else '#94a3b8'} !important;
        color: {'#f1f5f9' if dark else '#1e293b'} !important;
    }}
    .main [data-testid="baseButton-secondary"]:hover {{
        background: {'#4a5568' if dark else '#e2e8f0'} !important;
        border-color: {'#60a5fa' if dark else '#2563eb'} !important;
        color: {'#60a5fa' if dark else '#1e293b'} !important;
    }}
    section[data-testid="stSidebar"] [data-testid="column"] [data-testid="baseButton-secondary"] {{
        background: {'#2d3748' if dark else 'transparent'} !important;
        border: 1px solid {'#4a5568' if dark else '#94a3b8'} !important;
        color: {'#f1f5f9' if dark else '#1e293b'} !important;
    }}
    section[data-testid="stSidebar"] [data-testid="column"] [data-testid="baseButton-secondary"]:hover {{
        background: {'#4a5568' if dark else '#e2e8f0'} !important;
        border-color: {'#60a5fa' if dark else '#2563eb'} !important;
        color: {'#60a5fa' if dark else '#1e293b'} !important;
    }}
    /* ── Toast message text ── */
    [data-testid="stToast"] {{
        background: {'#1e293b' if dark else '#ffffff'} !important;
        color: {'#ffffff' if dark else '#0f172a'} !important;
    }}
    [data-testid="stToast"] p,
    [data-testid="stToast"] span,
    [data-testid="stToast"] div {{
        color: {'#ffffff' if dark else '#0f172a'} !important;
    }}
    /* ── Tooltip popup text (help= on buttons) ── */
    div[data-testid="stTooltipContent"],
    div[data-testid="stTooltipContent"] p,
    div[data-testid="stTooltipContent"] span,
    [role="tooltip"],
    [role="tooltip"] p {{
        background: #1e293b !important;
        color: #f1f5f9 !important;
        border: 1px solid #334155 !important;
        border-radius: 6px !important;
        font-size: 0.75rem !important;
    }}


    /* ── Inputs ── */
    .stTextArea textarea, .stTextInput input {{
        background: var(--bg2) !important;
        color: var(--tx) !important;
        caret-color: var(--blue) !important;
        border: 1px solid var(--border2) !important;
        border-radius: 10px !important;
        font-family: 'DM Mono', monospace !important;
        font-size: 0.88rem !important;
    }}
    .stTextArea textarea::placeholder, .stTextInput input::placeholder {{
        color: var(--tx3) !important;
        opacity: 1 !important;
    }}
    .stTextArea textarea:focus, .stTextInput input:focus {{
        border-color: var(--blue) !important;
        box-shadow: 0 0 0 2px rgba(59,130,246,0.15) !important;
    }}
    .stSelectbox > div > div {{
        background: var(--bg2) !important;
        border: 1px solid var(--border2) !important;
        border-radius: 10px !important;
        color: var(--tx) !important;
    }}
    /* ── File Uploader & Browse button ── */
    .stFileUploader {{
        background: var(--card) !important;
        border: 1px dashed var(--border2) !important;
        border-radius: 12px !important;
    }}
    [data-testid="stFileUploadDropzone"] button,
    .stFileUploader button,
    [data-testid="baseButton-secondary"][kind="secondary"] {{
        background: var(--card2) !important;
        color: var(--tx) !important;
        border: 1px solid var(--border2) !important;
        border-radius: 8px !important;
    }}
    [data-testid="stFileUploadDropzone"] button:hover,
    .stFileUploader button:hover {{
        background: var(--border2) !important;
        color: var(--tx) !important;
        border-color: var(--blue) !important;
    }}
    [data-testid="stFileUploadDropzone"] span,
    [data-testid="stFileUploadDropzone"] p,
    [data-testid="stFileUploadDropzone"] small,
    .stFileUploader span,
    .stFileUploader p,
    .stFileUploader small {{
        color: var(--tx2) !important;
    }}

    /* ── Dividers & misc ── */
    hr {{ border-color: var(--border) !important; opacity: 0.5 !important; }}
    .stCaption {{ color: var(--tx3) !important; font-family: 'DM Mono', monospace !important; font-size: 0.7rem !important; }}
    .stExpander {{ background: var(--card) !important; border: 1px solid var(--border) !important; border-radius: 10px !important; }}
    .stAlert {{ border-radius: 10px !important; }}
    .stMetric {{ background: var(--card) !important; border: 1px solid var(--border) !important; border-radius: 10px !important; padding: 0.6rem !important; }}
    .stMetric label, [data-testid="stMetricLabel"], [data-testid="stMetricLabel"] p {{
        color: var(--tx3) !important; font-family: 'DM Mono', monospace !important;
        font-size: 0.65rem !important; text-transform: uppercase !important; letter-spacing: 0.08em !important;
    }}
    [data-testid="stMetricValue"], [data-testid="stMetricValue"] > div,
    .stMetric [data-testid="metric-container"] > div:last-child {{
        color: var(--blue2) !important; font-family: 'Syne', sans-serif !important;
        font-size: 1.4rem !important; font-weight: 700 !important;
    }}

    /* ── Scrollbar ── */
    ::-webkit-scrollbar {{ width: 5px; }}
    ::-webkit-scrollbar-track {{ background: var(--bg); }}
    ::-webkit-scrollbar-thumb {{ background: var(--border2); border-radius: 10px; }}

    /* ── Radio ── */
    .stRadio > div {{ gap: 0.4rem !important; }}
    .stRadio > div label {{ padding: 4px 8px; border-radius: 8px; cursor: pointer; }}
    .stRadio > div label p {{ font-size: 0.82rem !important; color: var(--tx2) !important; font-family: 'DM Sans', sans-serif !important; }}

    /* ════════════════════════════════════════════════════════
       FIX 1 — Expander label & content text in BOTH themes
       ════════════════════════════════════════════════════════ */
    /* Expander toggle/summary text */
    .stExpander details summary,
    .stExpander details summary p,
    .stExpander details summary span,
    [data-testid="stExpander"] summary,
    [data-testid="stExpander"] summary p {{
        color: var(--tx) !important;
        background: var(--card) !important;
    }}
    /* Expander body */
    .stExpander details,
    [data-testid="stExpander"] details,
    [data-testid="stExpanderDetails"],
    .stExpander details > div {{
        background: var(--card) !important;
        color: var(--tx) !important;
    }}
    /* Text inside expander */
    .stExpander p,
    .stExpander li,
    .stExpander span,
    [data-testid="stExpanderDetails"] p,
    [data-testid="stExpanderDetails"] li {{
        color: var(--tx) !important;
    }}

    /* ════════════════════════════════════════════════════════
       FIX 2 — st.code inside expander (copy text block)
       ════════════════════════════════════════════════════════ */
    .stExpander pre,
    .stExpander pre code,
    [data-testid="stExpanderDetails"] pre,
    [data-testid="stExpanderDetails"] pre code,
    [data-testid="stCode"] pre,
    [data-testid="stCode"] code {{
        background: var(--bg2) !important;
        color: var(--tx) !important;
        border: 1px solid var(--border2) !important;
        border-radius: 8px !important;
        font-family: 'DM Mono', monospace !important;
        font-size: 0.82rem !important;
        line-height: 1.75 !important;
        white-space: pre-wrap !important;
        word-break: break-word !important;
    }}
    /* Copy button on st.code */
    [data-testid="stCode"] button {{
        background: var(--card2) !important;
        color: var(--tx2) !important;
        border: 1px solid var(--border2) !important;
        border-radius: 6px !important;
    }}
    [data-testid="stCode"] button:hover {{
        background: var(--border2) !important;
        color: var(--tx) !important;
    }}

    /* ════════════════════════════════════════════════════════
       FIX 3 — st.warning / st.error / st.info visibility
       Always show proper contrast regardless of theme
       ════════════════════════════════════════════════════════ */
    [data-testid="stAlert"] {{
        border-radius: 10px !important;
    }}
    /* Warning — amber */
    [data-testid="stAlert"][data-baseweb="notification"][kind="warning"],
    div[data-testid="stAlert"].st-ae {{
        background: rgba(245,158,11,0.12) !important;
        border: 1px solid rgba(245,158,11,0.5) !important;
    }}
    [data-testid="stAlert"] p,
    [data-testid="stAlert"] div,
    [data-testid="stAlert"] span,
    div.stAlert p {{
        color: var(--tx) !important;
        opacity: 1 !important;
    }}
    /* Force warning icon & text colour in light mode */
    .element-container .stAlert > div {{
        color: var(--tx) !important;
    }}
    </style>
    """, unsafe_allow_html=True)

    for k, v in [("session_id", str(uuid.uuid4())[:8]), ("messages", []),
                 ("engine", None), ("kb_ready", False),
                 ("query_count", 0), ("pending", None)]:
        if k not in st.session_state:
            st.session_state[k] = v

    with st.sidebar:
        # ── Logo + Theme Toggle ───────────────────────────────────────
        logo_col, theme_col = st.columns([3, 1])
        with logo_col:
            st.markdown("""
            <div class="sidebar-logo">
                <span>∫</span> MathAI
            </div>
            <div style="font-family:'DM Mono',monospace;font-size:0.65rem;color:var(--tx2);margin-bottom:0.5rem;">
                Advanced Mathematics Assistant
            </div>
            """, unsafe_allow_html=True)
        with theme_col:
            st.markdown("<br>", unsafe_allow_html=True)
            theme_icon = "☀️" if dark else "🌙"
            if st.button(theme_icon, key="theme_toggle", help="Toggle dark/light mode"):
                st.session_state.theme = "light" if dark else "dark"
                st.rerun()

        if GROQ_API_KEY and GROQ_API_KEY != "your_groq_api_key_here":
            st.markdown(f'<div class="status-pill status-ok"><span class="dot dot-pulse"></span> Groq LLM · {LLM_MODEL.split("-")[0].upper()}</div>', unsafe_allow_html=True)
            st.markdown('<div style="font-family:DM Mono,monospace;font-size:0.6rem;color:var(--tx3);margin-top:-0.3rem;padding-left:2px;">Free tier: 30 req/min · auto-retry on</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="status-pill status-err"><span class="dot"></span> No API Key — check .env</div>', unsafe_allow_html=True)

        st.markdown('<div class="sidebar-section">Quick Examples</div>', unsafe_allow_html=True)
        examples = {
            "🔢 Quadratic":   "Solve 2x² + 5x - 3 = 0 step by step",
            "📐 Derivatives": "Find the derivative of f(x) = x³sin(x)",
            "🔗 Integration": "Evaluate the integral of x²e^x dx",
            "🎯 Eigenvalues": "Find eigenvalues of the matrix [[2,1],[1,2]]",
            "📊 Statistics":  "Explain the Central Limit Theorem with an example",
            "📈 Series":      "Does the series sum(1/n²) converge? Find its sum",
            "🔺 Vectors":     "Find the angle between vectors (1,2,3) and (4,5,6)",
            "🧮 Probability": "Explain Bayes theorem with a medical test example",
        }
        for label, question in examples.items():
            if st.button(label, key=f"ex_{label}", use_container_width=True):
                st.session_state.pending = question
                st.rerun()

        st.markdown('<div class="sidebar-section">Graph Plotter</div>', unsafe_allow_html=True)
        gexpr  = st.text_input("Function(s):", placeholder="x**2, sin(x)")
        grange = st.slider("x range", -20, 20, (-10, 10))
        gtitle = st.text_input("Title:", placeholder="My Graph")
        if st.button("📊 Plot", use_container_width=True) and gexpr:
            render_graph(gexpr, grange, gtitle)

        st.markdown('<div class="sidebar-section">Symbolic Compute</div>', unsafe_allow_html=True)
        sym_in  = st.text_input("Expression:", placeholder="x**3 + 2*x")
        sym_act = st.selectbox("Action:", ["Differentiate", "Integrate", "Solve (=0)", "Simplify"])
        if st.button("⚡ Compute", use_container_width=True) and sym_in:
            sym = SymbolicMathEngine()
            result = (sym.differentiate(sym_in)        if sym_act == "Differentiate" else
                      sym.integrate(sym_in)             if sym_act == "Integrate"    else
                      sym.solve_equation(sym_in + "=0") if sym_act == "Solve (=0)"  else
                      sym.try_solve(sym_in))
            if result:
                st.success(result)
            else:
                st.warning("Could not compute symbolically")

        st.markdown('<div class="sidebar-section">Upload PDF</div>', unsafe_allow_html=True)
        uploaded_pdf = st.file_uploader(
            "Choose PDF file", type=["pdf"], label_visibility="collapsed")

        if uploaded_pdf is not None:
            pdf_hash = hashlib.md5(uploaded_pdf.getvalue()).hexdigest()

            # ── Only process once per unique uploaded file ─────────────
            if st.session_state.get("last_pdf_hash") != pdf_hash:
                st.session_state.last_pdf_hash     = pdf_hash
                st.session_state.pdf_status        = None
                st.session_state.pdf_detected_type = None

                # Use tempfile to avoid name collisions across concurrent sessions
                suffix = Path(uploaded_pdf.name).suffix or ".pdf"
                tmp_fd, tmp_path = tempfile.mkstemp(suffix=suffix)
                with os.fdopen(tmp_fd, "wb") as f2:
                    f2.write(uploaded_pdf.getvalue())

                with st.spinner("📖 Reading PDF..."):
                    try:
                        pdf_docs    = MathDataLoader().load_pdf(tmp_path)
                        all_text    = " ".join(d.page_content.lower() for d in pdf_docs)
                        total_words = len(all_text.split())

                        if not pdf_docs or total_words < 30:
                            st.session_state.pdf_status = "empty"
                        else:
                            # ── Strict math-only keywords (not in everyday English) ──
                            STRICT_MATH = [
                                "equation", "derivative", "integral", "differentiate",
                                "integrate", "calculus", "algebra", "trigonometry",
                                "polynomial", "quadratic", "eigenvalue", "determinant",
                                "theorem", "logarithm", "exponent", "coefficient",
                                "binomial", "permutation", "combination", "modular",
                                "arithmetic", "geometry", "probability", "variance",
                                "matrix", "gradient", "divergence", "laplace", "fourier",
                                "numerator", "denominator", "hypotenuse", "asymptote",
                                "parabola", "hyperbola", "ellipse", "congruent",
                                "factorize", "simplify", "differentiation", "integration",
                                "d/dx", "dy/dx", "f(x)", "g(x)", "ax²", "bx+c",
                                "∫", "∑", "∂", "√", "∞", "±", "²", "³",
                            ]
                            math_hits  = sum(1 for kw in STRICT_MATH if kw in all_text)
                            math_lines = len(re.findall(
                                r'\b\d+[\+\-\*/\^=]\d+\b|=\s*[\d\-]|\bx\s*=|\by\s*=', all_text))
                            is_math_pdf = (math_hits >= 4) or (math_hits >= 2 and math_lines >= 3)

                            if not is_math_pdf:
                                DOC_TYPES = {
                                    "📄 Resume / CV": [
                                        "experience", "skills", "education", "resume",
                                        "curriculum vitae", "employment", "linkedin",
                                        "references", "internship", "bachelor", "master",
                                        "gpa", "cgpa", "projects", "achievements",
                                        "objective", "career", "certification"],
                                    "📰 News / Article": [
                                        "published", "reporter", "journalist", "editor",
                                        "breaking news", "according to", "press release",
                                        "subscribe", "headline", "sources said"],
                                    "📖 Story / Novel / Essay": [
                                        "chapter", "once upon", "he said", "she said",
                                        "fiction", "narrative", "plot", "character",
                                        "dialogue", "protagonist", "author"],
                                    "🧾 Invoice / Receipt": [
                                        "invoice", "receipt", "total amount", "payment",
                                        "billing", "gst", "quantity", "order number",
                                        "due date", "subtotal", "discount", "vendor"],
                                    "⚖️ Legal Document": [
                                        "hereby", "clause", "agreement", "whereas",
                                        "plaintiff", "defendant", "jurisdiction",
                                        "contract", "liability", "terms and conditions"],
                                    "🍽️ Recipe / Food": [
                                        "ingredients", "tablespoon", "teaspoon", "bake",
                                        "recipe", "preheat", "oven", "serving", "cuisine",
                                        "cook", "boil", "fry", "garnish"],
                                    "💼 Business / Report": [
                                        "revenue", "profit", "quarterly", "stakeholder",
                                        "strategy", "market share", "fiscal", "kpi",
                                        "roi", "budget", "forecast", "annual report"],
                                    "🔬 Science (Non-Math)": [
                                        "biology", "chemistry", "organism", "cell",
                                        "molecule", "species", "evolution", "experiment",
                                        "hypothesis", "dna", "protein", "ecosystem"],
                                }
                                detected_type = "📁 Unknown document type"
                                best_score    = 0
                                for dtype, kws in DOC_TYPES.items():
                                    score = sum(1 for kw in kws if kw in all_text)
                                    if score > best_score:
                                        best_score    = score
                                        detected_type = dtype
                                if total_words < 100:
                                    detected_type = "🖼️ Scanned / Image-based PDF (no readable text)"

                                st.session_state.pdf_status        = "wrong"
                                st.session_state.pdf_detected_type = detected_type
                                st.session_state.pdf_math_hits     = math_hits
                            else:
                                clean  = MathDataPreprocessor().preprocess_documents(pdf_docs)
                                chunks = MathTextSplitter().split_documents(clean)
                                if st.session_state.engine and chunks:
                                    st.session_state.engine.vector_store.add_documents(chunks)
                                    st.session_state.pdf_status    = "ok"
                                    st.session_state.pdf_pages     = len(pdf_docs)
                                    st.session_state.pdf_math_hits = math_hits
                                else:
                                    st.session_state.pdf_status = "empty"

                    except Exception as e:
                        st.session_state.pdf_status = f"error:{e}"
                    finally:
                        if os.path.exists(tmp_path):
                            os.remove(tmp_path)

            # ── Show stored result (persists across all reruns) ─────────
            status = st.session_state.get("pdf_status")

            if status == "empty":
                st.markdown(f"""
                <div style="background:{'rgba(239,68,68,0.12)' if dark else '#fff1f2'};
                    border:1px solid {'rgba(239,68,68,0.45)' if dark else '#fca5a5'};
                    border-radius:10px;padding:0.9rem 1rem;margin:0.4rem 0;">
                    <div style="color:{'#f87171' if dark else '#dc2626'};font-weight:600;font-size:0.85rem;">
                        ❌ PDF is empty or unreadable
                    </div>
                    <div style="color:{'#fca5a5' if dark else '#991b1b'};font-size:0.75rem;margin-top:0.3rem;">
                        No text could be extracted. Try a different PDF.
                    </div>
                </div>""", unsafe_allow_html=True)

            elif status == "wrong":
                detected_type = st.session_state.get("pdf_detected_type", "📁 Unknown")
                math_hits     = st.session_state.get("pdf_math_hits", 0)
                st.markdown(f"""
                <div style="background:{'rgba(239,68,68,0.12)' if dark else '#fff1f2'};
                    border:1px solid {'rgba(239,68,68,0.45)' if dark else '#fca5a5'};
                    border-radius:10px;padding:0.9rem 1rem;margin:0.4rem 0;">
                    <div style="color:{'#f87171' if dark else '#dc2626'};font-weight:600;font-size:0.85rem;margin-bottom:0.4rem;">
                        ❌ Wrong PDF — Not a Math document
                    </div>
                    <div style="color:{'#fca5a5' if dark else '#991b1b'};font-size:0.78rem;line-height:1.8;">
                        <b>Detected as:</b> {detected_type}<br>
                        <b>Math keywords found:</b> {math_hits} (need at least 4)<br><br>
                        Please upload a <b>maths textbook, question paper, or class notes</b>.
                    </div>
                </div>""", unsafe_allow_html=True)

            elif status == "ok":
                pages     = st.session_state.get("pdf_pages", "?")
                math_hits = st.session_state.get("pdf_math_hits", 0)
                st.success(f"✅ Loaded {pages} page(s) · {math_hits} math keywords!")
                st.markdown("**Ask about this PDF:**")
                if st.button("📝 Solve all problems in this PDF", use_container_width=True, type="primary"):
                    st.session_state.pending = "Solve all the math problems from the uploaded PDF step by step"
                    st.rerun()
                if st.button("📋 Summarize this PDF", use_container_width=True):
                    st.session_state.pending = "Summarize the key math concepts from the uploaded PDF"
                    st.rerun()
                if st.button("❓ What topics are in this PDF?", use_container_width=True):
                    st.session_state.pending = "What math topics are covered in the uploaded PDF?"
                    st.rerun()

            elif status and str(status).startswith("error:"):
                st.error(f"PDF error: {str(status)[6:]}")


        st.markdown('<div class="sidebar-section">Scan Problem</div>', unsafe_allow_html=True)

        scan_method = st.radio(
            "Choose input:",
            ["📷 Use Camera", "🖼️ Upload Image"],
            horizontal=True,
            label_visibility="collapsed")

        scanned_image = None
        if scan_method == "📷 Use Camera":
            scanned_image = st.camera_input(
                "Point at math problem and capture", label_visibility="collapsed")
        else:
            scanned_image = st.file_uploader(
                "Upload photo of math problem",
                type=["png", "jpg", "jpeg", "webp"],
                label_visibility="collapsed",
                key="img_uploader")

        if scanned_image is not None:
            try:
                from PIL import Image as PILImage
                image = PILImage.open(scanned_image)
                st.image(image, caption="📸 Captured Image", use_container_width=True)

                img_hash = hashlib.md5(scanned_image.getvalue()).hexdigest()
                is_new_image = st.session_state.get("last_img_hash") != img_hash

                # ── Check pytesseract AND tesseract binary ──
                _tess_available = False
                try:
                    import pytesseract as _tess
                    import subprocess
                    # Try known binary paths first
                    for _tp in [
                        "/opt/homebrew/bin/tesseract",   # macOS Apple Silicon
                        "/usr/local/bin/tesseract",       # macOS Intel
                        "/usr/bin/tesseract",             # Linux / Streamlit Cloud
                        "/usr/local/share/tessdata/../../../bin/tesseract",
                    ]:
                        if os.path.exists(_tp):
                            _tess.pytesseract.tesseract_cmd = _tp
                            _tess_available = True
                            break
                    # Fallback: try running tesseract from PATH
                    if not _tess_available:
                        _r = subprocess.run(
                            ["tesseract", "--version"],
                            capture_output=True, timeout=5
                        )
                        if _r.returncode == 0:
                            _tess_available = True
                    # Final fallback: find tesseract using `which`
                    if not _tess_available:
                        _r = subprocess.run(
                            ["which", "tesseract"],
                            capture_output=True, timeout=5
                        )
                        if _r.returncode == 0:
                            _tp = _r.stdout.decode().strip()
                            if _tp:
                                _tess.pytesseract.tesseract_cmd = _tp
                                _tess_available = True
                except Exception:
                    _tess_available = False

                if not _tess_available:
                    # Show setup notice only once — collapse it after first view
                    _tess_warned = st.session_state.get("tess_warning_shown", False)
                    if not _tess_warned:
                        st.session_state.tess_warning_shown = True
                    with st.expander("⚙️ One-time setup: enable camera scan", expanded=not _tess_warned):
                        st.markdown(f"""
                        <div style="background:{'rgba(245,158,11,0.1)' if dark else '#fffbeb'};
                            border:1px solid {'rgba(245,158,11,0.4)' if dark else '#fcd34d'};
                            border-radius:8px;padding:0.8rem 1rem;margin-bottom:0.6rem;">
                            <div style="color:{'#fbbf24' if dark else '#b45309'};font-weight:600;font-size:0.85rem;margin-bottom:0.3rem;">
                                📷 OCR not installed — camera scan disabled
                            </div>
                            <div style="color:{'#fde68a' if dark else '#92400e'};font-size:0.75rem;line-height:1.75;">
                                To enable photo scanning, run <b>one</b> of these in your terminal and restart:
                            </div>
                        </div>""", unsafe_allow_html=True)
                        _tab_mac, _tab_linux, _tab_win = st.tabs(["🍎 macOS", "🐧 Linux", "🪟 Windows"])
                        with _tab_mac:
                            st.code("pip install pytesseract pillow\nbrew install tesseract", language="bash")
                        with _tab_linux:
                            st.code("pip install pytesseract pillow\nsudo apt install tesseract-ocr", language="bash")
                        with _tab_win:
                            st.code("pip install pytesseract pillow", language="bash")
                            st.markdown("<div style='font-size:0.75rem;color:var(--tx2);margin-top:0.3rem;'>Then download the Tesseract installer:<br><a href='https://github.com/UB-Mannheim/tesseract/wiki' target='_blank'>github.com/UB-Mannheim/tesseract/wiki</a></div>", unsafe_allow_html=True)
                        st.caption("After installing, restart Streamlit and camera scan will work automatically.")
                    st.markdown("<div style='color:var(--tx2);font-size:0.82rem;margin-top:0.4rem;'>✏️ Type your math problem manually instead:</div>", unsafe_allow_html=True)
                    manual_ocr = st.text_input(
                        "Type problem here:",
                        placeholder="e.g. Solve x² + 5x + 6 = 0",
                        key=f"manual_ocr_{img_hash}",
                        label_visibility="collapsed")
                    if st.button("🧮 Solve Manually", key=f"manual_ocr_solve_{img_hash}", use_container_width=True, type="primary"):
                        if manual_ocr.strip():
                            st.session_state.pending = f"Solve this math problem step by step: {manual_ocr}"
                            st.rerun()
                        else:
                            st.error("Please type a problem first!")

                else:
                    # pytesseract is available — run OCR now
                    if is_new_image:
                        with st.spinner("🔍 Reading math problem from image..."):
                            extracted = ocr_extract_text(image)
                        st.session_state.last_img_hash    = img_hash
                        st.session_state.last_ocr_text    = extracted
                        st.session_state.ocr_auto_solved  = False
                    else:
                        extracted = st.session_state.get("last_ocr_text", "")

                    if extracted and extracted.strip():
                        # validate OCR text is actually math before accepting
                        txt_low = extracted.lower()
                        MATH_OCR_SIGNALS = [
                            # operators & symbols
                            "=", "+", "-", "*", "/", "^", "²", "³", "√",
                            "∫", "∑", "∂", "±", "∞", "π",
                            # keywords
                            "solve", "find", "equation", "integral", "derivative",
                            "differentiate", "integrate", "matrix", "vector",
                            "quadratic", "polynomial", "theorem", "proof",
                            "calculate", "simplify", "factorize", "evaluate",
                            "sin", "cos", "tan", "log", "ln",
                            "f(x)", "g(x)", "d/dx", "dy/dx", "lim",
                            "dx", "dy", "x²", "x^2", "ax", "bx",
                        ]
                        # Count signals present in extracted text
                        ocr_math_hits = sum(1 for s in MATH_OCR_SIGNALS if s in txt_low or s in extracted)
                        # Also check: has at least one digit near an operator
                        has_math_pattern = bool(re.search(
                            r'\d[\+\-\*/=^]|[\+\-\*/=^]\d|\bx\b|\by\b', extracted))
                        is_math_image = ocr_math_hits >= 2 or has_math_pattern

                        if is_math_image:
                            st.success("✅ Math problem detected!")
                            st.info(f"📝 **Detected:** {extracted}")
                            st.markdown("<small style='color:var(--tx2)'>✏️ Edit if needed:</small>",
                                        unsafe_allow_html=True)
                            edited = st.text_input(
                                "Edit:", value=extracted,
                                key=f"edit_{img_hash}",
                                label_visibility="collapsed")
                            b1, b2 = st.columns(2)
                            with b1:
                                if st.button("🧮 Solve", key=f"solve_{img_hash}", use_container_width=True, type="primary"):
                                    st.session_state.pending = f"Solve this math problem step by step: {edited}"
                                    st.session_state.ocr_auto_solved = True
                                    st.rerun()
                                if st.button("📋 Summarize", key=f"sum_{img_hash}", use_container_width=True):
                                    st.session_state.pending = f"Summarize and explain this math problem: {edited}"
                                    st.session_state.ocr_auto_solved = True
                                    st.rerun()
                            with b2:
                                if st.button("💡 Hint", key=f"hint_{img_hash}", use_container_width=True):
                                    st.session_state.pending = f"Give me a hint to solve: {edited}"
                                    st.session_state.ocr_auto_solved = True
                                    st.rerun()
                                if st.button("📊 Similar", key=f"sim_{img_hash}", use_container_width=True):
                                    st.session_state.pending = f"Show similar example problems like: {edited}"
                                    st.session_state.ocr_auto_solved = True
                                    st.rerun()
                            if is_new_image and not st.session_state.get("ocr_auto_solved", False):
                                st.session_state.ocr_auto_solved = True
                                st.session_state.pending = f"Solve this math problem step by step: {extracted}"
                                st.rerun()

                        else:
                            # OCR found text but it's NOT math (photo, selfie, food, etc.)
                            st.markdown(f"""
                            <div style="background:{'rgba(239,68,68,0.12)' if dark else '#fff1f2'};
                                border:1px solid {'rgba(239,68,68,0.45)' if dark else '#fca5a5'};
                                border-radius:10px;padding:0.9rem 1rem;margin:0.5rem 0;">
                                <div style="color:{'#f87171' if dark else '#dc2626'};font-weight:600;font-size:0.88rem;margin-bottom:0.35rem;">
                                    ❌ This is not a Math image
                                </div>
                                <div style="color:{'#fca5a5' if dark else '#991b1b'};font-size:0.78rem;line-height:1.65;">
                                    Text was found but no math content detected.<br>
                                    <b>Math signals found:</b> {ocr_math_hits} (need at least 2)<br><br>
                                    Please upload an image of a <b>math problem, equation, or question paper</b>.
                                </div>
                            </div>""", unsafe_allow_html=True)
                            st.markdown(f"<div style='color:var(--tx2);font-size:0.82rem;margin-top:0.4rem;'>✏️ Or type your problem manually:</div>", unsafe_allow_html=True)
                            manual = st.text_input(
                                "Type problem here:",
                                placeholder="e.g. Solve x² + 5x + 6 = 0",
                                key=f"manual_{img_hash}",
                                label_visibility="collapsed")
                            if st.button("🧮 Solve Manually", key=f"manual_solve_{img_hash}", use_container_width=True, type="primary"):
                                if manual.strip():
                                    st.session_state.pending = f"Solve this math problem step by step: {manual}"
                                    st.rerun()
                                else:
                                    st.error("Please type a problem first!")

                    else:
                        # OCR found nothing at all (blank image, photo with no text)
                        st.markdown(f"""
                        <div style="background:{'rgba(239,68,68,0.12)' if dark else '#fff1f2'};
                            border:1px solid {'rgba(239,68,68,0.45)' if dark else '#fca5a5'};
                            border-radius:10px;padding:0.9rem 1rem;margin:0.5rem 0;">
                            <div style="color:{'#f87171' if dark else '#dc2626'};font-weight:600;font-size:0.88rem;margin-bottom:0.35rem;">
                                ❌ No text found in this image
                            </div>
                            <div style="color:{'#fca5a5' if dark else '#991b1b'};font-size:0.78rem;line-height:1.65;">
                                This looks like a photo or image without any readable text.<br><br>
                                • Make sure the image contains a <b>written or printed math problem</b><br>
                                • Ensure good lighting and focus<br>
                                • Avoid selfies, landscapes, or non-math images
                            </div>
                        </div>""", unsafe_allow_html=True)
                        st.markdown(f"<div style='color:var(--tx2);font-size:0.82rem;margin-top:0.4rem;'>✏️ Type your problem manually instead:</div>", unsafe_allow_html=True)
                        manual2 = st.text_input(
                            "Type problem here:",
                            placeholder="e.g. Solve x² + 5x + 6 = 0",
                            key=f"manual2_{img_hash}",
                            label_visibility="collapsed")
                        if st.button("🧮 Solve Manually", key=f"manual_solve2_{img_hash}", use_container_width=True, type="primary"):
                            if manual2.strip():
                                st.session_state.pending = f"Solve this math problem step by step: {manual2}"
                                st.rerun()
                            else:
                                st.error("Please type a problem first!")

            except ImportError:
                st.error("❌ Pillow not installed. Run: pip install pillow")
            except Exception as e:
                st.error(f"Scan error: {e}")
                st.info("💡 Try uploading a clearer image or type your problem manually.")

        st.markdown('<div class="sidebar-section">Session</div>', unsafe_allow_html=True)
        _cb  = "#111827" if dark else "#ffffff"
        _cbr = "#1e293b" if dark else "#e2e8f0"
        _lc  = "#475569" if dark else "#94a3b8"
        _nc  = "#60a5fa" if dark else "#2563eb"
        st.markdown(f"""
        <div style="display:flex;gap:0.5rem;margin-bottom:0.6rem;">
            <div style="flex:1;background:{_cb};border:1px solid {_cbr};border-radius:10px;padding:0.55rem 0.7rem;">
                <div style="font-family:'DM Mono',monospace;font-size:0.6rem;text-transform:uppercase;letter-spacing:0.08em;color:{_lc};margin-bottom:0.2rem;">Queries</div>
                <div style="font-family:'Syne',sans-serif;font-size:1.35rem;font-weight:700;color:{_nc};">{st.session_state.query_count}</div>
            </div>
            <div style="flex:1;background:{_cb};border:1px solid {_cbr};border-radius:10px;padding:0.55rem 0.7rem;">
                <div style="font-family:'DM Mono',monospace;font-size:0.6rem;text-transform:uppercase;letter-spacing:0.08em;color:{_lc};margin-bottom:0.2rem;">Messages</div>
                <div style="font-family:'Syne',sans-serif;font-size:1.35rem;font-weight:700;color:{_nc};">{len(st.session_state.messages)}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🗑️ Clear Chat", use_container_width=True):
            st.session_state.messages       = []
            st.session_state.query_count    = 0
            st.session_state.last_user_input = ""
            if st.session_state.engine:
                st.session_state.engine.clear_memory()
            st.rerun()

    st.markdown("""
    <div class="hero-wrap">
        <div class="hero-badge">⚡ Powered by LLaMA 3.3 · Groq · RAG</div>
        <h1 class="hero-title">Advanced Mathematics<br>Assistant</h1>
        <p class="hero-sub">Step-by-step AI solutions · Symbolic computation · Graph plotting</p>
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.engine is None:
        _init_placeholder = st.empty()
        _init_placeholder.info("⚡ Starting up… loading AI model (first run takes ~10 seconds, then it's instant)")
        try:
            store = build_pipeline()
            engine = MathAIEngine(vector_store=store, session_id=st.session_state.session_id)
            st.session_state.engine   = engine
            st.session_state.kb_ready = True
            _init_placeholder.empty()
        except Exception as e:
            _init_placeholder.empty()
            st.error(f"Init error: {e}")
            st.info("Make sure GROQ_API_KEY is set in .env and all packages are installed.")
            st.stop()

    if st.session_state.kb_ready and st.session_state.engine:
        doc_count = (st.session_state.engine.vector_store.get_document_count()
                     if st.session_state.engine.vector_store else 0)
        st.markdown(f"""
        <div style="text-align:center;margin-bottom:0.5rem;">
            <span style="font-family:'DM Mono',monospace;font-size:0.65rem;color:var(--tx2);letter-spacing:0.08em;">
                📚 {doc_count} CHUNKS &nbsp;·&nbsp; {LLM_MODEL} &nbsp;·&nbsp; SESSION {st.session_state.session_id.upper()}
            </span>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    if not st.session_state.messages:
        st.markdown("""
        <div class="welcome-wrap">
            <div class="welcome-symbols">∫ ∑ ∂ π</div>
            <div class="welcome-title">What would you like to solve?</div>
            <p class="welcome-sub">
                Ask any math question and get clear, step-by-step solutions.<br>
                From basic algebra to advanced calculus — I've got you covered.
            </p>
            <div class="feature-grid">
                <div class="feature-card">
                    <div class="feature-icon">🧮</div>
                    <div class="feature-title">Step-by-Step Solutions</div>
                    <div class="feature-desc">Clear explanations for every problem, just like a teacher</div>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">📷</div>
                    <div class="feature-title">Camera Scan</div>
                    <div class="feature-desc">Snap a photo of any handwritten problem — auto-solves instantly</div>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">📄</div>
                    <div class="feature-title">PDF Upload</div>
                    <div class="feature-desc">Upload textbooks or question papers and ask anything</div>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">📈</div>
                    <div class="feature-title">Graph Plotter</div>
                    <div class="feature-desc">Visualize any mathematical function instantly</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    for i, msg in enumerate(st.session_state.messages):
        if msg["role"] == "user":
            st.markdown(f"""
            <div class="msg-user">
                <div class="msg-user-name">▸ You</div>
                {msg["content"]}
            </div>""", unsafe_allow_html=True)
            edit_col, _ = st.columns([1, 9])
            with edit_col:
                if st.button("✏️ Edit", key=f"edit_msg_{i}", help="Edit this question"):
                    st.session_state["user_input"] = msg["content"]
                    st.rerun()
        else:
            st.markdown("""
            <div class="msg-ai-label">
                <div class="msg-ai-tag">∫ MathAI</div>
                <div class="msg-ai-line"></div>
            </div>""", unsafe_allow_html=True)
            st.markdown(msg["content"])

            # ── FIX: Clean plain text for copy ──────────────────────
            clean = msg["content"]
            clean = re.sub(r'\$\$(.+?)\$\$', r'\1', clean, flags=re.DOTALL)
            clean = re.sub(r'\$(.+?)\$', r'\1', clean)
            clean = re.sub(r'━+', '─────────────────────', clean)
            clean = re.sub(r'\*\*(.+?)\*\*', r'\1', clean)
            clean = re.sub(r'\*(.+?)\*', r'\1', clean)
            clean = re.sub(r'\\boxed\{(.+?)\}', r'[ \1 ]', clean)
            clean = re.sub(r'\\frac\{(.+?)\}\{(.+?)\}', r'(\1)/(\2)', clean)
            clean = re.sub(r'\\(pm|mp)', r'±', clean)
            clean = re.sub(r'\\sqrt\{(.+?)\}', r'√(\1)', clean)
            clean = re.sub(r'\\text\{(.+?)\}', r'\1', clean)
            clean = re.sub(r'\\[a-zA-Z]+', '', clean)

            # ── FIX: Use st.code for proper copy button ──────────────
            with st.expander("📋 Copy plain text", expanded=False):
                st.code(clean, language=None)

            if msg.get("sources"):
                tags = "".join(
                    f'<span class="tag">{s["topic"].replace("_"," ").title()}</span>'
                    for s in msg["sources"])
                st.markdown(f'<div style="margin:0.3rem 0 0.5rem">{tags}</div>', unsafe_allow_html=True)

            # ── Feedback buttons ──────────────────────────────────────
            fb_col1, fb_col2, fb_col3 = st.columns([1, 1, 8])
            with fb_col1:
                if st.button("👍", key=f"up_{i}", help="Helpful"):
                    st.toast("Thanks for the feedback! 🎉")
            with fb_col2:
                if st.button("👎", key=f"dn_{i}", help="Not helpful"):
                    st.toast("Thanks! We'll improve. 🙏")

    st.markdown('<div class="input-label">Ask a question</div>', unsafe_allow_html=True)
    col1, col2 = st.columns([5, 1])
    with col1:
        user_input = st.text_area(
            "Question:", height=90,
            placeholder="e.g.  Solve 2x² + 5x - 3 = 0   ·   Find derivative of x³·sin(x)   ·   Explain eigenvalues",
            key="user_input", label_visibility="collapsed")
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        send = st.button("Solve →", use_container_width=True, type="primary")

    pending_query = st.session_state.get("pending")
    if pending_query:
        st.session_state.pending = None
        st.session_state.messages.append({"role": "user", "content": pending_query})
        st.session_state.query_count += 1
        with st.spinner("🧮 Computing solution..."):
            result = st.session_state.engine.query(pending_query)
        st.session_state.messages.append({
            "role":          "assistant",
            "content":       result["answer"],
            "sources":       result.get("sources", []),
            "symbolic_hint": result.get("symbolic_hint"),
        })
        st.rerun()

    elif send and user_input.strip():
        # Route through pending — same safe pattern used by Quick Examples.
        # NEVER mutate st.session_state["user_input"] here: that key is bound
        # to the text_area widget and setting it mid-run causes Streamlit to
        # abort the script silently before query() is ever called.
        st.session_state.pending = user_input.strip()
        st.rerun()

    with st.expander("💡 Tips", expanded=False):
        st.markdown("""
        - **Type question** → click Ask ∫ for step-by-step solution
        - **📷 Camera** → snap photo of handwritten problem → auto solves!
        - **🖼️ Upload Image** → upload screenshot or photo of any problem
        - **📄 PDF Upload** → upload textbook or notes → 3 action buttons appear!
        - **Graph**: Type `x**2, sin(x)` in sidebar Graph Plotter
        - **Symbolic**: Use ⚡ Compute for instant derivatives/integrals
        - **Copy**: Click 📋 Copy plain text below any answer
        """)


# ╔══════════════════════════════════════════════════════════════════════╗
# ║  STEP 7 — TESTING                                                   ║
# ╚══════════════════════════════════════════════════════════════════════╝

class TestDataSources(unittest.TestCase):
    def test_builtin_knowledge(self):
        docs = MathDataLoader().load_builtin_knowledge()
        self.assertGreater(len(docs), 0)
        self.assertTrue(all(len(d.page_content) > 50 for d in docs))
        self.assertTrue(all("topic" in d.metadata for d in docs))

class TestPreprocessing(unittest.TestCase):
    def setUp(self):
        self.pp = MathDataPreprocessor()

    def test_cleans_whitespace(self):
        doc = Document(page_content="Hello   World\n\n\n\nMath content here is important", metadata={})
        result = self.pp.preprocess_document(doc)
        self.assertIsNotNone(result)
        self.assertNotIn("\n\n\n", result.page_content)

    def test_deduplication(self):
        doc = Document(page_content="The derivative of x squared is 2x. " * 10, metadata={})
        self.assertIsNotNone(self.pp.preprocess_document(doc))
        self.assertIsNone(self.pp.preprocess_document(doc))

    def test_topic_detection(self):
        doc = Document(page_content="The derivative and integral of functions in calculus.", metadata={})
        result = self.pp.preprocess_document(doc)
        self.assertEqual(result.metadata["topic"], "calculus")

    def test_skips_short(self):
        self.assertIsNone(MathDataPreprocessor().preprocess_document(
            Document(page_content="too short", metadata={})))

class TestChunking(unittest.TestCase):
    def setUp(self):
        self.splitter = MathTextSplitter(chunk_size=200, chunk_overlap=20)

    def test_splits_large_doc(self):
        doc = Document(page_content="Math paragraph with content. " * 60, metadata={"source": "test"})
        self.assertGreater(len(self.splitter.split_document(doc)), 1)

    def test_metadata_preserved(self):
        doc = Document(page_content="x " * 500, metadata={"source": "test.pdf", "topic": "algebra"})
        for chunk in self.splitter.split_document(doc):
            self.assertEqual(chunk.metadata.get("topic"), "algebra")
            self.assertIn("chunk_index", chunk.metadata)

class TestSymbolicEngine(unittest.TestCase):
    def setUp(self):
        self.sym = SymbolicMathEngine()

    def test_differentiate(self):
        result = self.sym.differentiate("x**3")
        self.assertIsNotNone(result)
        self.assertIn("3*x**2", result.replace(" ", ""))

    def test_integrate(self):
        result = self.sym.integrate("x**2")
        self.assertIsNotNone(result)
        self.assertIn("x**3", result)

    def test_solve(self):
        result = self.sym.solve_equation("x**2 - 4 = 0")
        self.assertIsNotNone(result)
        self.assertIn("2", result)

    def test_simplify(self):
        result = self.sym.try_solve("(x**2 - 1)/(x - 1)")
        self.assertIsNotNone(result)
        self.assertIn("x + 1", result)

class TestMemory(unittest.TestCase):
    def test_add_retrieve(self):
        mem = MongoDBChatMemory(session_id="test")
        mem.add_message("human", "What is a derivative?")
        mem.add_message("assistant", "Rate of change.")
        self.assertGreaterEqual(len(mem.get_history()), 2)

    def test_langchain_messages(self):
        mem = MongoDBChatMemory(session_id="test_lc")
        mem.add_message("human", "Test")
        mem.add_message("assistant", "Answer")
        msgs = mem.get_langchain_messages()
        self.assertTrue(any(isinstance(m, HumanMessage) for m in msgs))


def run_tests() -> bool:
    print("\n" + "="*60 + "\n  RUNNING TEST SUITE\n" + "="*60)
    loader = unittest.TestLoader()
    suite  = unittest.TestSuite()
    for cls in [TestDataSources, TestPreprocessing, TestChunking, TestSymbolicEngine, TestMemory]:
        suite.addTests(loader.loadTestsFromTestCase(cls))
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    return result.wasSuccessful()


def run_evaluation():
    print("\n" + "="*60 + "\n  RAG PIPELINE EVALUATION\n" + "="*60)
    store = build_pipeline()
    test_cases = [
        {"q": "What is the power rule for derivatives?",  "keywords": ["power", "derivative", "n*x"]},
        {"q": "How do you find eigenvalues of a matrix?", "keywords": ["eigenvalue", "determinant", "characteristic"]},
        {"q": "What is Bayes theorem?",                   "keywords": ["probability", "conditional", "P(A|B)"]},
        {"q": "What is the quadratic formula?",           "keywords": ["quadratic", "formula", "discriminant"]},
    ]
    scores = []
    for tc in test_cases:
        docs     = store.similarity_search(tc["q"], k=3)
        combined = " ".join(d.page_content.lower() for d in docs)
        hits     = sum(1 for kw in tc["keywords"] if kw.lower() in combined)
        score    = hits / len(tc["keywords"])
        scores.append(score)
        print(f"  Q: {tc['q'][:50]}... → {score:.2f} ({hits}/{len(tc['keywords'])} keywords)")
    print(f"\n  Average retrieval score: {sum(scores)/len(scores):.3f}")
    sym      = SymbolicMathEngine()
    sym_tests = [
        (sym.differentiate("x**3"),           "3*x**2"),
        (sym.integrate("x**2"),               "x**3"),
        (sym.solve_equation("x**2 - 4 = 0"),  "2"),
    ]
    passed = sum(1 for r, e in sym_tests if r and e in r.replace(" ", ""))
    print(f"  Symbolic engine: {passed}/{len(sym_tests)} tests passed")


def main():
    if any("streamlit" in arg for arg in sys.argv):
        run_streamlit_app()
        return

    parser = argparse.ArgumentParser(description="Advanced Mathematics Assistant")
    parser.add_argument("--setup",   action="store_true", help="Build knowledge base")
    parser.add_argument("--rebuild", action="store_true", help="Force rebuild knowledge base")
    parser.add_argument("--test",    action="store_true", help="Run unit tests")
    parser.add_argument("--eval",    action="store_true", help="Evaluate RAG pipeline")
    args = parser.parse_args()

    print("="*60 + "\n  🧮  Advanced Mathematics Assistant\n" + "="*60)

    if args.test:
        sys.exit(0 if run_tests() else 1)
    elif args.eval:
        run_evaluation()
    elif args.setup or args.rebuild:
        store = build_pipeline(force_rebuild=args.rebuild)
        print(f"\n✅ Knowledge base ready — {store.get_document_count()} chunks indexed")
    else:
        print("\nTo launch the UI:\n")
        print("  python3.11 -m streamlit run main.py\n")


try:
    import streamlit as st
    if hasattr(st, "session_state"):
        run_streamlit_app()
except Exception:
    pass

if __name__ == "__main__":
    main()