from pages.homepage import HomePage
from pages.loginpage import LoginPage
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options

# temp solution
@pytest.fixture()
def init_browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser
    browser.close()


def test_open_s6(init_browser):
    home_page = HomePage(init_browser)
    home_page.open()
    home_page.clickOnStartBtn()

    login_page = LoginPage(init_browser)
    login_page.isTitleDisplayed('Sign in')

