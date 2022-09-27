
import unittest

from base.base_driver import BaseDriver
from business.login_business import LoginBusiness


class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        dr = BaseDriver()
        cls.driver = dr.get_driver("Android")

    def setUp(self):
        self.login_business = LoginBusiness(self.driver)

    # log in fail
    def test_login_fail(self):
        result = self.login_business.login_fail("123@gmail.com", "1111", "illegal information")
        self.assertTrue(result)
        self.driver.save_screenshot("../log/login_fail_finish.png")

    # log in as guest
    def test_login_as_guest(self):
        self.login_business.login_as_guest()
        self.driver.save_screenshot("../log/login_guest_finish.png")

    # log in success
    def test_login_success(self):
        self.login_business.login_pass("tgsqqoa335@gaduguda.xyz", "Test!1234")
        self.driver.save_screenshot("../log/login_success_finish.png")

    @classmethod
    def tearDownClass(cls):
        print("finish")
