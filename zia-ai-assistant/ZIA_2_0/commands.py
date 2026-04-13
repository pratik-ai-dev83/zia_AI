import os
import pywhatkit as kit
from zia_ai import ZIA
from utils import remember, recall, set_alarm, explain_error

zia = ZIA()

def search_file(name):
    base_dirs = [
        os.path.expanduser("~/Desktop"),
        os.path.expanduser("~/Documents")
    ]

    for directory in base_dirs:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if name.lower() in file.lower():
                    os.startfile(os.path.join(root, file))
                    return f"File found: {file}"
    return "No matching file found."

def send_whatsapp(text, number="+91XXXXXXXXXX"):
    kit.sendwhatmsg_instantly(number, text)
    return "Message delivered."

def call_contact(name):
    return f"Calling {name} feature is not fully supported yet."

def read_notifications():
    return "Notification reading system will be enabled soon."

def process_command(text):
    text = text.lower()

    if "search file" in text:
        name = text.replace("search file named", "").strip()
        return search_file(name)

    elif "send a whatsapp message" in text:
        return "What should I send?"

    elif "call" in text:
        name = text.replace("call", "").strip()
        return call_contact(name)

    elif "read notifications" in text:
        return read_notifications()

    elif "explain this error" in text:
        return "Tell me the error."
    elif "remember" in text:
        key = text.split(" is ")[0].replace("remember", "").strip()
        value = text.split(" is ")[1].strip()
        remember(key, value)
        return "Memory stored."

    elif "what did i tell you" in text or "recall" in text:
        return recall("birthday")

    elif "wake me up at" in text:
        alarm_time = text.replace("wake me up at", "").strip().upper()
        set_alarm(alarm_time)
        return f"Alarm set for {alarm_time}"

    return None
