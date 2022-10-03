from base.find_element import FindElement


class HomePage:
    def __init__(self, driver):
        self.fd = FindElement(driver)

    # get login element
    def get_login(self):
        return self.fd.get_element("login")

    # get header avator element
    def get_header_avator(self):
        return self.fd.get_element("header_avator")
