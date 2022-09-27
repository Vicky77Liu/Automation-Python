from appium import webdriver

from util.write_user_cmd import WriteUserCommand


class BaseDriver:

    def android_driver(self):
        write_user_cmd = WriteUserCommand()
        device_name = write_user_cmd.get_value("device_name")
        port = write_user_cmd.get_value("port")
        capabilities = {
            "platformName": "Android",
            "automationName": "UiAutomator2",  # 这样才能定位到toast
            "deviceName": device_name,
            "app": "/Users/kurt/Desktop/study/test_portnov/MobileTest/LookingBus_v0.6.23.8.apk",
            "appWaitActivity": "com.seeing_bus_user_app.activities.MainActivity",
            "noReset": "true",
            "appPackage":"com.seeing_bus_user_app"
        }
        port_name = "http://127.0.0.1:{}/wd/hub".format(port)
        driver = webdriver.Remote(port_name, capabilities)
        return driver

    def ios_driver(self):
        write_user_cmd = WriteUserCommand()
        device_name = write_user_cmd.get_value("device_name")
        port = write_user_cmd.get_value("port")
        capabilities = {
            "platformName": "Android",
            "automationName": "UiAutomator2",  # 这样才能定位到toast
            "deviceName": device_name,
            "app": "/Users/kurt/Desktop/study/test_portnov/MobileTest/LookingBus_v0.6.23.8.apk",
            "appWaitActivity": "com.seeing_bus_user_app.activities.MainActivity",
            "noReset": "true"
        }
        port_name = "http://127.0.0.1:{}/wd/hub".format(port)
        driver = webdriver.Remote(port_name, capabilities)
        return driver

    def get_driver(self, plat_form):
        if plat_form == "Android":
            return self.android_driver()
        elif plat_form == "ios":
            return self.ios_driver()
        else:
            raise KeyError("Please choose plat form from 'Android' and 'ios'!!")