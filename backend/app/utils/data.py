import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]  # ../../ from utils/data.py
DATA_FILE = PROJECT_ROOT / "samples" / "patients.json"


def load_data():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)
