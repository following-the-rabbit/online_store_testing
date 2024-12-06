from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_TITLE = (By.CLASS_NAME, "basket-title") 

class LoginPageLocators():
    LOCGIN_FORM = (By.ID, "login_form")
    LOGIN_EMAIL = (By.ID, "id_login-username")
    LOGIN_PASSWORD = (By.ID, "id_login-password")
    LOGIN_SUBMIT = (By.NAME, "login_submit")

    REGISTRATION_FORM = (By.ID, "register_form")
    REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD1 =(By.ID, "id_registration-password1")
    REGISTRATION_PASSWORD2 =(By.ID, "id_registration-password2")
    REGISTRATION_SUBMIT = (By.NAME, "registration_submit")

class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CLASS_NAME,"btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:nth-of-type(1) .alertinner")
    BOOK_TITLE = (By.TAG_NAME, "h1")
    ITEM_TITLE = (By.CSS_SELECTOR, "#messages .alert:nth-of-type(1) strong")
    BOOK_PRICE = (By.CSS_SELECTOR, ".col-sm-6 p.price_color")
    BASKET_TOTAL = (By.CSS_SELECTOR, "#messages .alert:nth-of-type(3) strong")    
