from selenium.webdriver.common.by import By

class Login:
    def __init__(self, driver):
        self.driver = driver
        self.text_box_username_Name = "username"
        self.text_box_password_Name = "password"
        self.submit_button_Name = "orangehrm-login-button"

    def setUsername(self, username):
        self.driver.find_element(By.NAME, self.text_box_username_Name).clear()
        self.driver.find_element(By.NAME, self.text_box_username_Name).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.NAME, self.text_box_password_Name).clear()
        self.driver.find_element(By.NAME, self.text_box_password_Name).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.CLASS_NAME, self.submit_button_Name).click()
