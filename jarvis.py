import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

engine = pyttsx3.init()

def speak(text):
  print("jarvis:", text)
  engine.say(text)
  engine.runAndWait()

def take_command():
  r = sr.Recognizer()

with sr.Microphone() as source:
  print("Listening...")
  r.pause_threshold = 1
  audio = r.listen(source)
  try:
    print("Recognizing..")
    command = r.recognize_google(audio, language='en-in')
    print("You said:", command)
  except Exception:
    speak("Sorry, I didn't understand.")
    return "none"

  return command.lower()


def wish_user():
  hour = datetime.datetime.now().hour

  if hour < 12:
    speak("Good morning")
  elif hour < 18:
    speak("Good afternoon")
  else:
    speak("I am Jarvis. How can i help you?")


def run_jarvis():
  while True:
    command = take_command()

    if "time" in command:
      time = datetime.datetime.now().strftime("%H:%M")
      speak(f"The time is {time}")

    elif"open youtube" in command:
      webbrowser.open("https://youtubr.com")

    elif "open google" in command:
      webbrowser.open("https://github.com")

    elif "open code" in command:
      os.system("code")

    elif "play music" in command or "Play song" in command:
       speak("Wich song do you want to play?")
       song_name = take_command().lower()

      if song_name:
        url = f"https://open.spotify.com/search/{song_name}"
        webbroser.open(url)
        speak(f"Playing {song_name} on Spotify")
    else:
      speak("Song name not recogized")

elif "exit" in command or "stop" in command:
  speak("Good bye!")
  break

elif command != "none":
  speak("I can serch tht for you")
  webbrowser.open(f"https//www.google.com/search?q={command}")


if __name_ == "__main__":
  run_jarvis()
      
      

   
