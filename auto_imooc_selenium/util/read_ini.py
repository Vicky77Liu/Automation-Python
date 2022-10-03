import configparser


class ReadIni:
    def __init__(self, file_name=None, node=None):
        if file_name is None:
            file_name = "/Users/kurt/Desktop/selenium/config/elements.ini"
        if node is None:
            self.node = "LoginElement"
        else:
            self.node = node
        self.cf = self.load_ini(file_name)

    # load file
    def load_ini(self, file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf

    # get value
    def get_value(self, key):
        data = self.cf.get(self.node, key)
        return data


"""if __name__ == '__main__':
    ri = ReadIni()
    a = ri.get_value("username")
    print(a)"""
