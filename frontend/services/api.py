import requests
from utils.config import API_BASE


def get(path, params=None):
    r = requests.get(f"{API_BASE}{path}", params=params)
    r.raise_for_status()
    return r.json()


def post(path, payload):
    r = requests.post(f"{API_BASE}{path}", json=payload)
    r.raise_for_status()
    return r.json()


def put(path, payload):
    r = requests.put(f"{API_BASE}{path}", json=payload)
    r.raise_for_status()
    return r.json()


def delete(path):
    r = requests.delete(f"{API_BASE}{path}")
    r.raise_for_status()
    return r.json()
