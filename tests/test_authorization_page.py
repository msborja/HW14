from saucedemo_tests.pages.authorization_page import authorization
from saucedemo_tests.data.users import User
import allure


@allure.story('Успешная авторизация')
def test_successful_authorization():
    user = User(
        username='standard_user',
        password='secret_sauce'
    )
    authorization.open_authorization_page().fill_username(user).fill_password(
        user).click_login().assert_successful_authorization()


@allure.story('Авторизация c аккаунта заблокированного пользователя')
def test_unsuccessful_authorization():
    user = User(
        username='locked_out_user',
        password='secret_sauce'
    )
    authorization.open_authorization_page().fill_username(user).fill_password(
        user).click_login().assert_unsuccessful_authorization()
