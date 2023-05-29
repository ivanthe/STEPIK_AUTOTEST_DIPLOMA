from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_be_empty_basket(self): #проверяет пустая ли корзина
        actual_massage = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE).text
        assert "Your basket is empty" in actual_massage, "Корзина не пустная. ДОЛЖНА БЫТЬ ПУСТОЙ"