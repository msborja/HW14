from selene import browser, be, have
import allure
from saucedemo_tests.data.address import Address


class CheckoutStepOne:

    @allure.step('Проверка отображения ошибки о незаполненности обязательных полей')
    def error_fill_required_fields(self):
        browser.element('h3').should(be.visible).should(have.text('Error:'))
        return self

    @allure.step('Заполнение поля First Name')
    def fill_first_name(self, address: Address):
        browser.element('#first-name').type(address.firstName)
        return self

    @allure.step('Заполнение поля Last Name')
    def fill_last_name(self, address: Address):
        browser.element('#last-name').type(address.lastName)
        return self

    @allure.step('Заполнение поля Zip/Postal Code')
    def fill_postal_code(self, address: Address):
        browser.element('#postal-code').type(address.postalCode)
        return self

    @allure.step('Нажатие кнопки Continue')
    def click_continue(self):
        browser.element('#continue').click()
        return self

    @allure.step('Проверка перехода на страницу Checkout: Overview')
    def assert_go_to_overview(self):
        assert browser.driver.current_url == 'https://www.saucedemo.com/checkout-step-two.html'
        return self


checkoutStepOne = CheckoutStepOne()


class CheckoutStepTwo:

    @allure.step('Проверка стоимости товаров')
    def assert_total_price(self):
        price_product = browser.all('[data-test="inventory-item-price"]')
        total_price = 0
        for price_element in price_product:
            total_price += price

    @allure.step('Нажатие на кнопку Finish')
    def click_finish_button(self):
        browser.element('#finish').click()
        return self

    @allure.step('Проверка перехода на страницу Checkout: Complete!')
    def assert_go_to_complete(self):
        assert browser.driver.current_url == 'https://www.saucedemo.com/checkout-complete.html'
        return self


checkoutStepTwo = CheckoutStepTwo()


class CheckoutComplete:

    @allure.step('Нажатие кнопки Back Home')
    def click_back_home(self):
        browser.element('#back-to-products').click()
        return self

    @allure.step('Проверка нажатия кнопки Back Home')
    def assert_click_back_home(self):
        assert browser.driver.current_url == 'https://www.saucedemo.com/inventory.html'
        return self


checkoutComplete = CheckoutComplete()
