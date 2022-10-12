from selenium.webdriver.common.by import By

from util.get_locator import GetLocator


class AccountPage:
    def __init__(self, driver):
        self.driver = driver
        self.locator = GetLocator(self.driver)

    # get hamburger back icon
    def get_hamburger_icon(self):
        return self.locator.get_element("account", "hamburger_account")

    # get first name input field
    def get_first_name(self):
        return self.locator.get_element("account", "first_name")

    # get last name input field
    def get_last_name(self):
        return self.locator.get_element("account", "last_name")

    # get special condition dropdown list
    def get_special_condition(self):
        return self.locator.get_element("account", "special_condition")

    # get check mark button
    def get_check_mark_button(self):
        return self.locator.get_element("account", "check_mark")

    # get Blind condition
    def get_condition_blind(self):
        return self.locator.get_element("account", "blind")

    # get Visually Impaired
    def get_condition_visually_impaired(self):
        return self.locator.get_element("account", "visually_impaired")

    # get Wheel Chair condition
    def get_condition_wheel_chair(self):
        return self.locator.get_element("account", "wheel_chair")

    # get None condition
    def get_condition_none(self):
        return self.locator.get_element("account", "none")


