from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, browser):
        self.browser = browser

    def isTitleDisplayed(self, title):
        page_title = self.browser.find_element(By.ID, "headingText")
        assert page_title.text == title