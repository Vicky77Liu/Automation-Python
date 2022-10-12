import yaml


class ReadElementYaml:
    # read yaml file
    def read_data(self):
        with open("../config/locate_element.yaml", "r") as file:
            element = yaml.safe_load(file)
        return element

    def get_value(self, section, key):
        element = self.read_data()
        element_value = element[section][key]
        return element_value


if __name__ == '__main__':
    data = ReadElementYaml()
    value = data.get_value("navigation_drawer", "hamburger")
    print(value)
