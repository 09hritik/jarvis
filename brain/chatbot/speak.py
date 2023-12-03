#speaking function for jarvis
# windows based 
import pyttsx3
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

# inbuilt voice
def speak1(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[1].id)
    engine.setProperty('rate',150)
    print('')
    print(f"Jarvis:{text}")
    print('')
    engine.say(text)
    engine.runAndWait()

# online voice

chrome_options  = Options()
chrome_options.add_argument('--log-level=3')
chrome_options.headless = True
# path="drivers\\chromedriver.exe"
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

website = r"https://ttsmp3.com/text-to-speech/British%20English/"
driver.get(website)

XpathofSelect='//*[@id="sprachwahl"]'
ButtonSelection=Select(driver.find_element(by=By.XPATH,value=XpathofSelect))
ButtonSelection.select_by_visible_text('British English / Brian')

def speak2(text):
    lengthoftext=len(str(text))

    if lengthoftext==0:
        pass

    else:
        print("")
        print(f"Jarvis : {text}")
        print("")
        Data = str(text)
        Xpathoftextarea='//*[@id="voicetext"]'
        driver.find_element(By.XPATH,value=Xpathoftextarea).send_keys(Data)
        driver.find_element(By.XPATH,value='//*[@id="vorlesenbutton"]').click()
        driver.find_element(By.XPATH,value=Xpathoftextarea).clear()

        if lengthoftext>30:
            sleep(4)
        
        elif lengthoftext>=10:
            sleep(4)
        
        elif lengthoftext>=30:
            sleep(6)
        
        elif lengthoftext>=50:
            sleep(8)
        
        elif lengthoftext>=70:
            sleep(10)
        
        elif lengthoftext>=120:
            sleep(15)

        else:
            sleep(2)

# speak2("Hello Aryak")