import pyttsx3
import datetime

tts = pyttsx3.init()

def run():
    now = datetime.datetime.now()  # Lekérjük az aktuális dátumot és időt
    current_date = now.strftime("%Y-%m-%d")  # Formázott dátum
    print("Jelenlegi dátum:", current_date)
    tts.say("Jelenlegi dátum:" + current_date)
    tts.runAndWait()