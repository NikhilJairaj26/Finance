from pydantic_settings import BaseSettings
import os

# The root directory of the backend
backend_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
env_path = os.path.join(backend_root, '.env')


class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"

    class Config:
        env_file = env_path

settings = Settings()
