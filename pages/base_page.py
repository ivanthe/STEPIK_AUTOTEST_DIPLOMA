import math
import time
from .locators import BasePageLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage():
    def __init__(self, browser, url, timeout=3):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self): #открывает страницу
        self.browser.get(self.url)

    def go_to_login_page(self): #переходит на страницу логина и регистрации
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()

    def go_to_basket(self): #переходит в корзину
        self.browser.find_element(*BasePageLocators.BASKET_BUTTON).click()

    def should_be_login_link(self): #проверяет есть ли ссылка на логин и регистрацию
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Сыылка на логин не представлена на странице"

    def is_element_present(self, how, what):  #проверяет присутствует ли элемент на странице
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_mot_element_present(self, how, what, timeout=4):    #проверяет что элемент не появляется в течении timeout
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):  #проверяет, что элемент исчезает в течении timeout
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException)\
                .until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def should_be_authorized_user(self): #проверяет прошла ли авторизация
        assert self.is_element_present(*BasePageLocators.USER_ICON), "Иконка пользователя не представлена," \
                                                                     " ПОЛЬЗОВАТЕЛЬ НЕ БЫЛ АВТОРИЗОВАН!!!"

    def solve_quiz_and_get_code(self):  #решает задачу в алерте
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Ваш код: {alert_text}")
            time.sleep(2)
            alert.accept()
        except NoAlertPresentException:
            print("Второй АЛЕРТ не появился")


