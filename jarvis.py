from modules.voice import speak, listen
from modules.assistant import process_command
from config import ASSISTANT_NAME, WAKE_WORDS, EXIT_WORDS

def is_wake_word(command):
    return any(word in command for word in WAKE_WORDS)

def is_exit(command):
    return any(word in command for word in EXIT_WORDS)

def main():
    greeting = get_greeting()
    speak(f"{greeting}, I am {ASSISTANT_NAME}. How can I help you?")

    while True:
        command = listen()

        if not command:
            continue

        if is_exit(command):
            speak("Shutting down. Goodbye!")
            break

        if is_wake_word(command):
            speak("Yes?")
            command = listen()

            if is_exit(command):
                speak("Goodbye!") 
                break

            response = process_command(command)
            speak(response)

if __name__ == "__main__":
    main()
