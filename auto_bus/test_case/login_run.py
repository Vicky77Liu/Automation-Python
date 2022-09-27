import time
import unittest

from HTMLTestRunner.runner import HTMLTestRunner

from test_case.test_login import Login
from util.server import Server


def appium_init():
    server = Server()
    server.main()


def get_suite():
    suite = unittest.TestSuite()
    suite.addTest(Login("test_login_fail"))
    # suite.addTest(Login("test_login_as_guest"))
    # suite.addTest(Login("test_login_success"))
    # unittest.TextTestRunner().run(suite)
    runner = HTMLTestRunner(log=True, output='report', title='Test report', report_name='login_module',
                            open_in_browser=True, description="HTMLTestReport", tested_by="Vicky Liu",
                            add_traceback=False)
    runner.run(suite)


if __name__ == '__main__':
    appium_init()
    time.sleep(3)
    get_suite()
