from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from scraper import get_info
# from send_api import get_result

from local_llama import give_description



app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.post("/submit")
async def handle_form(request:Request, userInput: str = Form(...)):
   
    prompt = get_info(userInput)
  
    ##for OpenAI api
    # prompt_result = get_result(prompt)
    prompt_result = give_description(prompt)

    return templates.TemplateResponse("submit.html", {"request": request, "prompt_result": prompt_result})
