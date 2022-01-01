from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    HEADER_BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

    EMAIL_ON_REG_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    PASSW_1_ON_REG_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSW_2_ON_REG_FORM = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, "name=registrationsubmit")

    REGISTRATION_FORM = (By.NAME, "registration_submit")


class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, ".alertinner strong:first-child")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    ALERT_CART_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")
    # добавить тэг для мини конзины в шапке сайта


class BasketPageLocators():
    NOT_AN_EMPTY_BASKET = (By.CSS_SELECTOR, ".basket-title .row") #  rows in basket
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner>p>a") #  rows in basket
