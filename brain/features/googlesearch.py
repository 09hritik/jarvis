from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


chrome_options = Options()
chrome_options.add_argument('--log-leevels=0')
chrome_options.headless = False
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

website = r"https://www.google.com/"
driver.get(website)

XPATH_of_text_area='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea'

def hot_words_detection(sentence, keywords):
    extracted_results = {}
    for keyword in keywords:
        index = sentence.find(keyword)
        if index != -1:
            extracted_text = sentence[index + len(keyword):].strip()
            extracted_results[keyword] = extracted_text
    return extracted_results

# Example usage
sentence = "Search OpenAI's GPT-3 on "
keywords = ["Search", "google"]
results = hot_words_detection(sentence, keywords)

for keyword, result in results.items():
    if result:
        print(f"Extracted after '{keyword}': {result}")
        data = str(result)
        driver.find_element(By.XPATH,value=XPATH_of_text_area).send_keys(result)
        driver.find_element(By.XPATH,value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]').click()
    else:
        print(f"'{keyword}' not found.")
    
data = str(result)
driver.find_element(By.XPATH,value=XPATH_of_text_area).send_keys(result)
driver.find_element(By.XPATH,value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]').click()
