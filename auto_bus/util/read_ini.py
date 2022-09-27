import configparser


class ReadIni:
    def __init__(self, file_path=None, section=None):
        if file_path is None:
            self.file_path = "/Users/kurt/Desktop/pythonProject/appium/config/locate_element.ini"
        else:
            self.file_path = file_path
        if section is None:
            self.section = "login_element"
        else:
            self.section = section
        self.data = self.load_ini()

    def load_ini(self):
        read_ini = configparser.ConfigParser()
        read_ini.read(self.file_path)
        return read_ini

    def get_value(self, key):
        try:
            value = self.data.get(self.section, key)
        except:
            value = None
        return value


if __name__ == '__main__':
    i = ReadIni()
    print(i.get_value("username"))