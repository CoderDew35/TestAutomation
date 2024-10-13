# test-automation-scripts
This repository contains an automated test suite for simulating an online shopping experience on Amazon. The tests are implemented using Pytest and Playwright, leveraging the Page Object Model (POM) for better maintainability and scalability. The test scenario covers searching for a product, adding it to the basket, and updating the quantity of the item to ensure a seamless user experience.

amazon_home_page.py: Contains the HomePage class with methods for interacting with Amazon's home page elements.

basket_page.py: Contains the BasketPage class, which provides methods for managing items in the basket, such as reviewing, updating quantities, and verifying the basket contents.

product_page.py: Contains the ProductPage class, which includes methods for interacting with the product detail page.

test_shopping.py: Implements the test case for searching a product, adding it to the basket, and updating the quantity.


