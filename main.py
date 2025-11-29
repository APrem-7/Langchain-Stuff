from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

from vector import retriever

model = OllamaLLM(model="llama3.2:3b")

template = """
You are an expert in answering questions about a pizza restaurant

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

#letting teh user ask the question
while True:
    question=input("Hello How May i help You || Press q to leave")
    if question == "q":
        print("Thanks")
        break

    reviews=retriever.invoke(question)
    result=chain.invoke({"reviews":reviews,"question":question})
    print(result)