import random
import string
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import logging
from locators.locators_register import BasePageLocators, RegisterPageLocators


class BasePage():
    def __init__(self, browser, url,wait_time = 10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(wait_time)

    def open(self):
        self.browser.get(self.url)

    def accept_browser_cookies(self, tries=50, timelapse=0.1):
        '''
            Ожидание появления кукис и их подтверждение
        :param tries:  Количество попыток проверить возможность перейти на фрейм
        :param timelapse: Время для вейта между попытками
        '''
        for i in range(int(tries)):
            if self.frame_switch(BasePageLocators.BROWSER_COOKIES_FRAME) == True:
                logging.info("Element is found " + str(i))
                self.browser.find_element(*BasePageLocators.ASSEPT_BROWSER_COOKIES_BTN).click()
                self.browser.switch_to.parent_frame()
                break;
            else:
                time.sleep(timelapse)
                logging.info("WAIT --------------1 " + str(i))
        assert ("Cookies frame not found")


    def generate_random_word(self, wordlength):
        '''
        :param wordlength: Длинна слова для генерации
        :return: Слово состоящее из набора случайных букв
        '''
        word = ""
        for i in range(wordlength):
            word += random.choice(string.ascii_letters)
        return word

    def frame_switch(self, element):
        '''
        :param element: Локатор фрейма
        :return: Булевое значение в зависимости от того вышло ли переключится на фрейм
        '''
        try:
            self.browser.switch_to.frame(self.browser.find_element(*element))
            return True
        except Exception:
            return False



