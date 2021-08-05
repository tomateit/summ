from pydantic import BaseModel
# from typing import List, Optional, Tuple


class Response(BaseModel):
    text: str


