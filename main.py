import colorama
from colorama import Fore, Back, Style
from dotenv import load_dotenv
import os
import time
import importlib
import speech_recognition as sr

# inits
load_dotenv()
colorama.init()


command_require = os.getenv('command_require')
command = os.getenv('command')
lang = os.getenv('ListingLang')

imports = [
    "get_time",
    "get_date"
]


mimport = {}
for module_name in imports:
    mimport[module_name] = importlib.import_module(f"scripts.{module_name}")


commands = {
    "time": mimport["get_time"].run,
    "date": mimport["get_date"].run
}



class Msgs():
    def error(msg):
        m = Fore.RED + "[!] " + msg + Fore.RESET
        return m
    
    def succ(msg):
        m = Fore.GREEN + "[#] " + Fore.CYAN + msg + Fore.RESET
        return m
    
    def warn(msg):
        m = Fore.YELLOW + "[W] " + msg + Fore.RESET
        return m
    
    def ignor(msg):
        m = Fore.LIGHTBLACK_EX + "[i] " + msg + Fore.RESET
        return m

class Core():

    def command_exe(txt):
        print(Msgs.succ(txt))

        command.lower()
        cmd = txt.replace(command, "").strip()

        if cmd in commands:
            commands[cmd]()
        else:
            print(Msgs.ignor(txt))

    def listingA():
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            audio_data = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio_data, language=lang)

            if command_require:
                if command in text:
                    Core.command_exe(text)
                else: print(Msgs.ignor(text))
            else:
                Core.command_exe(text)
        except sr.UnknownValueError:
            print(Msgs.error("Sorry, could not understand audio."))
        except sr.RequestError as e:
            print(Msgs.warn("Error: Could not request results from Google Speech Recognition service."))

print(Msgs.ignor("Started!"))
while True:
    Core.listingA()