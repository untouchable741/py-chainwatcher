from dotenv import load_dotenv
import os

load_dotenv()

INFURA_URL = os.getenv("INFURA_URL")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
WATCHED_ADDRESS = os.getenv("WATCHED_ADDRESS")
