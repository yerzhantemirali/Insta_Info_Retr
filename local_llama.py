from langchain_ollama import OllamaLLM

model = OllamaLLM(model="Llama3:8b")

def give_description(prompt):

    result = model.invoke(prompt)

    return result