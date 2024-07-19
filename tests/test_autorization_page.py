from saucedemo_tests.pages.authorization_page import autorization
from saucedemo_tests.data.users import User
import allure


@allure.story('Успешная авторизация')
def test_successful_autorization():
    user = User(
        username='standard_user',
        password='secret_sauce'
    )
    autorization.open_autorization_page().fill_username(user).fill_password(
        user).click_login().assert_successful_authorization()

@allure.story('Авторизация c аккаунта заблокированного пользователя')
def test_unsuccessful_autorization():
    user = User(
        username='locked_out_user',
        password='secret_sauce'
    )
    autorization.open_autorization_page().fill_username(user).fill_password(
        user).click_login().assert_unsuccessful_authorization()


