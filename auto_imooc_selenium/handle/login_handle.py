from log.user_log import UserLog
from page.home_page import HomePage
from page.login_page import LoginPage


class LoginHandle:
    def __init__(self, driver):
        self.driver = driver
        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)
        logger = UserLog()
        self.logger = logger.get_log()

    # click login on home page head
    def click_login(self):
        self.hp.get_login().click()

    # enter username
    def input_username(self, username):
        self.logger.info("Input username is:{}".format(username))
        self.lp.get_username().send_keys(username)

    # enter password
    def input_password(self, password):
        self.logger.info("Input password is:{}".format(password))
        self.lp.get_password().send_keys(password)

    # click login button
    def click_login_button_box(self):
        self.lp.get_login_button().click()

    # assert success login
    def assert_success_login(self):
        return self.hp.get_header_avator().is_displayed()

    # assert no username input ,response element is displayed
    def assert_no_input_username(self):
        return self.lp.get_response_no_username_inputs().is_displayed()

    # assert no password input ,response element is displayed
    def assert_no_input_password(self):
        return self.lp.get_response_no_password_inputs().is_displayed()

    # assert mismatch username and password ,response element is displayed
    def assert_response_mismatch(self):
        return self.lp.get_response_mismatch_credentials().is_displayed()
