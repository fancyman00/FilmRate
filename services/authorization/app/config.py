import os

from pydantic import computed_field, PostgresDsn
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict

DOTENV = os.path.join(os.path.dirname(__file__), ".env")


class Settings(BaseSettings):
    JWT_ALGORITHM: str
    JWT_REFRESH_TOKEN_EXPIRE: int
    JWT_ACCESS_TOKEN_EXPIRE: int

    EMAIL_SERVER: str
    EMAIL_LOGIN: str
    EMAIL_PASSWORD: str
    EMAIL_EXPIRE: int

    WEBSERVER_HOST: str
    WEBSERVER_PORT: str

    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str

    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    @computed_field
    @property
    def asyncpg_url(self) -> PostgresDsn:
        return MultiHostUrl.build(
            scheme="postgresql+asyncpg",
            username=self.POSTGRES_USER,
            port=self.POSTGRES_PORT,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_HOST,
            path=self.POSTGRES_DB,
        )

    @computed_field
    @property
    def psyncopg_url(self) -> PostgresDsn:
        return MultiHostUrl.build(
            scheme="postgresql+psyncopg_url",
            username=self.POSTGRES_USER,
            port=self.POSTGRES_PORT,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_HOST,
            path=self.POSTGRES_DB,
        )

    @computed_field
    @property
    def email_verify_url(self) -> str:
        return f'http://{self.WEBSERVER_HOST}:{self.WEBSERVER_PORT}/auth/verify-email/'

    model_config = SettingsConfigDict(env_file=DOTENV)


settings = Settings()
