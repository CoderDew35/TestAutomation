from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Facebook:
    
    def __init__(self, email, password):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        self.browser = webdriver.Chrome(options=options)
        self.email = email
        self.password = password

    def sign_in(self):
        self.browser.get("https://www.facebook.com/login/")
        
        try:
            email_input = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.ID, "email"))
            )
            password_input = self.browser.find_element(By.ID, "pass")
            email_input.send_keys(self.email)
            password_input.send_keys(self.password)
            
            login_button = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.NAME, "login"))
            )
            login_button.click()
            self.check_login_status()
        
        except TimeoutException:
            print("An error occurred while loading the page or locating elements.")
        
        except Exception as e:
            print(f"An error occurred: {e}")
        
    def check_login_status(self):
        try:
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Feed')]"))
            )
            print("Successfully logged in.")
        except TimeoutException:
            print("Login failed. Please check your email and password.")
        
    def close_browser(self):
        self.browser.quit()

if __name__ == "__main__":
    email = "your_email@example.com"
    password = "your_password"

    fb = Facebook(email, password)
    fb.sign_in()
    fb.close_browser()
