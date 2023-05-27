from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BACKET_BUTTON = (By.XPATH, "//div[contains(@class, 'basket-mini')]//a")

class BasketPageLocators():
    BASKET_EMPTY_MESSAGE = (By.XPATH, "//div[@id='content_inner']/p")

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


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.XPATH, ".//button[contains(@class, 'btn-add-to-basket')]")
    NAME_OF_GOOD = (By.XPATH, "//div[@id='messages']/div[1]/div[contains(@class, 'alertinner')]/strong")
    ACTUAL_GOOD_ON_PAGE = (By.XPATH, "//div[contains(@class, 'product_main')]/h1")
    ACTUAL_PRICE_ON_PAGE = (By.XPATH, "//div[contains(@class, 'product_main')]/p[contains(@class, 'price_color')]")
    SUCCESS_MASAGE = (By.XPATH, "//div[@id='messages']/div[1]")
