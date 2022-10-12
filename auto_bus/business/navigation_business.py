from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from handle.navigation_handle import NavigationHandle


class NavigationBusiness:
    def __init__(self, driver):
        self.driver = driver
        self.nh = NavigationHandle(self.driver)

    # if the user id is displayed
    def assert_user_id(self):
        return self.nh.assert_user_id()

    # navigate to my account page
    def nav_to_my_account(self):
        self.nh.click_my_account()
        account_first_name = ("id", "com.seeing_bus_user_app:id/first_name")
        WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located(account_first_name))

    # navigate to home page
    def nav_to_home(self):
        self.nh.click_home()

