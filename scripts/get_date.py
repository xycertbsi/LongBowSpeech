import pyttsx3
import datetime

tts = pyttsx3.init()

def run():
    now = datetime.datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    print("Current Date:", current_date)
    tts.say("Current Date:" + current_date)
    tts.runAndWait()
