from playwright.sync_api import Page
from utils.captcha_solve import download_captcha_image, solve_captcha


class AmazonHomePage:
    def __init__(self, page: Page):
        self.page = page
    
    def navigate(self):
        self.page.goto("https://www.amazon.com")
        # Check if CAPTCHA is present
        """
        if self.page.is_visible('div.a-row.a-text-center img'):
            img = download_captcha_image(self.page)
            captcha_text = solve_captcha(img)
            print("CAPTCHA Text: ", captcha_text)
            
            # Fill in the CAPTCHA text and submit the form
            self.page.fill('input[name="field-keywords"]', captcha_text)
            self.page.click('input[type="submit"]')
        """    

    def search_product(self, product_name: str):
        self.page.fill('input[name="field-keywords"]', product_name)
        self.page.click('input[type="submit"]')