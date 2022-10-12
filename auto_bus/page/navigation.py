from util.get_locator import GetLocator


class NavigationPage:
    def __init__(self, driver):
        self.locator = GetLocator(driver)

    # get user number
    def get_user_number(self):
        return self.locator.get_element("navigation_drawer", "navigation_id")

    # get My Account
    def get_my_account(self):
        return self.locator.get_element("navigation_drawer", "user_account")

    # get Home
    def get_home(self):
        return self.locator.get_element("navigation_drawer", "home")

    # get My Reservation
    def get_my_reservation(self):
        return self.locator.get_element("navigation_drawer", "reservation")

    # get My Places
    def get_my_places(self):
        self.locator.get_element("navigation_drawer", "places")

    # get Settings
    def get_settings(self):
        return self.locator.get_element("navigation_drawer", "settings")

    # get Feedback
    def get_feedback(self):
        return self.locator.get_element("navigation_drawer", "feedback")

    # get log out
    def get_log_out(self):
        return self.locator.get_element("navigation_drawer", "log_out")
