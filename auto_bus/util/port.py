from util.cmd_doc import CmdDoc


class Port:
    def __init__(self):
        self.doc = CmdDoc()

    # check if the port is used
    def if_port_used(self, port_num):
        result = self.doc.cmd_result("netstat -an |grep {}".format(port_num))
        if len(result) >= 2:
            port_used_flag = True
        else:
            port_used_flag = False
        return port_used_flag

    # create list for available port
    def create_port_for_device(self, port_number, device):
        port_list = []
        if device:
            while len(port_list) < 1:
                if not self.if_port_used(port_number):
                    port_list.append(port_number)
                else:
                    port_number += 1
            return port_list[0]
        else:
            print("No device, crate port fail")
            return None





if __name__ == '__main__':
    p = Port()
    print(p.create_port_for_device(8554,"emulator-5556"))