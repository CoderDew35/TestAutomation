from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

class Twitter:
    def __init__(self, username, password):
        options = webdriver.ChromeOptions()
        # Uncomment the next line to run the browser in headless mode
        # options.add_argument("--headless")
        self.browser = webdriver.Chrome(options=options)
        self.username = username
        self.password = password

    def login(self):
        self.browser.get("https://twitter.com/login")
        self.browser.maximize_window()
        
        try:
            username_input = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.NAME, "text"))
            )
            username_input.send_keys(self.username)
            username_input.send_keys(Keys.ENTER)
            time.sleep(2)  # Wait for transition

            password_input = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.NAME, "password"))
            )
            password_input.send_keys(self.password)
            password_input.send_keys(Keys.ENTER)
        except TimeoutException:
            print("Failed to locate login fields.")
            self.close_browser()
            return False
        except Exception as e:
            print(f"An error occurred during login: {e}")
            self.close_browser()
            return False

        # Verify successful login by checking the presence of the home timeline
        try:
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a[@href='/home' and @aria-label='Home']"))
            )
            print("Successfully logged in to Twitter.")
            return True
        except TimeoutException:
            print("Login may have failed or took too long.")
            self.close_browser()
            return False

    def search_and_like_tweet(self, search_term):
        try:
            search_input = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Search query']"))
            )
            search_input.send_keys(search_term)
            search_input.send_keys(Keys.ENTER)
        except TimeoutException:
            print("Search input could not be found.")
            return

        # Wait for the search results to load
        try:
            # Navigate to the "Latest" tab to get the most recent tweets
            latest_tab = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Latest"))
            )
            latest_tab.click()
        except TimeoutException:
            print("'Latest' tab could not be clicked.")
            return

        # Wait for the latest tweets to load
        time.sleep(3)

        try:
            # Locate the first tweet in the list
            first_tweet = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//article[@role='article']"))
            )
            first_tweet.click()
        except TimeoutException:
            print("No tweets found for the search term.")
            return

        # Switch to the tweet's modal dialog
        try:
            like_button = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((
                    By.XPATH,
                    "//div[@data-testid='like']"
                ))
            )
            like_button.click()
            print(f"Liked a tweet containing '{search_term}'.")
        except TimeoutException:
            print("Like button could not be found or clicked.")
        except Exception as e:
            print(f"An error occurred while trying to like the tweet: {e}")

    def close_browser(self):
        self.browser.quit()

if __name__ == "__main__":
    username = "your_twitter_username"       # Replace with your Twitter username or email
    password = "your_twitter_password"       # Replace with your Twitter password
    search_term = "Your Song Name"           # Replace with the song or term you want to search

    twitter_bot = Twitter(username, password)
    if twitter_bot.login():
        twitter_bot.search_and_like_tweet(search_term)
    twitter_bot.close_browser()
