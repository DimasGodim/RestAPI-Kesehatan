import os
from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Config(BaseSettings):
    # api_key_opneai
    api_key_openai: str = os.getenv("API_KEY_OPENAI")
    
    # configs database
    url_database:  str = os.getenv("DATABASE_URL")

config = Config()