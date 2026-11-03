from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    TITLE = (By.CSS_SELECTOR, ".title")
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_BIKE_LIGHT = (By.ID, "add-to-cart-sauce-labs-bike-light")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_until_loaded(self):
        self.wait.until(EC.url_contains("inventory.html"))
        self.wait.until(EC.visibility_of_element_located(self.TITLE))
        assert self.driver.find_element(*self.TITLE).text == "Products"

    def add_two_products(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_BACKPACK)).click()
        self.wait.until(EC.element_to_be_clickable(self.ADD_BIKE_LIGHT)).click()
        badge = self.wait.until(EC.visibility_of_element_located(self.CART_BADGE))
        assert badge.text == "2"

    def open_cart(self):
        self.driver.find_element(*self.CART_LINK).click()
