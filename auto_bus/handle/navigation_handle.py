from page.navigation import NavigationPage


class NavigationHandle:
    def __init__(self, driver):
        self.np = NavigationPage(driver)

    # assert if user id is displayed
    def assert_user_id(self):
        return self.np.get_user_number().is_displayed()

    # click My Account
    def click_my_account(self):
        self.np.get_my_account().click()

    # click Home
    def click_home(self):
        self.np.get_home().click()

    # click My Reservation
    def click_my_reservation(self):
        self.np.get_my_reservation().click()

    # click Settings
    def click_settings(self):
        self.np.get_settings().click()

    # click Feedback
    def click_feedback(self):
        self.np.get_feedback().click()

    # click log out
    def click_log_out(self):
        self.np.get_log_out().click()
