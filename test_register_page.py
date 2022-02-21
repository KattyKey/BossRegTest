import pytest
import time
from pages.bosscasino.register_page import RegisterPage
from helpers.mailbox_functions import Mailbox
from rest_api.admin_requests import AdminRequest
from variables.bosscasino_variables import TestRegisterPageVariables
from variables.admin_variables import  AdminRequestsVariables

'''
Запуск теста регистрации
pytest -k test_registration_full

'''


def test_registration_first_step(browser):
    '''
       ТЕСТ Заполнение первого шага
       Проверяем прописаные в конфиге параметры и в зависимости от них формируем линку, если это дев, прописываем сценарий регистрации
       Открываем страницу, принемаем куки
       Запускаем регистрацию, заполняем шаг
    '''
    page = RegisterPage(browser, TestRegisterPageVariables.link)  # Открываем ссылку и принимаем куки
    page.open()
    page.accept_browser_cookies()
    page.click_register_button()
    page.fill_first_step(str(time.time()) + "@mailinator.com", "Qwerty78+", page.generate_random_word(5),
                         page.generate_random_word(5), "10101990", 1)
    page.click_submit_first_step()



def test_registration_second_step(browser, config):
    '''
       ТЕСТ Заполнение первых двух шагов
       Проверяем прописаные в конфиге параметры и в зависимости от них формируем линку, если это дев, прописываем сценарий регистрации
       Открываем страницу, принемаем куки
       Запускаем регистрацию, заполняем оба шага
    '''
    reg_mail = Mailbox().generate_random_email(TestRegisterPageVariables.email)
    print(reg_mail)
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
    page.fill_first_step(reg_mail, "Qwerty78+", page.generate_random_word(5), page.generate_random_word(5), "10101990",
                         1)
    page.click_submit_first_step()
    page.fill_second_step(page.generate_random_word(5), "TEST", "test", str(time.time())[:10], reg_scenario)



#@pytest.mark.current_test
def test_registration_full(browser, config):
    '''
    Очищаем почту от сообщений
    Проверяем прописаные в конфиге параметры и в зависимости от них формируем линку, если это дев, прописываем сценарий регистрации
    Открываем страницу, принемаем куки
    Запускаем регистрацию, заполняем оба шага
    Получаем ссылку валидации с почты
    Переходим по ссылке и завершаем регистрацию
    Отмечаем юзера как тестового через админку
    '''

    reg_mail = Mailbox().generate_random_email(TestRegisterPageVariables.email)
    print(reg_mail)
    Mailbox().clear_mailbox(TestRegisterPageVariables.email,
                            TestRegisterPageVariables.email_password)

    reg_scenario = ""
    if config['platform'] == "dev":
        link = TestRegisterPageVariables.dev_link
        reg_scenario = "Email or Telephone"
    else:
        link = TestRegisterPageVariables.prod_link
    page = RegisterPage(browser, link)
    page.open()
    page.accept_browser_cookies()

    page.click_register_button()
    page.fill_first_step(reg_mail, "Qwerty78+", page.generate_random_word(5), page.generate_random_word(5), "10101990",
                         1)
    page.click_submit_first_step()
    page.fill_second_step(page.generate_random_word(5), "TEST", "test", str(time.time())[:10], reg_scenario)
    page.click_submit_second_step()
    validation_link = Mailbox().get_link_from_message(TestRegisterPageVariables.email,
                                                      TestRegisterPageVariables.email_password)
    new_page = RegisterPage(browser, str(validation_link))
    new_page.open()
    new_page.click_reg_done_button()
    AdminRequest().select_platform(config['platform'])
    AdminRequest().switch_user_to_test(AdminRequestsVariables.admin_user_login, AdminRequestsVariables.admin_user_password,
                                       reg_mail, config['platform'])


@pytest.mark.current_test
def test_make_user_test(browser, config):
    AdminRequest().select_platform(config['platform'])
    AdminRequest().switch_user_to_test(AdminRequestsVariables.admin_user_login,
                                      AdminRequestsVariables.admin_user_password,
                                            "ValidityUser6@mailinator.com", config['platform'])

