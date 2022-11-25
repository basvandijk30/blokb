import serial


def main():
    with serial.Serial(port="COM5", baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=1) as serial_port:
        while True:
            try:
                line = serial_port.read().decode().replace("\n\r", " ")

                print(line)
            except KeyboardInterrupt:
                break


if __name__ == "__main__":
    main()
