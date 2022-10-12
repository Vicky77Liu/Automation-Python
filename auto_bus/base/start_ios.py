from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


def main():
    base_driver = BaseDriver()
    base_driver.get_driver("ios")

if __name__ == '__main__':
    main()
