from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_product_in_basket(self): # Негативная проверка       
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TITLE), "Your basket is not empty" 
        # Данный локатор может появиться на странице, только если в корзину добавлен товар
    
    def should_be_message_that_the_basket_is_empty(self): # Позитивная проверка       
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "The message that the basket is empty did not appear" 
        # Данный локатор уникален для страницы пустой корзины, а для страницы корзины с товарами, совпадения не найдутся
        message_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert "Your basket is empty" in message_text, "The text 'Your basket is empty' did not appear"
        # Проверка только для текста на английском языке, так как при запуске теста мы указываем конкретный язык, 
        # такой подход корректен в соответствии с комментарием автора курса
        # https://stepik.org/lesson/201964/step/10?discussion=1057515&reply=1057527&unit=176022