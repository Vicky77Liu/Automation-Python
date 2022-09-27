import subprocess
import sys
import time


class CmdDoc:
    def cmd_result(self, command):
        rest = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True).stdout.read()
        rest = rest.decode()
        list_devices = []
        if rest is not None:
            list_devices = rest.split("\n")
            return list_devices
        else:
            return list_devices

    def cmd_execute(self, command):
        subprocess.Popen(command, shell=True)




if __name__ == '__main__':
    doc = CmdDoc()
    # re = doc.cmd_result("ps -ef | grep node")
    doc.cmd_execute("pkill node")
    # re = doc.cmd_result("ls")
    # print(re)
    # print(len(re))
