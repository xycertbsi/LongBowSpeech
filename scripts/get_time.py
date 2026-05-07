import pyttsx3
tts = pyttsx3.init()
import time

def run():
    current_time = time.strftime("%H:%M:%S")
    print("Current time: ", current_time)
    tts.say("Current time: " + current_time)
    tts.runAndWait()
