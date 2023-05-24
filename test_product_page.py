from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_add_product_to_basket(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    actual_good_data = product_page.click_button_add_goods_to_basket()
    name = actual_good_data[0]
    price = actual_good_data[1]
    product_page.should_be_added_to_basket_correct_good(name)
    product_page.shoulb_be_correct_price(price)


