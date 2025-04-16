#Loading document


from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


def loading_splitting(file_path, chunkSize, chunkOverlap):
    # loader = PyPDFLoader(r"C:\Users\vigne\Desktop\Get_done\RAG\CV ARYA.pdf")
    loader = PyPDFLoader(file_path)
    pages = loader.load()
    # print(len(pages))
    # page = pages[0]
    # print(page.page_content[0:1000])


    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=chunkSize,
        chunk_overlap=chunkOverlap,
        length_function=len
    )
    # text_splitter = TokenTextSplitter(chunk_size=1000, chunk_overlap=100)
    # docs_token = text_splitter.split_documents(pages)

    docs = text_splitter.split_documents(pages)
    return docs