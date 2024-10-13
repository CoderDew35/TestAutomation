from playwright.sync_api import Page

class BasketPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto("https://www.amazon.com/gp/cart/view.html")

    def update_quantity(self, quantity: int):
        self.page.select_option('select[name="quantity"]', str(quantity))

    def get_quantity(self):
        return self.page.input_value('select[name="quantity"]')