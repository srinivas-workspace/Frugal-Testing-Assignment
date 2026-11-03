# Frugal Testing Assignment 1 – Python

## Stack
Python + Selenium + pytest + requests.

## Setup (Windows)
1. Install Python 3.10+ and Google Chrome.
2. Open this folder in VS Code.
3. Open Terminal and run:
   `python -m venv .venv`
   `.venv\Scripts\activate`
   `python -m pip install -r requirements.txt`

## Run
- UI tests: `pytest tests/test_ui_saucedemo.py --html=reports/ui-report.html --self-contained-html`
- API tests: `pytest tests/test_api_restful_booker.py --html=reports/api-report.html --self-contained-html`
- All tests: `pytest --html=reports/full-report.html --self-contained-html`

Selenium Manager (included with Selenium 4.6+) automatically manages ChromeDriver.
Screenshots on failed tests are saved in `screenshots/`.

## SauceDemo credentials
- standard_user / secret_sauce
- locked_out_user / secret_sauce

## Important
Run the tests yourself before submission. Public practice services can occasionally be unavailable.
Check every assertion and be ready to explain the code. Do not claim a test passed unless your own run confirms it.
