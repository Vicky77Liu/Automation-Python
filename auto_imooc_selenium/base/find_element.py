from selenium.webdriver.common.by import By

from log.user_log import UserLog
from util.read_ini import ReadIni


class FindElement:
    def __init__(self, driver):
        self.driver = driver
        logger = UserLog()
        self.logger = logger.get_log()

    def get_element(self, key):
        read_ini = ReadIni()
        data = read_ini.get_value(key)
        by = data.split(">")[0]
        value = data.split(">")[1]
        try:
            if by == "id":
                return self.driver.find_element(By.ID, value)
            elif by == "name":
                return self.driver.find_element(By.NAME, value)
            elif by == "className":
                return self.driver.find_element(By.CLASS_NAME, value)
            elif by == "tagName":
                return self.driver.find_element(By.TAG_NAME, value)
            elif by == "linkText":
                return self.driver.find_element(By.LINK_TEXT, value)
            else:
                return self.driver.find_element(By.XPATH, value)
        except:
            return None
