import pytest
from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync

from pages.amazon_home_page import AmazonHomePage
from pages.product_page_ import ProductPage
from pages.basket_page import BasketPage


@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


def test_shopping_experience(browser):
    page = browser.new_page()

    stealth_sync(page)

    print("Please solve the CAPTCHA in the opened browser...")
    page.pause()

    amazon_home = AmazonHomePage(page)

    
    product_page = ProductPage(page)
    basket_page = BasketPage(page)

    amazon_home.navigate()
    amazon_home.search_product("laptop")

    product_page.click_first_product()
    product_page.add_to_basket()

    basket_page.navigate()
    basket_page.update_quantity(2)

    assert basket_page.get_quantity() == "2"
