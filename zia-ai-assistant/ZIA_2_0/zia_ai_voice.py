import speech_recognition as sr
import subprocess
import datetime
import os
from playsound import playsound
from zia_ai import ZIA

# 🎙 Initialize ZIA AI
zia = ZIA()

# 🔊 Voice File (YOUR NEERJA VOICE)
VOICE_FILE = r"ZIA_Indian_(Neerja).mp3"


# 🔉 Speak Function (Plays MP3 Voice)
def speak_and_print(response):
    print(f"ZIA 🗣: {response}")

    try:
        playsound(VOICE_FILE)
    except Exception as e:
        print("🔇 Voice play error:", e)


# 🎧 Listen Function
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)

        try:
            audio = recognizer.listen(source, timeout=6)
            text = recognizer.recognize_google(audio, language="en-in").lower()
            print(f"You: {text}")
            return text

        except sr.UnknownValueError:
            speak_and_print("Sorry, I didn't understand.")
            return None

        except sr.RequestError:
            speak_and_print("Speech service is unavailable.")
            return None

        except Exception as e:
            print("⚠ Listening error:", e)
            return None


# 📱 App Control
def open_app(command):
    apps = {
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "notepad": "notepad.exe",
        "file explorer": "explorer.exe",
        "calculator": "calc.exe",
        "spotify": r"C:\Users\psp77\AppData\Roaming\Spotify\Spotify.exe",
        "whatsapp": rf"C:\Users\{os.environ['USERNAME']}\AppData\Local\WhatsApp\WhatsApp.exe",
        "telegram": r"C:\Users\psp77\OneDrive\Desktop\Telegram.lnk",
        "camera": "start microsoft.windows.camera:",
        "settings": "start ms-settings:",
        "instagram": "start https://www.instagram.com",
        "facebook": "start https://www.facebook.com"
    }

    for app, path in apps.items():
        if app in command:
            try:
                if path.startswith("start "):
                    subprocess.Popen(path, shell=True)
                else:
                    subprocess.Popen([path])

                speak_and_print(f"Opening {app}.")
                return True

            except FileNotFoundError:
                speak_and_print(f"I could not open {app}. Path not found.")
                return True

    return False

 
# ▶ YouTube Control
def youtube_action(command):
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

    if not os.path.exists(chrome_path):
        speak_and_print("Chrome not found!")
        return True

    if "search" in command and "on youtube" in command:
        query = command.replace("search", "").replace("on youtube", "").strip()

        if query:
            url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
            subprocess.Popen([chrome_path, url])
            speak_and_print(f"Searching for {query} on YouTube.")
            return True

    elif "open youtube" in command:
        subprocess.Popen([chrome_path, "https://www.youtube.com"])
        speak_and_print("Opening YouTube.")
        return True

    return False


# 🧠 MAIN SYSTEM
def main():
    speak_and_print("Hello! I'm ZIA, your assistant.")

    while True:
        user_input = listen()
        if user_input is None:
            continue

        # Exit
        if any(word in user_input for word in ["exit", "quit", "stop", "goodbye"]):
            speak_and_print("Goodbye! Shutting down.")
            break

        # Time
        elif "time" in user_input:
            t = datetime.datetime.now().strftime("%I:%M %p")
            speak_and_print(f"The time is {t}.")

        # Date
        elif "date" in user_input:
            d = datetime.datetime.now().strftime("%B %d, %Y")
            speak_and_print(f"Today's date is {d}.")

        # App opening
        elif open_app(user_input):
            continue

        # YouTube
        elif youtube_action(user_input):
            continue

        # Default AI Chat Response
        else:
            response = zia.get_response(user_input)
            speak_and_print(response)


if __name__ == "__main__": 
    main()


