import os

from pydantic_settings import BaseSettings, SettingsConfigDict

DOTENV = os.path.join(os.path.dirname(__file__), ".env")


class Settings(BaseSettings):
    JWT_ALGORITHM: str
    JWT_REFRESH_TOKEN_EXPIRE: int
    JWT_ACCESS_TOKEN_EXPIRE: int
    model_config = SettingsConfigDict(env_file=DOTENV)


settings = Settings()
