from pydantic import AnyHttpUrl, EmailStr, validator
from pydantic_settings import BaseSettings
from typing import List, Optional, Union
import os
from dotenv import load_dotenv

load_dotenv() # Carrega variáveis do .env

class Settings(BaseSettings):
    PROJECT_NAME: str = "SASI Backend PoC"
    API_V1_STR: str = "/api/v1"
    # BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [] # Configurar CORS depois

    # --- Database --- #
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: int = int(os.getenv("DB_PORT", "5432"))  # Convert to integer with default 5432

    # --- PostgreSQL Auth --- #
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "admin")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "admin")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "sasi")

    # --- PGAdmin Auth --- #
    PGADMIN_DEFAULT_EMAIL: str = os.getenv("PGADMIN_DEFAULT_EMAIL", "admin@admin.com")
    PGADMIN_DEFAULT_PASSWORD: str = os.getenv("PGADMIN_DEFAULT_PASSWORD", "admin")

    # --- JWT Authentication --- #
    SECRET_KEY: str = os.getenv("SECRET_KEY", "default_secret_key") # Use getenv para fallback
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

    # --- First Superuser (opcional, para criação inicial) --- #
    USER_EMAIL_INTINAL: EmailStr = os.getenv("USER_EMAIL_INTINAL")
    USER_PASSWORD_INTINAL: str = os.getenv("USER_PASSWORD_INTINAL")

    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings() 
