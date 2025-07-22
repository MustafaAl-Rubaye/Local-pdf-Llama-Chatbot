from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
#from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_core.documents import Document
import os

embeddings = OllamaEmbeddings(model="mxbai-embed-large")

pdf_folder = "./pdfs"  # Folder with your PDFs
db_location = "./chrome_langchain_db"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []
    doc_id = 0
    
    for filename in os.listdir(pdf_folder):
        if filename.endswith(".pdf"):
            #loader = PyPDFLoader(os.path.join(pdf_folder, filename))
            loader = UnstructuredPDFLoader(os.path.join(pdf_folder, filename))
            pdf_docs = loader.load()
            for doc in pdf_docs:
                documents.append(Document(page_content=doc.page_content))
                ids.append(str(doc_id))
                doc_id += 1

pdf_store = Chroma(
    collection_name="pdf_docs",
    persist_directory=db_location,
    embedding_function=embeddings
)

if add_documents:
    pdf_store.add_documents(documents=documents, ids=ids)

retriever = pdf_store.as_retriever(search_kwargs={"k": 5})
