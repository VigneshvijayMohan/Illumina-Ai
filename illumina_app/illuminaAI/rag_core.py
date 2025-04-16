from illumina_app.illuminaAI.pdf_loader import loading_splitting
from illumina_app.illuminaAI.embeddings import embed
from illumina_app.illuminaAI.llm_part import llm_process


def rag_core(file_path, dbname, question):
    chunkSize = 500
    chunkOverlap = 50
    docs = loading_splitting(file_path,chunkSize,  chunkOverlap)
    vectorbd = embed(docs, dbname)
    response = llm_process(question, vectorbd)
    return response.content
    

