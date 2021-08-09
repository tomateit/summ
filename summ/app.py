from datetime import datetime
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from models.response import Response
from models.request import Request
from summarizer import Summarizer
from pathlib import Path

app = FastAPI()

html_page_path = Path(Path(__file__).parent / Path("./static/index.html"))

@app.get("/", response_class=HTMLResponse)
async def index_page():
    with open(html_page_path,"r") as page:
        return page.read()


model = Summarizer()


@app.post("/", response_model=Response)
async def endpoint(request: Request) -> Response:

    return {
        "text": model(request.text, num_sentences=request.constraint),
    }


