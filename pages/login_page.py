from .base_page import BasePage
from ..locator.locators import LoginPageLocators
from ..data.data import Data
import time
from faker import Faker


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert str(self.browser.current_url) == LoginPageLocators.ACTUAL_URL, "Ссылка неверная"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Форма ЛОГИНА отсутствует"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Форма РЕГИСТРАЦИИ отсутствует"

    def register_new_user(self):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_USERNAME_INPUT)\
            .send_keys(str(time.time())+"@some.com")
        """fake = Faker()
        self.browser.find_element(*LoginPageLocators.REGISTRATION_USERNAME_INPUT) \
            .send_keys(fake.email())  -   ТРЕНИРОВАЛСЯ С БИБЛИОТЕКОЙ FAKER
                                           В requirements.txt добавлено """
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_INPUT)\
            .send_keys(Data.PASSWORD_FOR_REGISTRATION)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM_INPUT)\
            .send_keys(Data.PASSWORD_FOR_REGISTRATION)
        time.sleep(5)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)\
            .click()
