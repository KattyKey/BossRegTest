import pytest
import time
from pages.register_page import RegisterPage
from pages.mail_page import MailPage
from pages.admin_page import WorkWithAdminPage
from pages.variables import TestRegisterPageVariables, AdminPageVariables


def test_accept_browser_cokies(browser):
    page = RegisterPage(browser, TestRegisterPageVariables.link)
    page.accept_browser_cookies()


def test_open_register_form(browser):
    page = RegisterPage(browser, TestRegisterPageVariables.link)
    page.open_and_accept_browser_cookies()
    page.click_register_button()


def test_registration_first_step(browser):
    page = RegisterPage(browser, TestRegisterPageVariables.link)  # Открываем ссылку и принимаем куки
    page.open()
    page.accept_browser_cookies()
    page.click_register_button()
    page.fill_first_step(str(time.time()) + "@mailinator.com", "Qwerty78+", page.generate_random_word(5),
                         page.generate_random_word(5), "10101990", 1)
    page.click_submit_first_step()
    time.sleep(500)


@pytest.mark.current_task
def test_registration_second_step(browser, config):
    reg_scenario = ""
    if config['platform'] == "dev":
        link = TestRegisterPageVariables.dev_link
        reg_scenario = "Email or Telephone"
    else:
        link = TestRegisterPageVariables.prod_link

    page = RegisterPage(browser, link)  # Открываем ссылку и принимаем куки
    page.open()
    page.accept_browser_cookies()
    page.click_register_button()
    page.fill_first_step(str(time.time()) + "@mailinator.com", "Qwerty78+", page.generate_random_word(5),
                         page.generate_random_word(5), "10101990", 1)
    page.click_submit_first_step()
    page.fill_second_step(page.generate_random_word(5), "TEST", "test", str(time.time())[:10],reg_scenario)
    time.sleep(10)


def test_registration_full(browser):
    reg_mail = MailPage().generate_random_email(TestRegisterPageVariables.email)
    print(reg_mail)
    MailPage().clear_mailbox(TestRegisterPageVariables.email,
                             TestRegisterPageVariables.email_password)  # Очищаем почту от сообщений

    page = RegisterPage(browser, TestRegisterPageVariables.link)  # Открываем ссылку и принимаем куки
    page.open()
    page.accept_browser_cookies()

    page.click_register_button()
    page.fill_first_step(reg_mail, "Qwerty78+", page.generate_random_word(5), page.generate_random_word(5), "10101990",
                         1)
    page.click_submit_first_step()
    page.fill_second_step(page.generate_random_word(5), "TEST", "test", str(time.time())[:10])
    validation_link = MailPage().get_link_from_message(TestRegisterPageVariables.email,
                                                       TestRegisterPageVariables.email_password)

    new_page = RegisterPage(browser, str(validation_link))
    new_page.open()
    new_page.click_reg_done_button()
    WorkWithAdminPage().switch_user_to_test(AdminPageVariables.admin_user_login, AdminPageVariables.admin_user_password,
                                            reg_mail)

    time.sleep(50)
