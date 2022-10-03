import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from handle.login_handle import LoginHandle


class LoginBusiness:
    def __init__(self, driver):
        self.driver = driver
        self.lh = LoginHandle(self.driver)

    def login(self, username, password):
        self.lh.click_login()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "signin"))
        )
        self.lh.input_username(username)
        self.lh.input_password(password)
        self.lh.click_login_button_box()

    # success
    def login_success(self, username, password):
        self.login(username, password)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'我的课程')]"))
        )
        return self.lh.assert_success_login()

    # blank username
    def no_username_input(self, username, password):
        self.login(username, password)
        return self.lh.assert_no_input_username()

    # blank password
    def no_password_input(self, username, password):
        self.login(username, password)
        return self.lh.assert_no_input_password()

    # mismatch username and password
    def mismatch_inputs(self, username, password):
        self.login(username, password)
        time.sleep(2)
        return self.lh.assert_response_mismatch()
