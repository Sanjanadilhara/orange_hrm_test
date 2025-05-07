import pytest
from selenium import webdriver
from PageObjects.LoginPage import Login
import time

class Test_001_Login:
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"

    def test_homePageTitle(self):
        driver = webdriver.Chrome()
        driver.get(self.base_url)
        assert "OrangeHRM" in driver.title
        driver.quit()

    def test_login(self):
        driver = webdriver.Chrome()
        driver.get(self.base_url)
        login = Login(driver)

        time.sleep(10)
        login.setUsername(self.username)
        login.setPassword(self.password)
        login.clickLogin()

        time.sleep(3)
        assert "OrangeHRM" in driver.title
        driver.quit()
