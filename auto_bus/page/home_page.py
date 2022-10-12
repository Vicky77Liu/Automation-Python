from util.get_locator import GetLocator


class HomePage:
    def __init__(self, driver):
        self.locator = GetLocator(driver)

    # get hamburger icon to navigation drawer
    def get_hamburger_icon(self):
        return self.locator.get_element("home", "hamburger")

    # get Pick a destination
    def get_pick_destination(self):
        return self.locator.get_element("home","pick_destination")

    # get route element
    def get_route(self):
        return self.locator.get_element("home","route")
    