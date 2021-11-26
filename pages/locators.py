from selenium.webdriver.common.by import By


class BasePageLocators:
    BROWSER_COOKIES_FRAME  = (By.CSS_SELECTOR, "iframe#ifrmCookieBanner")
    ASSEPT_BROWSER_COOKIES_BTN = (By.CSS_SELECTOR,".sp-cookie-banner-3>.intro-banner-btn")

class RegisterPageLocators:
    REGISTRATION_FORM_OPEN_BTTN = (By.CSS_SELECTOR,".button-background.button-lg.orange")
    REGISTRATION_FORM = (By.CSS_SELECTOR,"#registrationForm")
    
    FIELD_EMAIL = (By.CSS_SELECTOR,"#registrationFormEmail-modal")
    FIELD_PASSWORD= (By.CSS_SELECTOR,"#RegistrationFormPassword-modal")
    FIELD_FIRSTNAME= (By.CSS_SELECTOR,"#registrationFormFirstName-modal")
    FIELD_LASTNAME= (By.CSS_SELECTOR,"#registrationFormLastName-modal")
    FIELD_DOB = (By.CSS_SELECTOR, "#birthday")
    SELECT_GENDER_M= (By.CSS_SELECTOR,"div:nth-of-type(2) > .gender.register-label")
    SELECT_GENDER_F = (By.CSS_SELECTOR, "div:nth-of-type(3) > .gender.register-label")
    SUBMIT_FIRST_STEP_BTTN = (By.CSS_SELECTOR, "#registrationForm .button-lg.orange")

    SELECT_COUNTRY =(By.CSS_SELECTOR,".ng-select-searchable [role]")
    SELECT_COUNTRY_ID = (By.CSS_SELECTOR,"div:nth-of-type(2) > div:nth-of-type(18)")
    FIELD_ADDRESS=(By.CSS_SELECTOR,"#registrationFormSecondStep-modal")
    FIELD_CITY = (By.CSS_SELECTOR, "#registrationFormCity-modal")
    FIELD_ZIP = (By.CSS_SELECTOR, "#registrationFormZipCode-modal")
    FIELD_PHONE = (By.CSS_SELECTOR, "#registrationFormPhoneNumber-modal")
    CHECK_ASSEPT_ALL = (By.CSS_SELECTOR, "[for='acceptAll-modal']")
    CHECK_EMAIL_ACTIVATION = (By.CSS_SELECTOR, "[for='registrationFormActivation_email']")
    
    SUBMIT_SECOND_STEP_BTTN = (By.CSS_SELECTOR, ".buttons-wrapper [type='submit']")

    SUCCESS_MESSAGE_EMAIL = (By.CSS_SELECTOR, ".message.message-email.ng-star-inserted")
    REGISTRATION_DONE_BTTN= (By.CSS_SELECTOR, ".button-bordered.button-md")
    

class MailPageLocators:
    MAILINATOR_ENTER_MAIL = (By.CSS_SELECTOR, "#addOverlay")
    MAILINATOR_GO_MAIL_PAGE_BTTN = (By.CSS_SELECTOR,"button#go-to-public")

    MAILINATOR_OPEN_MESSAGE = (By.CSS_SELECTOR, "[ng-repeat = 'email in emails']")
    MAILINATOR_OPEN_JSON_TEXT = (By.CSS_SELECTOR,"a#pills-json-tab")
    MAILINATOR_GET_MAIL_CONTENT = (By.CSS_SELECTOR, "div#pills-json-content > pre")

    






