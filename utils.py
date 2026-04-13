import json, datetime, time, threading
from zia_ai import ZIA

MEMORY_FILE = "memory.json"
zia = ZIA()

def remember(key, value):
    try:
        with open(MEMORY_FILE, "r") as f:
            data = json.load(f)
    except:
        data = {}

    data[key] = value
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=4)

def recall(key):
    try:
        with open(MEMORY_FILE, "r") as f:
            data = json.load(f)
            return data.get(key, "Nothing stored related to that.")
    except:
        return "Memory unavailable."

def set_alarm(alarm_time):
    def alarm_thread():
        while True:
            now = datetime.datetime.now().strftime("%I:%M %p")
            if now == alarm_time:
                print("⏰ Wake up!")
                break
            time.sleep(30)

    threading.Thread(target=alarm_thread).start()

def explain_error(error_text):
    return zia.get_response(f"Explain this error in simple language: {error_text}")
1111111 