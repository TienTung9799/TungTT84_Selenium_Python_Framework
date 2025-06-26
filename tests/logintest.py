import pytest
from tests.basetest import driver 
from pages.loginpage import LoginPage
from config.account_config import orangehrm_config

class TestLogin:
    def test_valid_login(self, driver):
        login_page = LoginPage(driver)
        login_page.login_successfull(orangehrm_config.USERNAME, orangehrm_config.PASSWORD)