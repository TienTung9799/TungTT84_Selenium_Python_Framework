import pytest
import allure
from pages.loginpage import LoginPage
import pytest
import allure
from pages.loginpage import LoginPage
from utilities.config_reader import ConfigReader
from tests.basetest import BaseTest

@pytest.mark.usefixtures("setup")
@allure.feature("Login Feature")

class Test_LoginPage(BaseTest):
    @allure.story("Login Successfull")
    @allure.title("Valid account")

    def test_login_success(self):
        login_page = LoginPage(self.driver)
        login_page.login_successfull(ConfigReader.get_username(), ConfigReader.get_password())
        assert login_page.verify_dashboard_title() is True
