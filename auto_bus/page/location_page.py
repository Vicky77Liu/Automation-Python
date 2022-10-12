from util.get_locator import GetLocator


class LocationPage:
    def __init__(self, driver):
        self.get_locator = GetLocator(driver)

    # get current location text field
    def get_current_location(self):
        return self.get_locator.get_element("location", "current")

    # get destination location text field
    def get_destination_location(self):
        return self.get_locator.get_element("location", "destination")

    # get Depart time button
    def get_time_button(self):
        return self.get_locator.get_element("location", "time")

    # get search button
    def get_search_button(self):
        return self.get_locator.get_element("location", "search")
