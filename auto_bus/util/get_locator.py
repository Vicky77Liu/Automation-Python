from selenium.webdriver.common.by import By

from util.read_ini import ReadIni


class GetLocator:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, key):
        read_ini = ReadIni()
        locator = read_ini.get_value(key)
        if locator is not None:
            by = locator.split(">")[0]
            value = locator.split(">")[1]
            if by == "id":
                return self.driver.find_element(By.ID, value)
            elif by == "class_name":
                return self.driver.find_element(By.CLASS_NAME, value)
            else:
                return self.driver.find_element(By.XPATH, value)
        else:
            return None
