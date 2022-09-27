import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_driver import BaseDriver
from util.get_locator import GetLocator


class LoginPage:
    # get all the elements on login page
    def __init__(self,driver):
        self.driver = driver
        self.locator = GetLocator(self.driver)

    # get username text field
    def get_username_element(self):
        return self.locator.get_element("username")

    # get password text field
    def get_password_element(self):
        return self.locator.get_element("password")

    # get log in button
    def get_login_button(self):
        return self.locator.get_element("login")

    # get login as guest button
    def get_login_as_guest(self):
        return self.locator.get_element("login_guest")

    # get toast element when login with credentials failed
    def get_login_fail_toast(self, message):
        toast_element = ("xpath", "//*[contains(@text,'{}')]".format(message))
        return WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located(toast_element))

