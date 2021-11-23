import pytest
import time
from pages.register_page import RegisterPage
from pages.mail_page import MailPage

link = "https://dev.bosscasino.com/registration"
mail_link = "https://www.mailinator.com/v4/public/inboxes.jsp?to="

def test_accept_browser_cokies(browser):
    page = RegisterPage(browser,link)
    page.accept_browser_cookies()

def test_open_register_form(browser):
    page = RegisterPage(browser,link)
    page.open_and_accept_browser_cookies()
    page.click_register_button()

def test_click_submit_with_empty_fields(browser):
    page = RegisterPage(browser,link)
    page.open_and_accept_browser_cookies()
    page.click_register_button()
    page.click_submit_first_step()

def test_registration_first_step(browser):
    page = RegisterPage(browser,link)
    page.open_and_accept_browser_cookies()
    page.click_register_button()
    page.fill_first_step(str(time.time())+"@mailinator.com","Qwerty78+",RandomWords().get_random_word(),RandomWords().get_random_word(),"10101990",1)
    page.click_submit_first_step()
    
@pytest.mark.current_task
def test_registration_second_step(browser):
    email = str(time.time()) +"@mailinator.com"
    page = RegisterPage(browser,link)
    page.open()
    page.accept_browser_cookies()
    page.click_register_button()
    page.fill_first_step(email, "Qwerty78+",page.generate_random_word(5),page.generate_random_word(5), "10101990", 1)
    page.click_submit_first_step()
    page.fill_second_step(page.generate_random_word(5) ,"TEST","test",str(time.time())[:10])
    mail_page = MailPage(browser,mail_link+email)
    mail_page.open()
    validation_link =mail_page.open_message()
    new_page = RegisterPage(browser, str(validation_link))
    new_page.open()
    new_page.click_reg_done_button()
    time.sleep(50)
    