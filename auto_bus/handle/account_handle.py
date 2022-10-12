from selenium.webdriver.common.by import By

from page.account_page import AccountPage


class AccountHandle:
    def __init__(self, driver):
        self.ap = AccountPage(driver)

    # click hamburger button
    def click_hamburger_button(self):
        self.ap.get_hamburger_icon().click()

    # click check mark button
    def click_check_mark_button(self):
        self.ap.get_check_mark_button().click()

    # clear first name input field
    def clear_first_name(self):
        self.ap.get_first_name().clear()

    # input first name
    def send_keys_first_name(self, first_name):
        self.ap.get_first_name().send_keys(first_name)

    # clear last name input field
    def clear_last_name(self):
        self.ap.get_last_name().clear()

    # input last name
    def send_keys_last_name(self, last_name):
        self.ap.get_last_name().send_keys(last_name)

    # click special condition
    def click_special_condition(self):
        self.ap.get_special_condition().click()

    # click condition Blind
    def click_condition_blind(self):
        self.ap.get_condition_blind().click()

    # click condition Visually Impaired
    def click_condition_visually_impaired(self):
        self.ap.get_condition_visually_impaired().click()

    # click condition Wheel Chair
    def click_condition_wheel_chair(self):
        self.ap.get_condition_wheel_chair().click()

    # click condition None
    def click_condition_none(self):
        self.ap.get_condition_none().click()




