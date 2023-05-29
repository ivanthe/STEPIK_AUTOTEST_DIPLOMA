from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):

    def click_button_add_goods_to_basket(self): #нажимает кнопку добавить в корзину,
                                                # првдварительно получает актуально название товара и его цену
        self.actual_good = [str(self.browser.find_element(*ProductPageLocators.ACTUAL_GOOD_ON_PAGE).text),
                            str(self.browser.find_element(*ProductPageLocators.ACTUAL_PRICE_ON_PAGE).text)]
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()
        time.sleep(2)
        return self.actual_good


    def should_be_added_to_basket_correct_good(self, expected_good_name): #проверяет верно ыфбрвннф  товар
        actual_good_name = self.browser.find_element(*ProductPageLocators.NAME_OF_GOOD).text
        assert actual_good_name == expected_good_name, "Товар в корзине не соответствует выбранному"

    def should_be_correct_price(self, expected_price): #проверяет цену товара
        actual_price = self.browser.find_element(*ProductPageLocators.ACTUAL_PRICE_ON_PAGE).text
        assert actual_price == expected_price, "Цена в корзине не соответствует актуальной цене"

    def should_not_be_success_massage(self): #проверяет отсутствие сообщения о добавление в корзину
        assert self.is_mot_element_present(*ProductPageLocators.SUCCESS_MASSAGE), "Сообщение о добавлении в корзину " \
                                                                                  "появилось, НЕ ДОЛЖНО ПОЯВЛЯТЬСЯ!!!"

    def should_disappear(self): #проверяет исчезноваение сообщения
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MASSAGE), "Сообщение об успешном добавлении не " \
                                                                          "исчезло. ДОЛЖНО ИСЧЕЗАТЬ В ТЕЧЕНИИ " \
                                                                          "4Х СЕКУНД!!!"



