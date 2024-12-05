from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) 
    # инициализируем Page Object, передаем 
    # в конструктор экземпляр драйвера и url адрес
    page.open()
    #  открываем страницу
    page.go_to_login_page()
    #  выполняем метод страницы - переходим на страницу логина

    # ниже старый код, который мы перепесали через методы двух класов родителя и потгомка
    # browser.get(link)
    # login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    # login_link.click()

    # Переходы между страницами
    login_page = LoginPage(browser, browser.current_url) 
    #  переход между страницами происходит неявно, инициализируем страницу LoginPage в теле теста: 
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_should_see_login_url(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()

def test_guest_should_see_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()

def test_guest_should_see_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_product_in_basket()    
    basket_page.should_be_message_that_the_basket_is_empty()
