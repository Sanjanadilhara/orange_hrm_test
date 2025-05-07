import pytest
from selenium import webdriver
from PageObjects.LoginPage import Login
import time

class Test_001_Login:
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    wrong_username = "Admin1"
    password = "admin123"
    wrong_password = "admin1235"

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
        assert driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        driver.quit()

    def test_login_wrong_password(self):
        driver = webdriver.Chrome()
        driver.get(self.base_url)
        login = Login(driver)

        time.sleep(10)
        login.setUsername(self.username)
        login.setPassword(self.wrong_password)
        login.clickLogin()

        time.sleep(5)
        assert driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        driver.quit()

    def test_login_wrong_username(self):
        driver = webdriver.Chrome()
        driver.get(self.base_url)
        login = Login(driver)

        time.sleep(10)
        login.setUsername(self.wrong_username)
        login.setPassword(self.password)
        login.clickLogin()

        time.sleep(5)
        assert driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        driver.quit()
