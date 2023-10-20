from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    """Settings of project."""

    API_V1_STR: str = "/api/v1"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    ALGORITHM: str = "HS256"

    SECRET_KEY: str

    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: str

    FIRST_SUPERUSER: str = "super_username"
    FIRST_SUPERUSER_PASSWORD: str = "super_password"
    SUPER_USER_ROLE: str = "SUPER_USER_ROLE"


settings = Settings()
