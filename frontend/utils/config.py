import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

API_BASE = os.getenv("API_BASE_URL")

if not API_BASE:
    raise RuntimeError("API_BASE_URL is not set in .env")
