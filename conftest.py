from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    # locally
    # browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser
    browser.close()

@pytest.fixture()
def separator():
    # print('=' + 10) for error
    yield 'value'
    print('test finished')

@pytest.fixture(scope='session')
def all_tests():
    print('before all')
    yield
    print('After all')