from base_page import BasePage
from locators.locators_register import RegisterPageLocators


class RegisterPage(BasePage):

    def click_register_button(self, timeout=15):
        self.wait_n_click_element(RegisterPageLocators.REGISTRATION_FORM_OPEN_BTTN)

    def click_reg_done_button(self, timeout=25):
        self.wait_n_click_element(RegisterPageLocators.REGISTRATION_DONE_BTTN)

    def click_submit_first_step(self):
        self.browser.find_element(*RegisterPageLocators.SUBMIT_FIRST_STEP_BTTN).click()

    def click_submit_second_step(self):
        self.browser.find_element(*RegisterPageLocators.SUBMIT_SECOND_STEP_BTTN).click()

    def fill_first_step(self, email, password, firstname, lastname, dob, gender):
        self.browser.find_element(*RegisterPageLocators.FIELD_EMAIL).send_keys(email)
        self.browser.find_element(*RegisterPageLocators.FIELD_PASSWORD).send_keys(password)
        self.browser.find_element(*RegisterPageLocators.FIELD_FIRSTNAME).send_keys(firstname)
        self.browser.find_element(*RegisterPageLocators.FIELD_LASTNAME).send_keys(lastname)
        self.browser.find_element(*RegisterPageLocators.FIELD_DOB).send_keys(dob)
        if gender == 1:
            self.browser.find_element(*RegisterPageLocators.SELECT_GENDER_M).click()
        else:
            self.browser.find_element(*RegisterPageLocators.SELECT_GENDER_F).click()

    def fill_second_step(self, address, city, zip, phone, reg_scenario):
        self.browser.find_element(*RegisterPageLocators.SELECT_COUNTRY).click()
        self.browser.find_element(*RegisterPageLocators.FIND_COUNTRY).click()
        self.browser.find_element(*RegisterPageLocators.FIELD_ADDRESS).send_keys(address)
        self.browser.find_element(*RegisterPageLocators.FIELD_CITY).send_keys(city)
        self.browser.find_element(*RegisterPageLocators.FIELD_ZIP).send_keys(zip)
        self.browser.find_element(*RegisterPageLocators.FIELD_PHONE).send_keys(phone)
        self.browser.find_element(*RegisterPageLocators.CHECK_CONFIRM_AGE).click()
        self.browser.find_element(*RegisterPageLocators.CHECK_ACCEPT_TERMS).click()
        if reg_scenario == "Email or Telephone":
            self.browser.find_element(*RegisterPageLocators.CHECK_EMAIL_ACTIVATION).click()


