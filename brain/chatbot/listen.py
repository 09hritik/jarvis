import speech_recognition as sr
from googletrans import  Translator

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio=r.listen(source,timeout=0,phrase_time_limit=8)   #entered listening mode

#recognizing
    try:
        print("Recognizing....")
        sentence = r.recognize_google(audio,language="en")
        print(f"User said:{sentence}")

    except Exception as e:
        print("Cannot recognize")
        return ""
    query= str(sentence).lower()
    return sentence

# translation hindi to english
# def translation(text):
#     line = str(text)
#     translate = Translator()
#     result = translate.translate(line, 'en')
#     data = result.text
#     print(f"user said:{data}")
#     return data

# # translation("सत्यमेव जयते")
# # connecting listening and translation
# def MicExecution():
#     query = listen()
#     data = translation(query)  
#     return data

# MicExecution()


