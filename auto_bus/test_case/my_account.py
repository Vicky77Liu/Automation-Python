import time
import unittest

from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver
from business.account_business import AccountBusiness
from business.home_business import HomeBusiness
from business.login_business import LoginBusiness
from business.navigation_business import NavigationBusiness


class MyAccount(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        dr = BaseDriver()
        cls.driver = dr.get_driver("Android")

    def setUp(self):
        self.login_business = LoginBusiness(self.driver)
        self.home_business = HomeBusiness(self.driver)
        self.navigation_business = NavigationBusiness(self.driver)
        self.account_business = AccountBusiness(self.driver)

    # log in with credentials
    def test_my_account(self):
        self.login_business.login_pass("tgsqqoa335@gaduguda.xyz", "Test!1234")
        time.sleep(3)
        self.home_business.direct_navigate()
        self.navigation_business.assert_user_id()
        self.navigation_business.nav_to_my_account()
        self.account_business.change_default_information("test111", "test222", "blind")
        self.driver.save_screenshot("../log/account_information.png")



