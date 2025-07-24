from selenium import webdriver
from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get("https://cloud.google.com/ai/generative-ai?hl=en")

    def clickOnStartBtn(self):
        startBtn = self.browser.find_element(By.CSS_SELECTOR, "[aria-label='Get started for free']")
        startBtn.click()