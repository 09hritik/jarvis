
import random
import json
import pickle
import numpy as np
import nltk
# import pywhatkit
# import wikipedia
# import os
import webbrowser as web
from search import youtueSearch_and_play
from search import GoogleSearch
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model #ignore warning
from listen import listen
from speak import speak2
from speak import speak1
from datetime import datetime
from time import sleep
from pywikihow import WikiHow , search_wikihow
from face_recognition_app import verify_face



lemmatizer = WordNetLemmatizer()

# Load intents
intents_path = "/home/hritik/transfer/jarvis/brain/Json/intents.json"
intents = json.loads(open(intents_path).read())

# Load model and preprocessing data
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbot_model.keras')

# Initialize responses for small talk
small_talk_responses = ["I'm here to help!", "Ask me anything!", "Let's chat!", "How can I assist you today?"]

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    lemmatized_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return lemmatized_words

def bag_of_words(sentence, words):
    sentence_words = clean_up_sentence(sentence)
    bag = [1 if w in sentence_words else 0 for w in words]
    return np.array(bag)

def predict_class(sentence):
    p = bag_of_words(sentence, words)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = [{'intent': classes[r[0]], 'probability': str(r[1])} for r in results]
    return return_list

def get_random_response(responses):
    return random.choice(responses)


def chat():
    print("Jarvis:", random.choice(small_talk_responses))
    verify_face("/home/hritik/transfer/jarvis/brain/features/photos/hritik.jpeg")
    while True:
        message = listen()
        if message == 'shutdown':
            speak2("Goodbye!")
            break
            
        intents_list = predict_class(message)
        if not intents_list:
            speak2("I'm sorry, I didn't understand that.")
            continue
        
        intent = intents_list[0]['intent']
        responses = [intent_data['responses'] for intent_data in intents['intents'] if intent_data['tag'] == intent]
        
        if responses:
            intent_response = get_random_response(responses[0])
            print("Jarvis:", intent_response)
            speak2(intent_response)
            
            if intent == "youtube":
                youtueSearch_and_play(message)
                sleep(20)

            elif intent == "google":
                GoogleSearch(message)
                sleep(20)
        
    
if __name__ == "__main__":
    print("Jarvis is running! ")
    chat()

