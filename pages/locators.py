from selenium.webdriver.common.by import By


class BasePageLocators:
    BROWSER_COOKIES_FRAME  = ((By.CSS_SELECTOR, "iframe#ifrmCookieBanner"))
    ASSEPT_BROWSER_COOKIES_BTN = ((By.CSS_SELECTOR,".sp-cookie-banner-3>.intro-banner-btn"))

class RegisterPageLocators:
    REGISTRATION_FORM_OPEN_BTTN = (By.CSS_SELECTOR,".button-background.button-lg.orange")

