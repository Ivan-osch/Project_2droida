import time

from .base_page import BasePage
from .locators import ProductsPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):
    def sort_by_increase(self):
        self.browser.find_element(*ProductsPageLocators.SORT_BY_PRODUCT).click()
        self.browser.find_element(*ProductsPageLocators.SORT_BY_INCREASE).click()

    def sort_by_decrease(self):
        self.browser.find_element(*ProductsPageLocators.SORT_BY_PRODUCT).click()
        self.browser.find_element(*ProductsPageLocators.SORT_BY_DECREASE).click()

    def should_be_sort_by_increase(self):
        prices = self.browser.find_elements(*ProductsPageLocators.PRICE_PRODUCT_IN_PAGE)
        price_min = float(prices[0].text)
        for price in prices:
            assert float(price.text) >= price_min, "Сортировка по возрастанию некорректна"
            price_min = float(price.text)

    def should_be_sort_by_decrease(self):
        prices = self.browser.find_elements(*ProductsPageLocators.PRICE_PRODUCT_IN_PAGE)
        price_max = float(prices[0].text)
        for price in prices:
            assert float(price.text) <= price_max, "Сортировка по убыванию некорректна"
            price_max = float(price.text)

    def add_to_cart(self, number):
        buttons = self.browser.find_elements(*ProductsPageLocators.BUTTON_ADD_TO_CART)
        self.browser.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", buttons[number])
        buttons[number].click()

    def should_not_be_product_in_cart(self, number):
        buttons = self.browser.find_elements(*ProductsPageLocators.BUTTON_ADD_TO_CART)
        text_button = buttons[number].get_attribute("aria-label")
        assert text_button == "В корзину", "Некорректная надпись кнопки, перед добавлением в корзину"

    def should_be_product_in_cart(self, number):
        buttons = self.browser.find_elements(*ProductsPageLocators.BUTTON_ADD_TO_CART)
        text_button = buttons[number].get_attribute("aria-label")
        assert text_button == "В корзине", "Некорректная надпись кнопки, после добавления в корзину"

    def get_product_name(self, number):
        names = self.browser.find_elements(*ProductsPageLocators.PRODUCT_NAME)
        return names[number].text

    def get_product_price(self, number):
        prices = self.browser.find_elements(*ProductsPageLocators.PRICE_PRODUCT_IN_PAGE)
        return prices[number].text


