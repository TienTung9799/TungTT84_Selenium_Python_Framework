import pytest
from tests.basetest import BaseTest
from pages.loginpage import LoginPage
import time

class TestLogin(BaseTest):
    def test_login_successful(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login()
        time.sleep(10)
