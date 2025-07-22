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
conda install python -y
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
pip install unstructured pypdf
# or install the full extra dependencies
pip install "unstructured[pdf]"
```


## 💬 Run the Chatbot

```bash
python main_ollama.py
```

### Example questions

```bash
Welcome to DocBot!     Type 'exit', 'exit', 'bye' to stop.
You: hi
DocBot:  I'm happy to help! However, I don't see any specific question or PDF information provided. Could you please clarify what you would like me to answer?
```

## 📁 Project Structure
.
├── main_ollama.py          # Chat loop: ask questions about any PDF
├── input_pdfs.py           # Loads, splits, indexes PDFs with metadata
├── pdfs/                   # Drop your PDF files here


