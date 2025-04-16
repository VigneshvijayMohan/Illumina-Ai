# 🌟 Illumina-AI — Your Smart Document-Based Assistant

**Illumina-AI** is an intelligent assistant chat application that allows users to upload files (currently PDFs) and interact with them through an AI-powered chat interface. The assistant provides context-aware responses based on the uploaded content using advanced retrieval and generation techniques.

---

## 🚀 Features

- 📁 **Smart Document Upload**
  - Supports PDF uploads.
  - Automatically assigns a unique UUID to each file.
  - Detects and avoids processing duplicates.
  - Stores metadata in the database and file content in the filesystem.

- 🧠 **AI-Powered Retrieval-Augmented Generation (RAG)**  
  Uses LangChain to implement a RAG pipeline that:
  - Loads and splits PDF content.
  - Generates embeddings for each chunk.
  - Stores and retrieves data using **ChromaDB** for vector similarity search.

- 💬 **Context-Aware Chat Assistant**  
  When a user asks a question, Illumina-AI:
  - Searches the vector database for relevant content.
  - Passes the matched chunks along with the query to OpenAI's LLM.
  - Returns accurate, context-rich responses in the chat UI.

---

## 🧰 Tech Stack

- **Backend:** Django, Django REST Framework
- **AI & Embeddings:** LangChain, OpenAI
- **Vector DB:** ChromaDB
- **PDF Processing:** LangChain PDF Loader, RecursiveCharacterTextSplitter
- **Frontend:** HTML, CSS, JavaScript (Bootstrap)
- **Storage:** SQLite (for file metadata), Local file system (for file content)

---

## 🔁 Flow Overview

1. **User Uploads PDF**
   - Assigned a UUID
   - Checked for duplicates
   - Stored in DB and file system

2. **AI Module Pipeline**
   - File loaded and split
   - Chunks embedded via LangChain
   - Stored in ChromaDB vector store

3. **Chat Interaction**
   - User submits a query
   - Relevant chunks retrieved via similarity search
   - Combined with query and sent to OpenAI LLM
   - Response returned and shown in UI

