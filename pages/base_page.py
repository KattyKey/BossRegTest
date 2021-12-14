import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from .locators import BasePageLocators
import random
import string


class BasePage():
    def __init__(self, browser, url, timeout=15):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def accept_browser_cookies(self,  tries = int(50), timelapse =0.1):
        for i in range(tries):
            time.sleep(timelapse)
            if self.frame_switch(BasePageLocators.BROWSER_COOKIES_FRAME) ==True:
                print("Element is found " + str(i))
                self.browser.find_element(*BasePageLocators.ASSEPT_BROWSER_COOKIES_BTN).click()
                self.browser.switch_to.parent_frame()
                break;
            else:
                time.sleep(timelapse)
                print("WAIT --------------1 "+str(i))
        assert("Cookies frame not found")

    def generate_random_word(self,wordlength):
        word=""
        for i in range(wordlength):
            word+=random.choice(string.ascii_letters)
        return word

    def frame_switch(self,element):
        try:
            self.browser.switch_to.frame(self.browser.find_element(*element))
            return True
        except Exception :
            return False
 