from .base_page import BasePage
from ..locator.locators import BasketPageLocators
from ..data.data import Constants

class BasketPage(BasePage):

    def should_be_empty_basket(self):
        actual_massage = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE).text
        print("Актуальное сообщение из корзины  -  ", actual_massage)
        assert Constants.BASKET_EMPTY in actual_massage, "Корзина не пустная. ДОЛЖНА БЫТЬ ПУСТОЙ"