import json
from pathlib import Path
import pytest
from selenium import webdriver

BASE = Path(__file__).resolve().parents[1]

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=options)  # Selenium Manager handles driver setup
    yield browser
    browser.quit()

@pytest.fixture
def login_cases():
    with open(BASE / "data" / "login_cases.json", encoding="utf-8") as f:
        return json.load(f)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        browser = item.funcargs.get("driver")
        if browser:
            folder = BASE / "screenshots"
            folder.mkdir(exist_ok=True)
            browser.save_screenshot(str(folder / f"{item.name}.png"))
