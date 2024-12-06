from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage): 

    def register_new_user(self, email, password):
        self.should_be_register_form()
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT).click()   
        
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):        
        current_url = self.browser.current_url
        assert "login" in current_url, "URL does not contain the word 'login'"

    def should_be_login_form(self):        
        assert self.is_element_present(*LoginPageLocators.LOCGIN_FORM), "Login form is not presented"
        
    def should_be_register_form(self):        
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Register form is not presented"
        