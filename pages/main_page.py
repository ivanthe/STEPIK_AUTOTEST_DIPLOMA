from .base_page import BasePage
from .login_page import LoginPage
from selenium.webdriver.common.by import By
from ..locator.locators import MainPageLocators
import time

class MainPage(BasePage):
    def go_to_login_page(self):
        self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()
        time.sleep(2)


    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

