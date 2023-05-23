from .base_page import BasePage
from ..locator.locators import LoginPageLocators


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