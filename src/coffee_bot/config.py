from pydantic_settings import BaseSettings
from pydantic import SecretStr, Field
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    BOT_TOKEN: SecretStr = Field(..., validation_alias="BOT_TOKEN")

    class Config:
        env_file = f"{BASE_DIR}/.env"


settings = Settings()


