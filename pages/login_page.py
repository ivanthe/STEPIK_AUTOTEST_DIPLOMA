from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self): #проверяет страницу логина на наличие форм лигин и регистрация
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self): #проверяет верная ли ссылка страницы логина и регистрации
        assert str(self.browser.current_url) == LoginPageLocators.ACTUAL_URL, "Ссылка неверная"

    def should_be_login_form(self): #проверяет наличие формы логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Форма ЛОГИНА отсутствует"

    def should_be_register_form(self): #проверяет наличие формы регистрации
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Форма РЕГИСТРАЦИИ отсутствует"

    def register_new_user(self): #регистрирует нового пользователя
        self.browser.find_element(*LoginPageLocators.REGISTRATION_USERNAME_INPUT)\
            .send_keys(str(time.time())+"@some.com")
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_INPUT)\
            .send_keys("just_password")
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM_INPUT)\
            .send_keys("just_password")
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)\
            .click()
