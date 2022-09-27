from page.login_page import LoginPage


class LoginHandle:
    def __init__(self,driver):
        self.lp = LoginPage(driver)

    # input username
    def input_username(self, user):
        self.lp.get_username_element().send_keys(user)

    # input password
    def input_password(self, password):
        self.lp.get_password_element().send_keys(password)

    # click login button
    def click_login(self):
        self.lp.get_login_button().click()

    # click login as guest button
    def click_login_as_guest(self):
        self.lp.get_login_as_guest().click()

    # get login fail toast
    def get_login_fail_toast(self, message):
        toast_element = self.lp.get_login_fail_toast(message)
        if toast_element:
            return True
        else:
            return False