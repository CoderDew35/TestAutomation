from playwright.sync_api import Page


class ProductPage:
    def __init__(self, page: Page):
        self.page = page

    def click_first_product(self): 
        self.page.click('div.s-main-slot div[data-component-type="s-search-result"] h2 a')


    def add_to_basket(self):
        self.page.click('#add-to-cart-button')