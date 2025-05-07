from pydantic import BaseSettings

class Settings(BaseSettings):
    supabase_url: str
    supabase_key: str
    openai_key: str = None
    DATABASE_URL: str = "postgresql+asyncpg://user:pass@localhost/dbname"
    SECRET_KEY: str = "secret-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440

    class Config:
        env_file = ".env"

settings = Settings()
