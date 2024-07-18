from saucedemo_tests.pages.authorization_page import autorization
from saucedemo_tests.pages.inventory_page import inventory
from saucedemo_tests.data.users import User
from selene import browser
import allure


class Cart:

    @allure.step('Открытие корзины')
    def open_cart(self):
        user = User(
            username='standard_user',
            password='secret_sauce'
        )
        autorization.open_autorization_page().fill_username(user).fill_password(
            user).click_login().assert_successful_authorization()
        inventory.click_cart_button().assert_open_cart()
        return self

    @allure.step('Возвращение на страницу со списком товаров')
    def return_to_inventory(self):
        browser.element('#continue-shopping').click()
        return self

    @allure.step('Проверка возвращения на страницу со списком товаров')
    def assert_return_to_inventory(self):
        assert browser.driver.current_url == 'https://www.saucedemo.com/inventory.html'

    @allure.step('Переход на страницу оплаты товаров')
    def go_to_checkout(self):
        browser.element('#checkout').click()
        return self

    @allure.step('Проверка перехода на страницу оплаты товаров')
    def assert_go_to_checkout(self):
        assert browser.driver.current_url == 'https://www.saucedemo.com/checkout-step-one.html'
        return self

    @allure.step('Проверка количества товаров в корзине')
    def assert_product_in_cart(self):
        self.remove_buttons = browser.all("[id^='remove']")
        return self

    @allure.step('Удаление товара из корзины')
    def remove_product_from_cart(self):
        browser.element("[id^='remove']").click()
        inventory.product_in_cart -= 1
        return self

    @allure.step('Проверка количества товаров в корзине после удаления')
    def assert_remove_product_in_cart(self):
        quantity_remove_button = browser.all("[id^='remove']")
        assert len(quantity_remove_button) == inventory.product_in_cart
        return self


cart = Cart()
