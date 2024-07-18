from selene import browser, have
import allure
from saucedemo_tests.data.users import User


class Autorization:

    @allure.step('Открытие страницы')
    def open_autorization_page(self):
        browser.open('')
        return self

    @allure.step('Заполнение поля Username')
    def fill_username(self, user: User):
        browser.element('#user-name').type(user.username)
        return self

    @allure.step('Заполнение поля Password')
    def fill_password(self, user: User):
        browser.element('#password').type(user.password)
        return self

    @allure.step('Нажатие на кнопку Login')
    def click_login(self):
        browser.element('#login-button').click()
        return self

    @allure.step('Проверка успешной авторизации')
    def assert_successful_authorization(self):
        assert browser.driver.current_url == 'https://www.saucedemo.com/inventory.html'

    @allure.step('Проверка неуспешной авторизации')
    def assert_unsuccessful_authorization(self):
        browser.element('[data-test="error"]').should(have.text('Epic sadface: Sorry, this user has been locked out.'))


autorization = Autorization()
