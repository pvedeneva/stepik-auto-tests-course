from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert 'login' in login_url, "url doesnt contain login"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        self.go_to_login_page # from baseclass
        user_email = self.browser.find_element(*LoginPageLocators.EMAIL_ON_REG_FORM)
        user_email.send_keys(email)
        passw_1 = self.browser.find_element(*LoginPageLocators.PASSW_1_ON_REG_FORM)
        passw_1.send_keys(password)
        passw_2 = self.browser.find_element(*LoginPageLocators.PASSW_2_ON_REG_FORM)
        passw_2.send_keys(password)

        button = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM)
        button.click()

        self.should_be_authorized_user()
