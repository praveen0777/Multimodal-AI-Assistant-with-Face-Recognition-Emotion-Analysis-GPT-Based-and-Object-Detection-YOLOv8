import json
import os

MEMORY_FILE = "user_memory.json"

def retrieve_memory(user):
    if not os.path.exists(MEMORY_FILE):
        return ""
    with open(MEMORY_FILE, "r") as f:
        data = json.load(f)
    return data.get(user, "")

def update_memory(user, prompt, response):
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            data = json.load(f)
    else:
        data = {}

    history = data.get(user, "")
    history += f"\nUser: {prompt}\nMaya: {response}"
    data[user] = history

    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)

def load_memory():
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
