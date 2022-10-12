import time

from handle.account_handle import AccountHandle


class AccountBusiness:
    def __init__(self, driver):
        self.ah = AccountHandle(driver)

    # change information
    def change_default_information(self, first_name, last_name, special_condition):
        self.ah.clear_first_name()
        self.ah.send_keys_first_name(first_name)
        self.ah.clear_last_name()
        self.ah.send_keys_last_name(last_name)
        self.ah.click_special_condition()
        time.sleep(1)
        if special_condition == "blind":
            self.ah.click_condition_blind()
        elif special_condition == "visually_impaired":
            self.ah.click_condition_visually_impaired()
        elif special_condition == "wheel_chair":
            self.ah.click_condition_wheel_chair()
        else:
            self.ah.click_special_condition()
        self.ah.click_check_mark_button()

    # back to navigation drawer
    def back_navigation(self):
        self.ah.click_hamburger_button()

