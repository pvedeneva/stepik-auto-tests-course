from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_cart_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART), "Add to cart not presented"

    def add_to_cart(self):
        add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add_to_cart.click()

    def check_in_cart(self):
        """Сообщение о том, что товар добавлен в корзину.
        Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
        """
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        alert_product_name = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_NAME).text
        assert product_name == alert_product_name, "Added wrong item"

    def check_price_cart_and_product_eq(self):
        """Сообщение со стоимостью корзины.
        Стоимость корзины совпадает с ценой товара.
        """
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        alert_cart_price = self.browser.find_element(*ProductPageLocators.ALERT_CART_PRICE).text
        assert product_price == alert_cart_price, "Wrong quantity in cart"

    def should_not_be_success_message(self): # TODO
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disapear_success_message(self): # TODO
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"