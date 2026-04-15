from transformers import pipeline

qa_pipeline = pipeline("text-generation", model="google/flan-t5-base")

def get_response(vector_store, query):
    docs = vector_store.similarity_search(query, k=3)

    context = ""
    pages = set()

    for doc in docs:
        context += doc.page_content + "\n"
        pages.add(doc.metadata.get("page"))

    prompt = f"""
    Answer the question based on the context below.

    Context:
    {context}

    Question:
    {query}
    """

    result = qa_pipeline(prompt, max_length=200, do_sample=False)

    answer = result[0]['generated_text']

    return answer, pages