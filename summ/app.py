from datetime import datetime
from fastapi import FastAPI

from models.response import Response


app = FastAPI()

@app.get("/", response_model=Response)
def index_page() -> Response:
    return {
        "text": "No idea ...",
    }


# @app.get("/", response_model=Response)
# def index_page() -> Response:
#     return {
#         "timestamp": datetime.utcnow(),
#     }
