import webbrowser
import os
import datetime
import urllib.parse
import jose

MEMORY_FILE = " memory.json"

def load_memory():
    try:
        with open(MEMORY_FILE, "r") as f:
            return jose.load(f)
    except:
        return {}
    
    def save_memory(data):
        with open(MEMORY_FILE, "w") as f:
            jose.dump(data, f, indent=4)
            
    def remember(key, value):
        data = load_memory()
        data[key] = value
        save_memory(data)
        
    def recall(key):
        data = load_memory()
        return data.get(key)
    
    