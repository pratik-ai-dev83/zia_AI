import webbrowser
import os
import datetime
import urllib.parse


def process_command(command):
    
    if not command:
        return "I didn't catch that"

    command = command.lower()

    if "youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube..."

    elif "google" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google..."

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        return f"The time is {current_time}"

    elif "notepad" in command:
        try:
            os.system("notepad")
            return "Opening Notepad"
        except:
            return "Couldn't open Notepad"

    elif "search" in command:
        query = command.replace("search", "").strip()

        if query:
            query = urllib.parse.quote(query)
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            return f"Searching for {query}"
        else:
            return "What should I search?"

    elif "exit" in command:
        return "exit"

    else:
        return "Sorry, I don't understand that yet"


while True:
    cmd = input("Enter command: ")
    result = process_command(cmd)

    if result == "exit":
        break

    print(result)
