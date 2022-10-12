import time
import unittest

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_driver import BaseDriver
from business.home_business import HomeBusiness
from business.location_business import LocationBusiness
from business.login_business import LoginBusiness


class TestLocation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        dr = BaseDriver()
        cls.driver = dr.get_driver("Android")

    def setUp(self):
        self.login_business = LoginBusiness(self.driver)
        self.home_business = HomeBusiness(self.driver)
        self.location_business = LocationBusiness(self.driver)

    def test_location(self):
        self.login_business.login_as_guest()
        element = ("id", "com.seeing_bus_user_app:id/search_address_box")
        self.wait_element(element)
        self.home_business.direct_location()
        element = ("id", "com.seeing_bus_user_app:id/edit_origin")
        self.wait_element(element)
        current = "Apple Park Way, Cupertino, California, United States, 95014"
        destination = "Google Building 43, Charleston Road, Mountain View, California, United States, 94043"
        self.location_business.set_locations(current, destination)
        element = ("class", "android.view.ViewGroup")
        self.wait_element(element)
        self.driver.save_screenshot("../log/locations.png")

    def wait_element(self,element):
        WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located(element))
