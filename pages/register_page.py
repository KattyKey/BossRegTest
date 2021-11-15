import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from pages.locators import RegisterPageLocators

class RegisterPage(BasePage):

    def is_exist_register_button(self):
        assert self.browser.find_element(*RegisterPageLocators.REGISTRATION_FORM_OPEN_BTTN), "Register button is not found"

    def click_register_button(self):
        self.browser.find_element(*RegisterPageLocators.REGISTRATION_FORM_OPEN_BTTN).click()
