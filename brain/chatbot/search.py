import re
# import pywhatkit
import wikipedia
from pywikihow import WikiHow , search_wikihow
from time import sleep
from speak import speak2
from speak import speak1
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def clean_query(query):
    # Remove common keywords like 'search', 'play', 'on youtube', etc. (case-insensitive)
    keywords_to_remove = ['search', 'play', 'on Youtube', 'youtube','what is the meaning of','what does','what is','who is']
    for keyword in keywords_to_remove:
        query = re.sub(r'\b' + re.escape(keyword) + r'\b', '', query, flags=re.IGNORECASE).strip()
    return query

def youtueSearch_and_play(query):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument('--log-level=0')

    # Provide the correct path to your ChromeDriver executable
    chrome_driver_path = 'path/to/chromedriver'
    driver = webdriver.Chrome(options=chrome_options)

    query = clean_query(query)
    if query:
        youtube_url = "https://www.youtube.com/results?search_query=" + query
        driver.get(youtube_url)

        sleep(10)  # Wait for search results to load

        # Use explicit wait to wait for the first video link to be available
        wait = WebDriverWait(driver, 10)
        first_video = wait.until(EC.presence_of_element_located((By.ID, 'video-title')))
        first_video.click()

        sleep(5)  # Wait for the video to play (adjust the duration as needed)

        speak2("Playing the first video on YouTube related to: " + query)
    else:
        speak2("I'm sorry, I didn't catch what you want to search on YouTube.")

def GoogleSearch(term):
    query = clean_query(term)
    if query:
        try:
            search_summary = wikipedia.summary(query)
            speak2("Here's a summary:")
            speak2(search_summary)
        except wikipedia.exceptions.DisambiguationError as e:
            speak2("It seems like there are multiple meanings for the query. Please provide more context.")
        except wikipedia.exceptions.PageError as e:
            speak2("I couldn't find a Wikipedia article related to the query.")
    else:
        speak2("I'm sorry, I didn't catch the query properly.")
    # if query:
    #     google_url = "https://www.google.com/search?q=" + query
    #     speak2("Here's what I found on Google for: " + query)
    # else:
    #     speak2("I'm sorry, I didn't catch what you want to search on Google.")

# Test the function
# youtueSearch_and_play("play Shiv tandav stotram on youtube")
