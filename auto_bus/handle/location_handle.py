from page.location_page import LocationPage


class LocationHandle:
    def __init__(self, driver):
        self.lp = LocationPage(driver)

    # input current location
    def send_keys_current_location(self, current_location):
        self.lp.get_current_location().send_keys(current_location)

    # input destination location
    def send_keys_destination_location(self, destination_location):
        self.lp.get_destination_location().send_keys(destination_location)

    # click Depart time button
    def click_time_button(self):
        self.lp.get_time_button().click()

    # click Search button
    def click_search_button(self):
        self.lp.get_search_button().click()
