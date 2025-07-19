# Placeholder for utils.py
import os

def ensure_dirs():
    os.makedirs("data", exist_ok=True)
    os.makedirs("data/results", exist_ok=True)
    os.makedirs("data/params", exist_ok=True)
    os.makedirs("logs", exist_ok=True)
