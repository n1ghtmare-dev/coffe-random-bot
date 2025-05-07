from pydantic_settings import BaseSettings
from pydantic import SecretStr, Field
from pathlib import Path



BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    BOT_TOKEN: SecretStr = Field(..., validation_alias="BOT_TOKEN") 
    DB_URL: str = f"sqlite+aiosqlite:///{BASE_DIR}/data/db.sqlite3"

    class Config:
        env_file = BASE_DIR / ".env"



settings = Settings() # type: ignore

