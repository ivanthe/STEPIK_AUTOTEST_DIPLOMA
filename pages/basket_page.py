from .base_page import BasePage
from ..locator.locators import BasketPageLocators

class BasketPage(BasePage):

    def should_be_empty_basket(self):
        actual_massage = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE).text
        print("Актуальное сообщение из корзины  -  ", actual_massage)
        assert  "Your basket is empty." in actual_massage, "Корзина не пустная. ДОЛЖНА БЫТЬ ПУСТОЙ"