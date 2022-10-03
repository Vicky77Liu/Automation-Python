from selenium import webdriver


class DriverBase:

    def get_driver(self, browser):
        if browser == "safari":
            return webdriver.Safari()
        else:
            chrome_path = "/Users/kurt/Desktop/study/seleniumTest/chromedriver"
            return webdriver.Chrome(executable_path=chrome_path)
