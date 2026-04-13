import json
import os
import subprocess
import datetime
import re
import webbrowser
import speech_recognition as sr
import pyttsx3
from typing import Dict, Any

MEMORY_FILE = 'memory.json'
APPS_FILE = 'apps.json'

COMMON_SEARCH_DIRS = [
    os.path.join(os.environ.get('USERPROFILE', ''), 'Desktop'),
    os.path.join(os.environ.get('USERPROFILE', ''), 'AppData', 'Roaming'),
    os.path.join(os.environ.get('USERPROFILE', ''), 'AppData', 'Local'),
    r"C:\Program Files",
    r"C:\Program Files (x86)",
]

class ZIA:
    def __init__(self):
        self.memory = self.load_memory()
        self.user_name = self.memory.get('name', 'User')
        self.apps = self.load_apps()

        # Voice setup
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 180)
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id if len(voices) > 1 else voices[0].id)

        self.recognizer = sr.Recognizer()

    # ---------------- Helper Methods ----------------
    def speak(self, text: str):
        print(f"ZIA 🗣️: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def listen_once(self) -> str:
        with sr.Microphone() as source:
            print("Listening...")
            try:
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=8)
                text = self.recognizer.recognize_google(audio).lower()
                print(f"You: {text}")
                return text
            except:
                return ""

    def load_memory(self) -> Dict[str, Any]:
        if os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, 'r') as f:
                return json.load(f)
        return {}

    def save_memory(self):
        with open(MEMORY_FILE, 'w') as f:
            json.dump(self.memory, f, indent=4)

    def update_memory(self, key: str, value: Any):
        self.memory[key] = value
        self.save_memory()
        if key == 'name':
            self.user_name = value

    def load_apps(self) -> Dict[str, str]:
        if os.path.exists(APPS_FILE):
            try:
                with open(APPS_FILE, 'r') as f:
                    return json.load(f)
            except:
                return {}
        return {}

    def save_apps(self):
        with open(APPS_FILE, 'w') as f:
            json.dump(self.apps, f, indent=4)

    def add_app(self, name: str, path: str):
        self.apps[name.lower()] = path
        self.save_apps()

    def find_app_executable(self, app_name: str) -> str:
        name = app_name.lower()
        stored = self.apps.get(name)
        if stored and os.path.exists(stored):
            return stored

        # quick scan for exe
        for base in COMMON_SEARCH_DIRS:
            for root, dirs, files in os.walk(base):
                for f in files:
                    if f.lower().startswith(name) and f.lower().endswith(".exe"):
                        return os.path.join(root, f)
        return ""

    def _open_path(self, path: str) -> bool:
        try:
            if path.startswith("http"):
                webbrowser.open(path)
                return True
            if os.path.exists(path):
                subprocess.Popen(f'start "" "{path}"', shell=True)
                return True
        except Exception as e:
            print(f"Open Error: {e}")
        return False

    # ---------------- Main Response ----------------
    def get_response(self, user_input: str) -> str:
        user_input = user_input.lower().strip()

        # Memory
        if 'my name is' in user_input:
            name = user_input.split('my name is')[-1].strip()
            self.update_memory('name', name)
            return f"Got it, I'll remember your name as {name}."

        if 'what is my name' in user_input:
            return f"Your name is {self.user_name}."

        # Time / Date
        if 'time' in user_input:
            return f"It's {datetime.datetime.now().strftime('%I:%M %p')}."
        if 'date' in user_input:
            return f"Today is {datetime.datetime.now().strftime('%B %d, %Y')}."

        # YouTube Search
        if "youtube" in user_input and ("search" in user_input or "play" in user_input):
            query = user_input.split("search")[-1].replace("on youtube", "").strip()
            if not query:
                query = user_input.split("play")[-1].replace("on youtube", "").strip()
            if query:
                url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
                self._open_path(url)
                return f"Searching {query} on YouTube."

        # Google Search
        if "search" in user_input and "google" in user_input:
            query = user_input.split("search")[-1].replace("on google", "").strip()
            url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            self._open_path(url)
            return f"Searching Google for {query}."

        # Open app
        if user_input.startswith(("open", "launch")):
            app_name = user_input.replace("open", "").replace("launch", "").strip()
            found = self.find_app_executable(app_name)
            if found:
                self._open_path(found)
                return f"Opening {app_name}."
            else:
                # Ask user for path
                self.speak(f"I couldn't find {app_name} on your system. Would you like to tell me its path?")
                ans = self.listen_once()
                if "yes" in ans:
                    self.speak(f"Please say the full path for {app_name}.")
                    path = self.listen_once()
                    if path:
                        self.add_app(app_name, path)
                        self.speak(f"Got it, I've saved {app_name}'s path. Opening now.")
                        self._open_path(path)
                        return f"Added and opened {app_name}."
                    else:
                        return f"Okay, I didn't catch the path for {app_name}."
                else:
                    return f"Alright, skipping {app_name}."

        # Close app
        if user_input.startswith("close"):
            app_name = user_input.replace("close", "").strip()
            path = self.apps.get(app_name)
            if path and path.endswith(".exe"):
                exe = os.path.basename(path)
                try:
                    subprocess.run(f'taskkill /f /im {exe}', shell=True)
                    return f"Closing {app_name}."
                except:
                    return f"Couldn't close {app_name}."
            else:
                return f"I don't know how to close {app_name}."

        if any(greet in user_input for greet in ["hi", "hello", "hey"]):
            return f"Hello {self.user_name}, how can I help you?"

        return "I'm sorry, I didn't understand that."
    
    
    