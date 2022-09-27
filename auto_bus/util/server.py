from util.cmd_doc import CmdDoc
from util.port import Port
from util.write_user_cmd import WriteUserCommand


class Server:
    def __init__(self):
        self.doc = CmdDoc()
        self.device = self.get_device_name()
        self.write_user_cmd = WriteUserCommand()

    # get current devices
    def get_device_name(self):
        result_list = self.doc.cmd_result("adb devices")
        if len(result_list) >= 2:
            devices = []
            for i in result_list:
                if "\tdevice" in i:
                    devices.append(i.split("\t")[0])
            return devices[0]
        else:
            return None

    # create available ports for devices
    def create_port(self, port_number):
        port = Port()
        port_number = port.create_port_for_device(port_number, self.device)
        return port_number

    # create command for appium
    def create_command(self):
        # command: appium -p 4720 -bp 5720 -U emulator-5554 --no-reset --log
        # /Users/kurt/Desktop/pythonProject/auto_bus/log/test_log.txt
        appium_port = self.create_port(4720)
        bootstrap_port = self.create_port(4721)
        command = "appium -p {} -bp {} -U {} --no-reset --log " \
                  "/Users/kurt/Desktop/pythonProject/auto_bus/log/test_log.txt " \
            .format(appium_port, bootstrap_port, self.device)
        self.write_user_cmd.write_data(self.device, bootstrap_port, appium_port)
        return command

    def start_server(self):
        self.doc.cmd_execute(self.create_command())

    # kill old process of appium
    def kill_server(self):
        result_list = self.doc.cmd_result("ps -ef |grep node")
        if len(result_list) >= 4:
            self.doc.cmd_execute("pkill node")

    def main(self):
        self.kill_server()
        self.write_user_cmd.clear_data()
        self.start_server()


if __name__ == '__main__':
    s = Server()
    s.kill_server()