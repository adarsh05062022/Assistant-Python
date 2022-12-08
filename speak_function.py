import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voices",voices[0].id)
engine.setProperty('rate',180)

def speak(command):
    print("")
    engine.say(command)
    print(f"{command} \n")
    engine.runAndWait()