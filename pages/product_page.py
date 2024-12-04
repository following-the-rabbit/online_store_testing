from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_item_to_basket(self):
        btn_add_to_basket = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn_add_to_basket.click()

    # def check_added_item(self):
    #     item_addition_success = self.browser.find_element(*ProductPageLocators.ITEM_ADDITION_SUCCESS).text
    #     assert "has been added to your basket" in item_addition_success, "Item has not been added to your basket"

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_ADDITION_SUCCESS), "Success message is not presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ITEM_ADDITION_SUCCESS), "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ITEM_ADDITION_SUCCESS), "Success message is not disappeared"

    def check_item_title(self):
        book_title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text
        item_title = self.browser.find_element(*ProductPageLocators.ITEM_TITLE).text
        assert book_title == item_title, "Invalid item added to basket"

    def check_price_and_total(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert book_price == basket_total, "Item price is not equal to total basket"