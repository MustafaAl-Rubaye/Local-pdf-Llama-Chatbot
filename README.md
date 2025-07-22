# Local-pdf-Llama-Chatbot

A simple, fast, and fully **local chatbot** that lets you **talk to any PDF** using [Ollama](https://ollama.com), [LangChain](https://www.langchain.com/), and **LLaMA3** — with document-aware retrieval powered by Chroma and embeddings from `mxbai-embed-large`.

It shows how to:
- 🧠 Run a Retrieval-Augmented Generation (RAG) pipeline
- 📄 Process PDFs and extract metadata
- 💬 Build a conversational interface for querying local files
- 🔒 Work completely offline after setup

---

## 🚀 Getting Started

### 1. Set up the environment

```bash
conda create --name new_env python=3.10 -y
conda activate new_env
```

### 2. Install Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Pull the required models:

```bash
ollama pull llama3
ollama pull mxbai-embed-large
```

### 3. Install Python Dependencies
```bash
pip install langchain langchain-ollama ollama
pip install langchain-chroma langchain-community
pip install pypdf "unstructured[pdf]"
```


## 💬 Run the Chatbot
python main_ollama.py
