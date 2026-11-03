from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def verify_selected_items(self):
        items = self.wait.until(EC.visibility_of_all_elements_located(self.ITEMS))
        actual = {}
        for item in items:
            name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            price = item.find_element(By.CLASS_NAME, "inventory_item_price").text
            actual[name] = price
        assert actual == {
            "Sauce Labs Backpack": "$29.99",
            "Sauce Labs Bike Light": "$9.99"
        }

    def checkout(self):
        self.driver.find_element(*self.CHECKOUT).click()
