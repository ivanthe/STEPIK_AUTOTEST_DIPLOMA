from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

def test_guest_should_see_login_link_on_product_page(browser): #наличие ссылки для авторизации и регистрации
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser): #возможность перейти на страциу авторизации
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?"
                                               "promo=offer7", marks=pytest.mark.xfail(reason='ЖДЕМ ПОКА ИСПРАВЯТ '
                                                                                              'БАГ!!!')),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link): #в корзину добавлен вреный товар с верной ценой
    product_page = ProductPage(browser, link)
    product_page.open()
    actual_good_data = product_page.click_button_add_goods_to_basket()
    name = actual_good_data[0]
    price = actual_good_data[1]
    product_page.should_be_added_to_basket_correct_good(name)
    product_page.should_be_correct_price(price)


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): #отсутствует сообщение
                                                                                    # о добавления товара в корзину
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.click_button_add_goods_to_basket()
    product_page.should_not_be_success_massage()

def test_guest_cant_see_success_message(browser): #отсутствует сообщине о добавлении в коризину на странице товара
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_massage()

@pytest.mark.xfail(reason="Ждем пока реализуют функционал")
def test_message_disappeared_after_adding_product_to_basket(browser): #сообщение о добавлении товара в коризину исчезает
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.click_button_add_goods_to_basket()
    product_page.should_disappear()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser): #корзина пустая (товар не добавлялся)
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()

class TestUserAddToBasketFromProductPage(): #тесты для зарегестрированных пользователей

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser): #Создается тестовое окружение: Регистрируется новый пользователь
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.go_to_login_page()
        login_page.register_new_user()
        login_page.should_be_authorized_user()


    def test_user_cant_see_success_message(self, browser): #пользователь не видет сообщения о добавлении товара
                                                            # в коризу на странице товара
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_massage()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser): #Пользователь добавли в корзину товар.
                                                            # Товар и цена верные
        product_page = ProductPage(browser, link)
        product_page.open()
        actual_good_data = product_page.click_button_add_goods_to_basket()
        name = actual_good_data[0]  #название получено до клика ДОБАВИТЬ В КОРЗИНУ
        price = actual_good_data[1]  #цена получено до клика ДОБАВИТЬ В КОРЗИНУ
        product_page.should_be_added_to_basket_correct_good(name)
        product_page.should_be_correct_price(price)