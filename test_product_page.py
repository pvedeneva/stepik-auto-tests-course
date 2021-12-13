import pytest
from selenium import webdriver
from .pages.product_page import ProductPage
from .pages.main_page import MainPage
from .pages.base_page import BasePage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    product.open()                      # открываем страницу
    product.should_be_cart_btn()
    product.add_to_cart()
    product.solve_quiz_and_get_code()
    product.check_in_cart()
    product.check_price_cart_and_product_eq()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """Открываем страницу товара
    Добавляем товар в корзину
    Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    """
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    product = ProductPage(browser, link)
    product.open()
    product.add_to_cart()
    product.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    """Открываем страницу товара
    Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    """
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product = ProductPage(browser, link)
    product.open()
    product.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    """Открываем страницу товара
    Добавляем товар в корзину
    Проверяем, что нет сообщения об успехе с помощью is_disappeared
    """
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product = ProductPage(browser, link)
    product.open()
    product.add_to_cart()
    product.should_disapear_success_message()