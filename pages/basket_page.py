from .base_page import BasePage
from .login_page import LoginPage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def check_empty_basket(self):
        """Ожидаем, что в корзине нет товаров"""
        assert self.is_not_element_present(*BasketPageLocators.NOT_AN_EMPTY_BASKET), "Basket is not empty"
        # not a best practice!!

    def present_empty_basket_text(self):
        """ Ожидаем, что есть текст о том что корзина пуста"""
        #empty_basket_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Empty basket text is not present on a page"


