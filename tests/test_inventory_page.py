from saucedemo_tests.pages.inventory_page import inventory
import allure


@allure.story('Добавление всех товаров в корзину')
def test_add_inventory():
    (
        inventory.open_inventory().
        add_all_product_to_cart().assert_all_product_added_to_cart()
    )


@allure.story('Добавление всех товаров в корзину')
def test_clear_inventory():
    (
        inventory.open_inventory().
        add_all_product_to_cart().assert_all_product_added_to_cart().
        clear_cart().assert_clear_cart()
    )
