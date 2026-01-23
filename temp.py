class Device:
    def __init__(self):
        self._voltage = 0

    def get_voltage(self):
        return self._voltage

    def set_voltage(self, new_voltage):
        self._voltage = new_voltage


dev_1 = Device(3)

print(dev_1.get_voltage())