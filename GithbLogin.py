from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class Github:
    def __init__(self, username, password):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        self.browser = webdriver.Chrome(options=options)
        self.username = username
        self.password = password

    def sign_in(self):
        self.browser.get("https://github.com/login")
        self.browser.maximize_window()
        try:
            username_input = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.ID, "login_field"))
            )
            password_input = self.browser.find_element(By.ID, "password")
            username_input.send_keys(self.username)
            password_input.send_keys(self.password)
            
            login_button = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.NAME, "commit"))
            )
            login_button.click()
        
        except TimeoutException:
            print("An error occurred while trying to log in.")
    
    def search_and_star_repo(self, repo_name):
        try:
            search_box = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.NAME, "q"))
            )
            search_box.send_keys(repo_name)
            search_box.submit()
            
            repo_link = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//ul[@class='repo-list']//a[contains(@href, '/" + repo_name + "')]"))
            )
            repo_link.click()
            
            star_button = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//form[contains(@action, 'star')]//button"))
            )
            star_button.click()
            print("Successfully starred the repository.")
        
        except TimeoutException:
            print("An error occurred while searching or starring the repository.")
    
    def close_browser(self):
        self.browser.quit()

if __name__ == "__main__":
    gitname = "your_username"
    gitpass = "your_password"
    repo_name = "repository_owner/repository_name"  # Example: "octocat/Hello-World"

    github = Github(gitname, gitpass)
    github.sign_in()
    time.sleep(3)  # wait for login to complete
    github.search_and_star_repo(repo_name)
    github.close_browser()
