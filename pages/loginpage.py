from selenium.webdriver.common.by import By
from pages.basepage import BasePage
 
class LoginPage(BasePage):
    def enter_username(self, username):
        username_input = self.wait_for_element(By.XPATH, "//input[@name='username']")
        username_input.send_keys(username)
 
    def enter_password(self, password):
        password_input = self.wait_for_element(By.XPATH, "//input[@name='password']")
        password_input.send_keys(password)
 
    def click_login(self):
        login_button = self.wait_for_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
 
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()