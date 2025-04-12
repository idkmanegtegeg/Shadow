import json

def get_current_version():
    with open('version.json', 'r') as f:
        data = json.load(f)
    return data["version"]
