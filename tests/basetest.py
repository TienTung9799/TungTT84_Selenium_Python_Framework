from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
 
class BaseTest:
 """Base test class to set up and tear down the WebDriver."""
 driver = webdriver.Chrome(service=Service("drivers/chromedriver.exe"))
 driver.get("https://opensource-demo.orangehrmlive.com")