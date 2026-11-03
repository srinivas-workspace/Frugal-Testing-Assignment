from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def login_standard(driver):
    LoginPage(driver).open().login("standard_user", "secret_sauce")
    inventory = InventoryPage(driver)
    inventory.wait_until_loaded()
    return inventory

def test_login_happy_path(driver):
    login_standard(driver)
    assert driver.current_url.endswith("inventory.html")
    assert driver.find_element(By.CLASS_NAME, "title").text == "Products"

def test_login_negative_cases(driver, login_cases):
    page = LoginPage(driver)
    for case in login_cases:
        page.open()
        page.login(case["username"], case["password"])
        assert page.error_message() == case["expected"]

def test_cart_two_products_and_checkout(driver):
    inventory = login_standard(driver)
    inventory.add_two_products()
    inventory.open_cart()

    cart = CartPage(driver)
    cart.verify_selected_items()
    cart.checkout()

    checkout = CheckoutPage(driver)
    checkout.enter_details("Srinivas", "Rao", "522001")
    item_total, tax, total = checkout.totals()
    assert round(item_total + tax, 2) == round(total, 2)
    assert checkout.finish_order() == "Thank you for your order!"

def test_checkout_empty_first_name(driver):
    login_standard(driver).add_two_products()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    CartPage(driver).checkout()

    checkout = CheckoutPage(driver)
    checkout.enter_details("", "Rao", "522001")
    assert checkout.error_message() == "Error: First Name is required"
