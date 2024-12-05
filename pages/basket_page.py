from .base_page import BasePage
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    def should_not_be_product_in_basket(self): # Негативная проверка       
        assert self.is_not_element_present(By.CLASS_NAME, "basket-title"), "Your basket is not empty" 
        # Данный селектор может появиться на странице, только если в корзину добавлен товар
    
    def should_be_message_that_the_basket_is_empty(self): # Позитивная проверка       
        assert self.is_element_present(By.CSS_SELECTOR, "#content_inner > p"), "The message that the basket is empty did not appear" 
        # Данный селектор уникален для страницы пустой корзины, а для страницы корзины с товарами, совпадения не найдутся
        message_text = self.browser.find_element(By.CSS_SELECTOR, "#content_inner > p").text
        assert "Your basket is empty" in message_text, "The text 'Your basket is empty' did not appear"
        # Проверка только для текста на английском языке, так как при запуске теста мы указываем конкретный язык, 
        # такой подход корректен в соответствии с комментарием автора курса
        # https://stepik.org/lesson/201964/step/10?discussion=1057515&reply=1057527&unit=176022