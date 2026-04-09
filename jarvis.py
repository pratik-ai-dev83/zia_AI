import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

engine = pyttsx3.int()

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
    commabd = r.recognizing_google(audio, languag='en-in')
    print("You said:", command)
  except Exception:
    speak("Sorry, I didn't understand.")
    return "none"

return commnd.lower()
