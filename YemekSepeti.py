from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

class Yemeksepeti:
    def __init__(self, username, password):
        options = webdriver.ChromeOptions()
        # Uncomment the next line to run the browser in headless mode
        # options.add_argument("--headless")
        self.browser = webdriver.Chrome(options=options)
        self.username = username
        self.password = password

    def login(self):
        self.browser.get("https://www.yemeksepeti.com/kktc")
        self.browser.maximize_window()

        try:
            username_input = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.ID, "UserName"))
            )
            password_input = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.ID, "password"))
            )
            username_input.send_keys(self.username)
            password_input.send_keys(self.password)

            login_button = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.ID, "ys-fastlogin-button"))
            )
            login_button.click()
            print("Logged in successfully.")
        except TimeoutException:
            print("Error: Unable to locate login fields or button.")
            self.close_browser()
            return False
        except Exception as e:
            print(f"An unexpected error occurred during login: {e}")
            self.close_browser()
            return False

        # Wait for the page to load after login
        time.sleep(2)
        return True

    def select_city(self):
        try:
            city_selector = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/header/div/div/div/div[2]/span/span[1]/span/span[2]"))
            )
            city_selector.click()
            print("City selector clicked.")
        except TimeoutException:
            print("Error: Unable to locate city selector.")
            return False
        except Exception as e:
            print(f"An unexpected error occurred while selecting city: {e}")
            return False

        try:
            town_input = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id='ys-areaSelector-droparea']/span/span/span[1]/input"))
            )
            town_input.send_keys(Keys.ENTER)
            print("City selected.")
        except TimeoutException:
            print("Error: Unable to select city.")
            return False
        except Exception as e:
            print(f"An unexpected error occurred while selecting city: {e}")
            return False

        return True

    def search_food(self, food_item):
        try:
            search_input = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/header/div/div/div/div[4]/input"))
            )
            search_input.click()
            search_input.send_keys(food_item)
            search_input.send_keys(Keys.ENTER)
            print(f"Searched for '{food_item}'.")
        except TimeoutException:
            print("Error: Unable to locate search bar.")
            return False
        except Exception as e:
            print(f"An unexpected error occurred during search: {e}")
            return False

        return True

    def select_first_food(self):
        try:
            first_food = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/a/i"))
            )
            first_food.click()
            print("Selected the first food item.")
        except TimeoutException:
            print("Error: Unable to select the first food item.")
            return False
        except Exception as e:
            print(f"An unexpected error occurred while selecting food: {e}")
            return False

        return True

    def confirm_order(self):
        try:
            confirm_button = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='basket-container']/div[2]/div/div[5]/button"))
            )
            confirm_button.click()
            print("Order confirmed.")
        except TimeoutException:
            print("Order confirmation button not found. Trying alternative method...")
            try:
                alternative_confirm = WebDriverWait(self.browser, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[@id='cboxLoadedContent']/div/div[2]/div/div[2]/button"))
                )
                alternative_confirm.click()
                confirm_button = WebDriverWait(self.browser, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[@id='basket-container']/div[2]/div/div[5]/button"))
                )
                confirm_button.click()
                print("Order confirmed via alternative method.")
            except Exception as e:
                print(f"Failed to confirm order: {e}")
                return False
        except Exception as e:
            print(f"An unexpected error occurred during order confirmation: {e}")
            return False

        return True

    def select_payment_method(self):
        try:
            payment_option = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[8]/div/div/div/div/div[2]/div/div[2]/label/input"))
            )
            payment_option.click()
            print("Payment method selected.")
        except TimeoutException:
            print("Error: Unable to select payment method.")
            return False
        except Exception as e:
            print(f"An unexpected error occurred while selecting payment method: {e}")
            return False

        return True

    def order_food(self, food_item):
        if not self.login():
            return
        if not self.select_city():
            return
        if not self.search_food(food_item):
            return
        if not self.select_first_food():
            return
        if not self.confirm_order():
            return
        if not self.select_payment_method():
            return
        print("Food ordered successfully.")
        self.close_browser()

    def close_browser(self):
        self.browser.quit()
        print("Browser closed.")

if __name__ == "__main__":
    username = "your_username"     # Replace with your Yemeksepeti username
    password = "your_password"     # Replace with your Yemeksepeti password
    food_item = "pizza"            # Replace with the food item you want to order

    yemeksepeti = Yemeksepeti(username, password)
    yemeksepeti.order_food(food_item)
