from pages.register_page import RegisterPage

link = "https://dev.bosscasino.com/registration"

def test_accept_browser_cokies(browser):
    page = RegisterPage(browser,link)
    page.open_and_accept_browser_cookies()

def test_open_register_form(browser):
    page = RegisterPage(browser,link)
    page.open_and_accept_browser_cookies()
    page.is_exist_register_button()
    page.click_register_button()