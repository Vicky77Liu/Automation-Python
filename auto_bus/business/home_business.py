from handle.home_handle import HomeHandle


class HomeBusiness:
    def __init__(self, driver):
        self.hh = HomeHandle(driver)

    # click hamburger icon then navigate to navigation drawer
    def direct_navigate(self):
        self.hh.click_hamburger_icon()

    # click Pick a destination and navigate to location page
    def direct_location(self):
        self.hh.click_pick_destination()

    # assert route element is displayed
    def assert_route(self):
        if self.hh.get_route().is_displayed():
            return True
        return False

