from langchain_ollama import OllamaLLM

model = OllamaLLM(model="Llama3:8b")


def give_description(prompt: str) -> str:
    """
    Get a response of the LLM based on prompt and return it.

    This function takes a string type prompt
    and returns the resulting text of LLM response.

    Args:
        prompt (str): The prompt to sent to the LLM.

    Returns:
        str: Resulting response of the LLM.
    """
    result = model.invoke(prompt)

    return result
