
from conftest import browser
from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get("https://cloud.google.com/ai/generative-ai?hl=en")

    def clickOnStartBtn(self):
        start_btn = self.browser.find_element(By.CSS_SELECTOR, "[aria-label='Get started for free']")
        start_btn.click()