from page.home_page import HomePage


class HomeHandle:
    def __init__(self, driver):
        self.hp = HomePage(driver)

    # click hamburger icon
    def click_hamburger_icon(self):
        self.hp.get_hamburger_icon().click()

    # click Pick a destination
    def click_pick_destination(self):
        self.hp.get_pick_destination().click()

    # get route element
    def get_route(self):
        return self.hp.get_route()


