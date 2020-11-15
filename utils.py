import json
from types import SimpleNamespace

def load_data():
    with open('characters.json', 'r') as f:
        characters_dict = json.load(f)
    return characters_dict