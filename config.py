import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = int(os.getenv("DB_PORT", "5432"))
    DB_NAME = os.getenv("DB_NAME", "smartcommute_db")
    DB_USER = os.getenv("DB_USER", "postgres")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "0102+-*")
    DATABASE_URL = os.getenv("DATABASE_URL", f"postgresql://{DB_USER}:0102%2B-*@{DB_HOST}:{DB_PORT}/{DB_NAME}")
    SECRET_KEY = os.getenv("SECRET_KEY", "smartcommute_apple_production_secret_2026_x89f")
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    TEMPLATES_AUTO_RELOAD = True
