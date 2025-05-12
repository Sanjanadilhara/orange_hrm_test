from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Dashboard:
    def __init__(self, driver):
        self.driver = driver
        self.LOGOUT_LINK = (By.XPATH, "//a[text()='Logout']")
        self.USER_DROPDOWN = (By.XPATH, "//span[@class='oxd-userdropdown-tab']")
        self.wait = WebDriverWait(driver, 10)

    def logout(self):
        self.wait.until(EC.element_to_be_clickable(self.USER_DROPDOWN)).click()
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_LINK)).click()
