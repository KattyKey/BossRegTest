import pytest
import time
from pages.register_page import RegisterPage

link = "https://dev.bosscasino.com/registration"


def test_accept_browser_cokies(browser):
    page = RegisterPage(browser,link)
    page.accept_browser_cookies()

def test_open_register_form(browser):
    page = RegisterPage(browser,link)
    page.open_and_accept_browser_cookies()
    page.click_register_button()
    
#@pytest.mark.xfail

def test_click_submit_with_empty_fields(browser):
    page = RegisterPage(browser,link)
    page.open_and_accept_browser_cookies()
    page.click_register_button()
    #page.go_to_register_form()
    page.click_submit_first_step()


def test_registration_first_step(browser):
    page = RegisterPage(browser,link)
    page.open_and_accept_browser_cookies()
    page.click_register_button()
    page.fill_first_step(str(time.time())+"@mailinator.com","Qwerty78+","jhh","jhgbjtgj","10101990",1)
    page.click_submit_first_step()
    
@pytest.mark.current_task
def test_registration_second_step(browser):
    page = RegisterPage(browser,link)
    page.open_and_accept_browser_cookies()
    page.click_register_button()
    page.fill_first_step(str(time.time()) +"@mailinator.com", "Qwerty78+", "jhh", "jhgbjtgj", "10101990", 1)
    page.click_submit_first_step()
    page.fill_second_step("Malta","jtggy","guyg","5485468")
    time.sleep(10)
    