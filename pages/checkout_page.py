from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    FIRST = (By.ID, "first-name")
    LAST = (By.ID, "last-name")
    POSTAL = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    ERROR = (By.CSS_SELECTOR, "[data-test='error']")
    FINISH = (By.ID, "finish")
    COMPLETE = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_details(self, first, last, postal):
        self.wait.until(EC.visibility_of_element_located(self.FIRST)).send_keys(first)
        self.driver.find_element(*self.LAST).send_keys(last)
        self.driver.find_element(*self.POSTAL).send_keys(postal)
        self.driver.find_element(*self.CONTINUE).click()

    def error_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.ERROR)).text

    def totals(self):
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "summary_info")))
        item_total = float(self.driver.find_element(By.CLASS_NAME, "summary_subtotal_label").text.split("$")[1])
        tax = float(self.driver.find_element(By.CLASS_NAME, "summary_tax_label").text.split("$")[1])
        total = float(self.driver.find_element(By.CLASS_NAME, "summary_total_label").text.split("$")[1])
        return item_total, tax, total

    def finish_order(self):
        self.driver.find_element(*self.FINISH).click()
        return self.wait.until(EC.visibility_of_element_located(self.COMPLETE)).text
