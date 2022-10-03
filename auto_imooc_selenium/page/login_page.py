

from base.find_element import FindElement


class LoginPage:
    def __init__(self, driver):
        self.fd = FindElement(driver)

    # get username input field
    def get_username(self):
        return self.fd.get_element("username")

    # get password input field
    def get_password(self):
        return self.fd.get_element("password")

    # get login button
    def get_login_button(self):
        return self.fd.get_element("login_button")

    # no input for username, click login button, get the responds element
    def get_response_no_username_inputs(self):
        return self.fd.get_element("no_input_username")

    # no input for password, click login button, get the responds element
    def get_response_no_password_inputs(self):
        return self.fd.get_element("no_input_password")

    # mismatch inputs for username and password, click login button, get the responds element
    # 3 different responses
    def get_response_mismatch_credentials(self):
        if self.fd.get_element("mismatch_inputs"):
            return self.fd.get_element("mismatch_inputs")
        elif self.fd.get_element("mismatch_inputs_2"):
            return self.fd.get_element("mismatch_inputs_2")
        else:
            return self.fd.get_element("mismatch_inputs_3")
