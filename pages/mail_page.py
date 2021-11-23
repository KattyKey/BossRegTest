import time
import re
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from pages.locators import MailPageLocators

class MailPage(BasePage):
    def open_message(self,timeout = 20):
        WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(MailPageLocators.MAILINATOR_OPEN_MESSAGE)).click()
        WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(MailPageLocators.MAILINATOR_OPEN_JSON_TEXT)).click()
        mail_text =self.browser.find_element(*MailPageLocators.MAILINATOR_GET_MAIL_CONTENT).text
        print(mail_text)
        print()
        print()
        mail_link = re.search(r'https://((\w+\.\w+\.\w+)|(\w+\.\w+))[/](\w{2}-\w{2,3}|\w{2,7})/verify/email/(\d+)[/](\w+)', mail_text)
        print(mail_link.group()	)
        return mail_link.group()