from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from input_pdfs import retriever


model = OllamaLLM(model="llama3")

temp = """
Answer the question below.

Here is the pdf information to use: {context}

Question: {question}

Answer: 
"""


prompt = ChatPromptTemplate.from_template(temp)


chain = prompt | model

def make_conversation():

    print("Welcome to DocBot!     Type 'exit', 'bye' to stop.")
    while True:
        my_input = input("You: ")
        if my_input.lower() in ["exit", "bye"]:
            break

        #results = model.invoke(input="hello world")
        #context = retriever.invoke(my_input)
        docs = retriever.invoke(my_input)
        context = "\n\n".join(doc.page_content for doc in docs)
        results = chain.invoke({"context": context, "question":my_input})
        print("DocBot: ", results)
        # building a chat history
        context += f"\nUser: {my_input}\nAI: {results}"


if __name__ == "__main__":
    make_conversation()

