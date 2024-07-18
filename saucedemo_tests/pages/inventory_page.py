from selene import browser
from saucedemo_tests.pages.authorization_page import autorization
from saucedemo_tests.data.users import User
import allure


class Inventory:

    def __init__(self):
        self.product_in_cart = 0

    @allure.step('Авторизация и открытие страницы со списком товаров')
    def open_inventory(self):
        user = User(
            username='standard_user',
            password='secret_sauce'
        )
        autorization.open_autorization_page().fill_username(user).fill_password(
            user).click_login().assert_successful_authorization()
        return self

    @allure.step('Добавление в корзину всех товаров')
    def add_all_product_to_cart(self):
        self.all_elements = browser.all("[id^='add-to-cart']")
        self.product_added = 0
        for button in self.all_elements:
            button.click()
            self.product_added += 1
        return self

    @allure.step('Проверка добавления всех товаров в корзину')
    def assert_all_product_added_to_cart(self):
        add_to_cart_elements = browser.all("[id^='add-to-cart']")
        assert len(add_to_cart_elements) == 0, "Не все товары добавлены в корзину"
        return self

    @allure.step('Удаление всех товаров из корзины')
    def clear_cart(self):
        remove_all_product = browser.all("[id^='remove")
        for button in remove_all_product:
            button.click()
        return self

    @allure.step('Проверка удаления всех товаров из корзины')
    def assert_clear_cart(self):
        remove_elements = browser.all("[id^='remove']")
        assert len(remove_elements) == 0, "Не все товары удалены из корзины"
        return self

    @allure.step('Открытие страницы с корзиной')
    def click_cart_button(self):
        browser.element('[data-test="shopping-cart-link"]').click()
        return self

    @allure.step('Проверка открытия страницы с корзиной')
    def assert_open_cart(self):
        assert browser.driver.current_url == 'https://www.saucedemo.com/cart.html'
        return self

    @allure.step('Добавление в корзину одного товара')
    def add_one_product_to_cart(self):
        browser.element("[id^='add-to-cart']").click()
        self.product_in_cart += 1
        return self


inventory = Inventory()
