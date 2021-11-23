from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from .locators import BasePageLocators
import random
import string


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def accept_browser_cookies(self, timeout = 10):
        WebDriverWait(self.browser, timeout).until(EC.frame_to_be_available_and_switch_to_it((BasePageLocators.BROWSER_COOKIES_FRAME)))
        self.browser.find_element(*BasePageLocators.ASSEPT_BROWSER_COOKIES_BTN).click()
        self.browser.switch_to.parent_frame()
        
    def open_and_accept_browser_cookies(self):
        self.browser.get(self.url)
        self.accept_browser_cookies()

    def generate_random_word(self,wordlength):
        word=""
        for i in range(wordlength):
            word+=random.choice(string.ascii_letters)
        return word
 