from saucedemo_tests.pages.cart_page import cart
from saucedemo_tests.pages.inventory_page import inventory
from saucedemo_tests.pages.checkout_pages import checkoutStepOne, checkoutStepTwo, checkoutComplete
from saucedemo_tests.data.address import Address
import allure


@allure.story('Покупка товаров')
def test_checkout():
    (
        inventory
        .open_inventory()
        .add_one_product_to_cart().add_one_product_to_cart().add_one_product_to_cart()
        .click_cart_button()
    )
    (
        cart
        .go_to_checkout().assert_go_to_checkout()
    )

    address = Address(
        firstName='Kevin',
        lastName='Parker',
        postalCode=10011
    )
    (
        checkoutStepOne
        .fill_first_name(address).click_continue().error_fill_required_fields()
        .fill_last_name(address).click_continue().error_fill_required_fields()
        .fill_postal_code(address).click_continue()
        .assert_go_to_overview()
    )

    (
        checkoutStepTwo
        .assert_total_price().click_finish_button().assert_go_to_complete()
    )

    (
        checkoutComplete
        .click_back_home().assert_click_back_home()
    )
