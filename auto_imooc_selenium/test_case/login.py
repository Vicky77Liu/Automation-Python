import os.path
import time
import unittest

from base.driver_base import DriverBase
from business.login_business import LoginBusiness
from log.user_log import UserLog


class LoginTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        dr = DriverBase()
        cls.log = UserLog()
        cls.logger = cls.log.get_log()
        cls.driver = dr.get_driver("chrome")
        cls.driver.get("https://www.imooc.com/")
        cls.driver.maximize_window()

    def setUp(self):
        self.driver.refresh()
        self.logger.info("this is chrome")
        self.login = LoginBusiness(self.driver)

    def tearDown(self):
        time.sleep(2)
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(os.getcwd() + "/report/" + case_name + "_error.png")
                self.driver.save_screenshot(file_path)

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()
        cls.driver.close()
        cls.driver.quit()

    def test_success(self):
        result = self.login.login_success("nirvanawgw@gmail.com", "987654321QWER")
        self.assertTrue(result)
        case_name = self._testMethodName
        file_path = os.path.join(os.getcwd() + "/report/" + case_name + ".png")
        self.driver.save_screenshot(file_path)

    def test_no_username(self):
        no_input_username_response = self.login.no_username_input("", "12345678")
        self.assertTrue(no_input_username_response)
        case_name = self._testMethodName
        file_path = os.path.join(os.getcwd() + "/report/" + case_name + ".png")
        self.driver.save_screenshot(file_path)

    def test_no_password(self):
        no_input_password_response = self.login.no_password_input("abac@gmail.com", "")
        self.assertTrue(no_input_password_response)
        case_name = self._testMethodName
        file_path = os.path.join(os.getcwd() + "/report/" + case_name + ".png")
        self.driver.save_screenshot(file_path)

    def test_mismatch_username_password(self):
        mismatch_inputs = self.login.mismatch_inputs("nirvanawgw@gmail.com", "123456789")
        self.assertTrue(mismatch_inputs)
        case_name = self._testMethodName
        file_path = os.path.join(os.getcwd() + "/report/" + case_name + ".png")
        self.driver.save_screenshot(file_path)
