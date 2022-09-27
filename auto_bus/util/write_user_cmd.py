import yaml
from yaml import SafeLoader


class WriteUserCommand:

    # read yaml file
    def read_data(self):
        with open("../config/user_info.yaml") as file:
            user_info = yaml.load(file, Loader=SafeLoader)
        return user_info

    # key:device_name/port/bp
    def get_value(self, key):
        user_info = self.read_data()
        value = user_info["user_info"][key]
        return value

    def join_data(self, device, bp, port):
        user_info = {
            "user_info": {
                "device_name": device,
                "bp": bp,
                "port": port
            }
        }
        return user_info

    # write data to yaml file
    def write_data(self,device, bp, port):
        user_info = self.join_data(device, bp, port)
        with open("../config/user_info.yaml", "a") as file:
            yaml.dump(user_info, file)

    # clear all of data in the file
    def clear_data(self):
        with open("../config/user_info.yaml", "w") as file:
            file.truncate()
        file.close()



if __name__ == '__main__':
    write = WriteUserCommand()
    data = write.read_data()
    write.clear_data()
    #print(write.get_value('device_name'))