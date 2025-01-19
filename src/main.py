import re

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from src.local_llama import give_description
from src.scraper import get_prompt

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request) -> HTMLResponse:
    """
    Render the home page with the given request context.

    This function handles a GET request and returns an HTML template
    response for the home page.

    Args:
        request (Request): The incoming HTTP request object.

    Returns:
        Response: An HTML response containing the rendered home page template.
    """
    return templates.TemplateResponse("home.html", {"request": request})


@app.post("/submit")
async def handle_form(
    request: Request, userInput: str = Form(...)
) -> HTMLResponse:
    """
    Render the response page with the output text.

    This function handles a POST request and returns an HTML template
    response with text based on the input of the user in the home page.

    Args:
        request (Request): The incoming HTTP request object.
        userInput (str): The instagram account name provided by user.

    Returns:
        Response: An HTML response containing the rendered page with description.
    """
    prompt = get_prompt(userInput)

    prompt_result = give_description(prompt)

    prompt_result = re.sub(
        r"\*\*(.*?)\*\*:", r"<br><br><b>\1</b><br>", prompt_result
    )
    prompt_result = re.sub(r"(\d\.)", r"", prompt_result)

    return templates.TemplateResponse(
        "submit.html", {"request": request, "prompt_result": prompt_result}
    )
