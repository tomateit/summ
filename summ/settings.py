from typing import List
from pydantic import BaseSettings

class Settings(BaseSettings):
    HOST: str = "127.0.0.1"
    PORT: int = 8012
    ENVIRONMENT: str = "development"


settings = Settings(
    _env_file=".env",
    _env_file_encoding="utf-8"
)