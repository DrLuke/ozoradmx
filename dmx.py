import serial, time

class pyDMX:
    """Works with UART1 (ttyS1) and UART2 (ttyS2)"""
    def __init__(self, port="/dev/ttyS1"):
        self.tty = serial.Serial(port=port, stopbits=serial.STOPBITS_TWO)

    def send(self, data):
        _data = ""
        if type(data) == list:
            data = [0] + data
            _data = bytes(list(map(lambda x: int(max(0, min(255, x * 255))), data)))

        else:
            _data = data

        self.tty.baudrate = 115200
        self.tty.write("\x00".encode())
        self.tty.flush()

        self.tty.stopbits = serial.STOPBITS_TWO
        self.tty.baudrate = 250000

        self.tty.write(_data)
