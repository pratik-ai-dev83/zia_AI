import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

engine = pyttsx3.init()

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio, language='en-in')
        print("You said:", command)
    except Exception:
        speak("Sorry, I didn't understand.")
        return "none"

    return command.lower()

def wish_user():
    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good morning, I am Jarvis. How can I help you?")
    elif hour < 18:
        speak("Good afternoon, I am Jarvis. How can I help you?")
    else:
        speak("Good evening, I am Jarvis. How can I help you?")
        
    
   

def run_jarvis():
    wish_user()

    while True:
        command = take_command()

        if "time" in command:
            current_time = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {current_time}")

        elif "open youtube" in command:
            webbrowser.open("https://youtube.com")

        elif "open google" in command:
            webbrowser.open("https://google.com")

        elif "open code" in command:
            os.system("code")

        elif "play music" in command or "play song" in command:
            speak("Which song do you want to play?")
            song_name = take_command()

            if song_name != "none":
                url = f"https://open.spotify.com/search/{song_name}"
                webbrowser.open(url)
                speak(f"Playing {song_name} on Spotify")
            else:
                speak("Song name not recognized")

        elif "exit" in command or "stop" in command:
            speak("Goodbye!")
            break

        elif command != "none":
            speak("I can search that for you")
            webbrowser.open(f"https://www.google.com/search?q={command}")

if __name__ == "__main__":
    run_jarvis()
    