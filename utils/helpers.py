import datetime

def get_time():
    time_now = datetime.datetime.now()
    return time_now.strftime("%I:%M %p")


def get_greeting():
    time_now = datetime.datetime.now()
    h = time_now.hour

    if h < 12:
        return "Good morning"
    elif h < 18:
        return "Good afternoon"
    else:
        return "Good evening"
