import pyttsx3
import speech_recognition as sr
import googletrans as trsanslator
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
# engine.say('Hi...Im jarvis')
# engine.say('how may i help you')
engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak('Good morning Sir')
    elif hour>12 and hour<4:
        speak('Good afternoon sir')
    else:
        speak('Good evening sir')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...... ')
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=8)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}")

    except Exception as e:
        # engine.say("Say That Again please")
        # engine.runAndWait()
        # print("Say that again please")
        return "none"
    return query


if __name__ == "__main__":
    # wish()
    listen()
