import serial
from serial.tools import list_ports

serial_ports = list_ports.comports()
print("[INFO] Serial ports found:")
for i, port in enumerate(serial_ports):
    print(str(i) + ". " + str(port.device))
pico_port_index = int(input("Which port is the Raspberry Pi Pico connected to? "))
pico_port = serial_ports[pico_port_index].device


def read_serial(port):
    """Read data from serial port and return as string."""
    line = port.read(1000)
    return line.decode()


with serial.Serial(port=pico_port, baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=1) as serial_port:
    if serial_port.isOpen():
        print("[INFO] Using serial port", serial_port.name)
    else:
        print("[INFO] Opening serial port", serial_port.name, "...")
        serial_port.open()

    try:
        while True:
            data = read_serial(serial_port)
            print(data)
    except KeyboardInterrupt:
        pass
