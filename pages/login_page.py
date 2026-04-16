from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.ID, "flash")
    SUCCESS_MESSAGE = (By.ID, "flash")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_username(self, username):
        field = self.wait.until(EC.presence_of_element_located(self.USERNAME_INPUT))
        field.clear()
        field.send_keys(username)

    def enter_password(self, password):
        field = self.wait.until(EC.presence_of_element_located(self.PASSWORD_INPUT))
        field.clear()
        field.send_keys(password)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_flash_message(self):
        return self.wait.until(EC.presence_of_element_located(self.SUCCESS_MESSAGE)).text

    def is_login_successful(self):
        try:
            msg = self.get_flash_message()
            return "You logged into a secure area" in msg
        except Exception:
            return False

    def is_login_failed(self):
        try:
            msg = self.get_flash_message()
            return "Your username is invalid" in msg or "Your password is invalid" in msg
        except Exception:
            return False
