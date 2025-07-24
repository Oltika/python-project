from pages.homepage import HomePage
from pages.loginpage import LoginPage
from conftest import browser

def test_open_s6(browser):
    home_page = HomePage(browser)
    home_page.open()
    home_page.clickOnStartBtn()

    login_page = LoginPage(browser)
    login_page.isTitleDisplayed('Sign in')