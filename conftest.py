import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def browser(request):
    browser = webdriver.Chrome()

    yield browser
    print("\nquit browser..")
    browser.quit()

