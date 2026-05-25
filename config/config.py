import os
from dotenv import load_dotenv
import yaml

load_dotenv()

class Config:
    BASE_URL = os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com")
    USERNAME = os.getenv("API_USERNAME", "bishnu")
    PASSWORD = os.getenv("API_PASSWORD", "123456")

    settings_path = os.path.join(os.path.dirname(__file__), "settings.yaml")
    with open(settings_path, "r") as f:
        SETTINGS = yaml.safe_load(f)
        
config = Config()
