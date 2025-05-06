# utils/config.py

import os
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
ENV_PATH = os.path.join(BASE_DIR, '.env')

if os.path.exists(ENV_PATH):
    load_dotenv(dotenv_path=ENV_PATH)
else:
    print(f"[WARN] .env file not found at: {ENV_PATH}")

INFURA_URL = os.getenv("INFURA_URL")
if not INFURA_URL or "YOUR_PROJECT_ID" in INFURA_URL:
    raise ValueError("[ERROR] INFURA_URL is missing or invalid. Check your .env file.")
