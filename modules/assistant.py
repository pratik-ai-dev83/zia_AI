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

def process_command(command):
    if not command:
        return "I didn't catch that"

command = command.lower()

if "my name is" in command:
    name = command.replace("my name is", "").strip()
    remember("name", name)
    return f"Nice to meet you {name}"

elif "i like" in command:
    like = command.replace("i like", "").strip()
    remember("like", like)
    return f"I will remember that you like {like}"

elif "what do i like" in command:
    like = recall("like")
    return f"You like {like}" if like else "I don't know what you like yet"

elif "time" in command:
    current_time = datetime.datatime.now().strftime("%H:%M:%S")
    return f"The time is {current_time}"

elif "youtube" in command:
    webbrowser.open("https://www.youtube.com")
    return "Opening Youtube..."

elif "google" in command:
    webbrowser.open("https://www.google.com")
    return "Opening Google..."

elif "search" in command:
    query = cpmmand.replace("search", "").strip()

    if query:
        encoded = urllib.parse.quote(query)
