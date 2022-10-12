import time
import unittest

from HTMLTestRunner.runner import HTMLTestRunner

from test_case.my_account import MyAccount
from test_case.test_location import TestLocation
from test_case.test_login import Login
from util.server import Server


def appium_init():
    server = Server()
    server.main()


def log_in_run():
    suite = unittest.TestSuite()
    suite.addTest(Login("test_login_fail"))
    # suite.addTest(Login("test_login_as_guest"))
    # suite.addTest(Login("test_login_success"))
    # unittest.TextTestRunner().run(suite)
    runner = HTMLTestRunner(log=True, output='report', title='login', report_name='login',
                            open_in_browser=True, description="HTMLTestReport", tested_by="Vicky Liu",
                            add_traceback=False)
    runner.run(suite)


def account_run():
    suite = unittest.TestSuite()
    suite.addTest(MyAccount("test_my_account"))
    runner = HTMLTestRunner(log=True, output='report', title='account', report_name='account_module',
                            open_in_browser=True, description="HTMLTestReport", tested_by="Vicky Liu",
                            add_traceback=False)
    runner.run(suite)


def location_run():
    suite = unittest.TestSuite()
    suite.addTest(TestLocation("test_location"))
    runner = HTMLTestRunner(log=True, output='report', title='account', report_name='account_module',
                            open_in_browser=True, description="HTMLTestReport", tested_by="Vicky Liu",
                            add_traceback=False)
    runner.run(suite)


if __name__ == '__main__':
    appium_init()
    time.sleep(3)
    location_run()
