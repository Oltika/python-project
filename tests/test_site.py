from pages.homepage import HomePage
from pages.loginpage import LoginPage

def test_open_s6(init_browser):
    home_page = HomePage(init_browser)
    home_page.open()
    home_page.clickOnStartBtn()

    login_page = LoginPage(init_browser)
    login_page.isTitleDisplayed('Sign in')

