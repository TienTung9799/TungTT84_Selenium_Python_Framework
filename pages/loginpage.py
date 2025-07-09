from selenium.webdriver.common.by import By
from pages.basepage import BasePage

class LoginPage(BasePage):
    username_input = (By.XPATH, "//input[@name='username']")
    password_input = (By.XPATH, "//input[@name='password']")
    login_btn = (By.XPATH, "//button[@type='submit']")
    dashboard_title =(By.XPATH,"//h6[text()='Dashboard']")

    def enter_username(self, username):
        self.wait_for_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.wait_for_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.wait_for_element(*self.login_btn).click()

    def verify_dashboard_title(self):
         dashboard_title = self.wait_for_element(*self.dashboard_title).is_displayed()
         return dashboard_title

    def login_successfull(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
