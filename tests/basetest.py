# tests/basetest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config.account_config import orangehrm_config
@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(orangehrm_config.BASE_URL)
    driver.maximize_window()
    yield driver
    driver.quit()