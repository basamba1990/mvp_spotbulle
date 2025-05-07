from pydantic import BaseSettings

class Settings(BaseSettings):
    supabase_url: str
    supabase_key: str
    openai_key: str = None

    class Config:
        env_file = ".env"

settings = Settings()
