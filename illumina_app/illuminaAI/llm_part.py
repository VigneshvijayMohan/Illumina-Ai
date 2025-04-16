from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

# Initialize OpenAI Chat model
def llm_process(question, vectordb):

    llm = ChatOpenAI(
        model="gpt-3.5-turbo",  # or "gpt-4" if available
        openai_api_key="your-openai-key"
    )

    # User question
    # question = "is there an email I can ask for help?"
    # question = "is there any email that i can use to contact?"

    # Step 1: Retrieve relevant documents
    relevant_docs = vectordb.similarity_search(question, k=3)
    context = "\n\n".join([doc.page_content for doc in relevant_docs])
    # print(context)

    # Step 2: Create a prompt for the model
    final_prompt = f"""You are a helpful assistant. Use the context below to answer the user's question in a detailed and accurate way. 
    If the answer isn't in the context, say you don't know.

    Context:
    --------------------
    {context}
    --------------------
    Question: {question}
    Answer:"""

    # Step 3: Ask OpenAI
    response = llm([HumanMessage(content=final_prompt)])

    # Output
    # print(response.content)
    return response
