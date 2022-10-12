from business.home_business import HomeBusiness
from handle.location_handle import LocationHandle


class LocationBusiness:
    def __init__(self, driver):
        self.hb = HomeBusiness(driver)
        self.lh = LocationHandle(driver)

    def set_locations(self, current_location, destination_location):
        self.lh.send_keys_current_location(current_location)
        self.lh.send_keys_destination_location(destination_location)
        self.lh.click_search_button()
