from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

word_to_translate = input("Please enter the word to translate: ")

class Translator:
    def __init__(self):
        options = webdriver.ChromeOptions()
        # Uncomment the next line to run in headless mode
        # options.add_argument("--headless")
        self.browser = webdriver.Chrome(options=options)
    
    def translate_word(self, word):
        self.browser.get("https://translate.google.com/")
        self.browser.maximize_window()

        try:
            source_input = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//textarea[@aria-label='Source text']"))
            )
            source_input.send_keys(word)
        except TimeoutException:
            print("Error occurred while locating the source text area.")
            return

        try:
            target_language_button = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='More target languages']"))
            )
            target_language_button.click()

            turkish_option = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[text()='Turkish']"))
            )
            turkish_option.click()
        except TimeoutException:
            print("Error occurred while selecting the target language.")
            return

        try:
            translated_text = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//span[@jsname='W297wb']"))
            )
            print(f"Translated Text: {translated_text.text}")
        except TimeoutException:
            print("Error occurred while retrieving the translated text.")
    
    def close_browser(self):
        self.browser.quit()

translator = Translator()
translator.translate_word(word_to_translate)
translator.close_browser()

