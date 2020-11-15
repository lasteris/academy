import json

def load_data():
    text = ''
    with open('characters.json', 'r') as f:
        text = json.load(f)
    return text