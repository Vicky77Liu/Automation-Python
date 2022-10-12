

from handle.login_handle import LoginHandle


class LoginBusiness:
    def __init__(self, driver):
        self.lh = LoginHandle(driver)

    def login_pass(self, username, password):
        self.lh.input_username(username)
        self.lh.input_password(password)
        self.lh.click_login()

    def login_fail(self, username, password, message):
        self.lh.input_username(username)
        self.lh.input_password(password)
        self.lh.click_login()
        return self.lh.get_login_fail_toast(message)

    def login_as_guest(self):
        self.lh.click_login_as_guest()
