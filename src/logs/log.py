from pathlib import Path
import os


path = Path(__file__).resolve().parents[1]

if os.path.exists(path):
    print(path)
