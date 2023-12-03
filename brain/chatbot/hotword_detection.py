import os
import subprocess
import speech_recognition as sr
from listen import listen

def run_chatbot():
    folder_path = "/home/hritik/transfer/jarvis/brain/chatbot"
    chatbot_script_path = os.path.join(folder_path, "chatbot.py")
    subprocess.run(["python", chatbot_script_path])

def main():
    while True:
        wake_up = listen()

        if wake_up == 'wake up':
            run_chatbot()
        else:
            print("Nothing")

if __name__ == "__main__":
    main()
