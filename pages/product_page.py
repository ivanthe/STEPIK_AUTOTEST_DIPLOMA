from .base_page import BasePage
from ..locator.locators import ProductPageLocators
import time

class ProductPage(BasePage):

    def click_button_add_goods_to_basket(self):
        self.actual_good = [str(self.browser.find_element(*ProductPageLocators.ACTUAL_GOOD_ON_PAGE).text),
                            str(self.browser.find_element(*ProductPageLocators.ACTUAL_PRICE_ON_PAGE).text)]
        print(self.actual_good)
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()
        return self.actual_good


    def should_be_added_to_basket_correct_good(self, expected_good_name):
        actual_good_name = self.browser.find_element(*ProductPageLocators.NAME_OF_GOOD).text
        assert actual_good_name == expected_good_name, "Товар в корзине не соответствует выбранному"

    def shoulb_be_correct_price(self, expected_price):
        actual_price = self.browser.find_element(*ProductPageLocators.ACTUAL_PRICE_ON_PAGE).text
        assert actual_price == expected_price, "Цена в корзине не соответствует актуальной цене"



