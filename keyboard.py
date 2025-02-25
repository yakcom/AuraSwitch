import hid

class Keyboard:

    def __init__(self,vid,pid):
        device = hid.enumerate(vid, pid)
        if len(device) == 0:raise Exception('No device found')
        self.device = device

    def send(self, data, iid):
        interface = next((dev for dev in self.device if dev['interface_number'] == int(iid)), None)
        if not interface:raise Exception('No interface found')
        device = hid.device()
        device.open_path(interface['path'])
        device.write(data)
        device.close()




