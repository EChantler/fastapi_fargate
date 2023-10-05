import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()



class Settings():
    APP_TITLE:str = os.getenv("APP_TITLE")
    APP_VERSION:str = os.getenv("APP_VERSION")
    APP_HOST:str = os.getenv("APP_HOST")
    APP_PORT:int = os.getenv("APP_PORT")



settings = Settings()