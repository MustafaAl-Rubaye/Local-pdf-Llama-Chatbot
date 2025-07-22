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
