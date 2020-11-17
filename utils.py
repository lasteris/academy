import json
from types import SimpleNamespace

def load_dict(path):
    with open(path, 'r') as f:
        dictionary = json.load(f)
    return dictionary