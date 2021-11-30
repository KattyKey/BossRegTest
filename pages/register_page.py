
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from pages.locators import RegisterPageLocators
import time

class RegisterPage(BasePage):
    def click_register_button(self,timeout = 15):
        WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(RegisterPageLocators.REGISTRATION_FORM_OPEN_BTTN)).click()
     
    def click_submit_first_step(self):
        self.browser.find_element(*RegisterPageLocators.SUBMIT_FIRST_STEP_BTTN).click()
        
    def click_reg_done_button(self,timeout = 25):
        WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(RegisterPageLocators.REGISTRATION_DONE_BTTN)).click()

    def fill_first_step(self,email,password,firstname,lastname,dob,gender):
        self.browser.find_element(*RegisterPageLocators.FIELD_EMAIL).send_keys(email)
        self.browser.find_element(*RegisterPageLocators.FIELD_PASSWORD).send_keys(password)
        self.browser.find_element(*RegisterPageLocators.FIELD_FIRSTNAME).send_keys(firstname)
        self.browser.find_element(*RegisterPageLocators.FIELD_LASTNAME).send_keys(lastname)
        self.browser.find_element(*RegisterPageLocators.FIELD_DOB).send_keys(dob)
        if gender==1:
            self.browser.find_element(*RegisterPageLocators.SELECT_GENDER_M).click()
        else:
            self.browser.find_element(*RegisterPageLocators.SELECT_GENDER_F).click()

    def fill_second_step(self,address,city,zip, phone):
        self.browser.find_element(*RegisterPageLocators.SELECT_COUNTRY).click()
        self.browser.find_element(*RegisterPageLocators.SELECT_COUNTRY_ID).click()
        self.browser.find_element(*RegisterPageLocators.FIELD_ADDRESS).send_keys(address)
        self.browser.find_element(*RegisterPageLocators.FIELD_CITY).send_keys(city)
        self.browser.find_element(*RegisterPageLocators.FIELD_ZIP).send_keys(zip)
        self.browser.find_element(*RegisterPageLocators.FIELD_PHONE).send_keys(phone)
        self.browser.find_element(*RegisterPageLocators.CHECK_CONFIRM_AGE).click()
        self.browser.find_element(*RegisterPageLocators.CHECK_ACCEPT_TERMS).click()
        self.browser.find_element(*RegisterPageLocators.CHECK_EMAIL_ACTIVATION).click()
        self.browser.find_element(*RegisterPageLocators.SUBMIT_SECOND_STEP_BTTN).click()

        
    