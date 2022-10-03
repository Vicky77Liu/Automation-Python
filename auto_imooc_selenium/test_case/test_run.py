
import unittest

from HTMLTestRunner import HTMLTestRunner

from test_case.login import LoginTestCase


def html_login_run():
    suite = unittest.TestSuite()
    #suite.addTest(LoginTestCase("test_success"))
    #suite.addTest(LoginTestCase("test_no_username"))
    #suite.addTest(LoginTestCase("test_no_password"))
    suite.addTest(LoginTestCase("test_mismatch_username_password"))
    runner = HTMLTestRunner(output="login", verbosity=2, title='Test report', report_name='report',
                            open_in_browser=True, description="HTMLTestReport", tested_by="Vicky Liu",
                            )
    runner.run(suite)


if __name__ == '__main__':
    html_login_run()
