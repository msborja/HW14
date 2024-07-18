from saucedemo_tests.pages.inventory_page import inventory
from saucedemo_tests.pages.cart_page import cart
import allure


@allure.story('Удаление товара из корзины')
def test_cart():
    (
        inventory
        .open_inventory()
        .add_one_product_to_cart().add_one_product_to_cart().add_one_product_to_cart()
    )
    (
        cart
        .assert_product_in_cart()
        .remove_product_from_cart().assert_remove_product_in_cart()
    )

@allure.story('Возвращение на страницу со списком товаров')
def test_return_to_inventory():
    cart.open_cart().return_to_inventory().assert_return_to_inventory()

@allure.story('Переход на страницу оплаты товаров')
def test_go_to_checkout():
    cart.open_cart().go_to_checkout().assert_go_to_checkout()
