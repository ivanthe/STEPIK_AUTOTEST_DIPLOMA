from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    ACTUAL_URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"

    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_USERNAME_INPUT = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON = (By.NAME, "login_submit")

    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_USERNAME_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_CONFIRM_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")


