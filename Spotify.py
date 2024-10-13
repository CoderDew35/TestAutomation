from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class Spotify:
    def __init__(self, username, password):
        options = webdriver.ChromeOptions()
        # Uncomment the next line to run the browser in headless mode
        # options.add_argument("--headless")
        self.browser = webdriver.Chrome(options=options)
        self.username = username
        self.password = password

    def login(self):
        self.browser.get("https://www.spotify.com/login/")
        self.browser.maximize_window()
        try:
            login_button = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Log in with Facebook')]"))
            )
            login_button.click()
        except TimeoutException:
            print("Login with Facebook button could not be clicked.")
            return

        try:
            email_input = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.ID, "email"))
            )
            password_input = self.browser.find_element(By.ID, "pass")
            email_input.send_keys(self.username)
            password_input.send_keys(self.password)
        except TimeoutException:
            print("Facebook login fields could not be found.")
            return

        try:
            fb_login_button = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.NAME, "login"))
            )
            fb_login_button.click()
        except TimeoutException:
            print("Facebook login button could not be clicked.")
            return

        # Wait for Spotify to redirect after login
        try:
            WebDriverWait(self.browser, 15).until(
                EC.presence_of_element_located((By.XPATH, "//button[@data-testid='play-button']"))
            )
            print("Successfully logged in to Spotify.")
        except TimeoutException:
            print("Login may have failed or took too long.")

    def search_song(self, song_name):
        try:
            search_icon = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='search-button']"))
            )
            search_icon.click()
        except TimeoutException:
            print("Search icon could not be clicked.")
            return

        try:
            search_input = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@data-testid='search-input']"))
            )
            search_input.send_keys(song_name)
            search_input.send_keys(Keys.ENTER)
        except TimeoutException:
            print("Search input could not be found.")
            return

        # Wait for search results to load
        time.sleep(3)

    def select_song_and_add_to_favorites(self, song_name):
        try:
            # Locate the song in the search results
            song_link = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//span[text()='{song_name}']/ancestor::div[@role='button']"))
            )
            song_link.click()
        except TimeoutException:
            print(f"Song '{song_name}' could not be found in search results.")
            return

        # Wait for the song page to load
        time.sleep(3)

        try:
            # Click on the "Save to Your Library" button
            save_button = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='add-button']"))
            )
            save_button.click()
            print(f"'{song_name}' has been added to your favorites.")
        except TimeoutException:
            print("Save to Your Library button could not be clicked.")

    def close_browser(self):
        self.browser.quit()

if __name__ == "__main__":
    username = "your_facebook_email@example.com"  # Replace with your Facebook email
    password = "your_facebook_password"           # Replace with your Facebook password
    song_name = "Shape of You"                    # Replace with the song you want to add to favorites

    spotify = Spotify(username, password)
    spotify.login()
    time.sleep(5)  # Wait for login to complete and redirect
    spotify.search_song(song_name)
    spotify.select_song_and_add_to_favorites(song_name)
    spotify.close_browser()
