import pytest
from selenium import webdriver
import json

@pytest.fixture(scope="function")
def browser(request):
    browser = webdriver.Chrome()

    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(scope='session')
def config():
  with open('config.json') as config_file:
    data = json.load(config_file)
  return data