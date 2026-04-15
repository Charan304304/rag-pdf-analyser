from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document

def create_vector_store(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    docs = []

    for doc in documents:
        chunks = splitter.split_text(doc["content"])

        for chunk in chunks:
            docs.append(
                Document(
                    page_content=chunk,
                    metadata={"page": doc["page"]}
                )
            )

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    vector_store = FAISS.from_documents(docs, embedding=embeddings)

    return vector_store