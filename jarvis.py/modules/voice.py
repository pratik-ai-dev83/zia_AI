import pyttsx3
import speech_recognition as sr 

engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    print("jarvis:", text)
    engine.say(text)
    engine.runAndWait()
    
    
def listen():
    recognizer = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=5)
            
        command = recognizer.recognize_google(audio)
        print("You:", command)
        return command.lower()
    
    except sr.WaitTimeoutError:
        return ""
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""