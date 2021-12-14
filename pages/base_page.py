import random
import string
import time

from .locators import BasePageLocators


class BasePage():
    def __init__(self, browser, url, timeout=15):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def accept_browser_cookies(self, tries=int(50), timelapse=0.1):
        '''
            Ожидание появления кукис и их подтверждение
        :param tries:  Количество попыток проверить возможность пперейти на фрейм
        :param timelapse: Время для вейта между попытками
        '''
        for i in range(int(tries)):
            if self.frame_switch(BasePageLocators.BROWSER_COOKIES_FRAME) == True:
                print("Element is found " + str(i))
                self.browser.find_element(*BasePageLocators.ASSEPT_BROWSER_COOKIES_BTN).click()
                self.browser.switch_to.parent_frame()
                break;
            else:
                time.sleep(timelapse)
                print("WAIT --------------1 " + str(i))
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
