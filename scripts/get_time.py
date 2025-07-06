import pyttsx3
tts = pyttsx3.init()
import time

def run():
    current_time = time.strftime("%H:%M:%S")
    print("Jelenlegi idő: ", current_time)
    tts.say("Jelenlegi idő: " + current_time)
    tts.runAndWait()
