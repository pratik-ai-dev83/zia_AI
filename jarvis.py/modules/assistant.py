import webbrowser
import os
import datetime
import urllib.parse
import json

MEMORY_FILE = "memory.json"


# MEMORY FUNCTIONS
def load_memory():
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=4)

def remember(key, value):
    data = load_memory()
    data[key] = value
    save_memory(data)

def recall(key):
    data = load_memory()
    return data.get(key)


# MAIN FUNCTIO
def process_command(command):

    if not command:
        return "I didn't catch that"

    command = command.lower()

    # MEMORY 
    if "my name is" in command:
        name = command.replace("my name is", "").strip()
        remember("name", name)
        return f"Nice to meet you {name}"

    elif "what is my name" in command:
        name = recall("name")
        return f"Your name is {name}" if name else "I don't know your name yet"

    elif "i like" in command:
        like = command.replace("i like", "").strip()
        remember("like", like)
        return f"I will remember that you like {like}"

    elif "what do i like" in command:
        like = recall("like")
        return f"You like {like}" if like else "I don't know what you like yet"

    # TIME
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        return f"The time is {current_time}"

    # OPEN WEBSITES 
    elif "youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube..."

    elif "google" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google..."

    # SEARCH
    elif "search" in command:
        query = command.replace("search", "").strip()

        if query:
            encoded = urllib.parse.quote(query)
            url = f"https://www.google.com/search?q={encoded}"
            webbrowser.open(url)
            return f"Searching for {query}"
        else:
            return "What should I search?"

    # PLAY MUSIC
    elif "play" in command:
        song = command.replace("play", "").strip()

        if song:
            encoded = urllib.parse.quote(song)
            url = f"https://www.youtube.com/results?search_query={encoded}"
            webbrowser.open(url)
            return f"Playing {song}"
        else:
            return "Which song should I play?"

    # OPEN APPS
    elif "notepad" in command:
        try:
            os.system("start notepad")
            return "Opening Notepad"
        except:
            return "Couldn't open Notepad"

    elif "vs code" in command:
        try:
            os.system("code")
            return "Opening VS Code"
        except:
            return "Couldn't open VS Code"

    elif "camera" in command:
        try:
            os.system("start microsoft.windows.camera:")
            return "Opening Camera"
        except:
            return "Couldn't open Camera"

    elif "cmd" in command:
        try:
            os.system("start cmd")
            return "Opening Command Prompt"
        except:
            return "Couldn't open CMD"