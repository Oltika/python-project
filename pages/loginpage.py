
from selenium.webdriver.common.by import By
from conftest import browser


class LoginPage:

    def __init__(self, browser):
        self.browser = browser

    def isTitleDisplayed(self, title):
        self.browser.implicitly_wait(5)
        sign_in_title = self.browser.find_element(By.ID, "headingText")
        assert sign_in_title.text == title