import time

from machine import ADC, Pin

LED_PINS = [
    Pin(0, Pin.OUT),
    Pin(1, Pin.OUT),
    Pin(2, Pin.OUT),
    Pin(3, Pin.OUT),
    Pin(4, Pin.OUT)
]


def leds(value, delay):
    for led in LED_PINS:
        if value % 2 == 1:
            led.value(1)
        else:
            led.value(0)
        value = value // 2
    time.sleep(delay)


def kitt(led_pins, delay, n):
    rev = 1  # Heenweg +1, terugweg -1. Vermenigvuldig met index.
    x, _ = 0, 1  # Extra switch waarde om op terugweg af te trekken van index zodat de uiteindes niet dubbel knipperen.
    run = 0
    while run < n:
        for i in range(0, len(led_pins) - 1):
            led_pins[i * rev - x].value(1)
            time.sleep(delay)
            led_pins[i * rev - x].value(0)
            time.sleep(delay)
        rev = -rev
        x, _ = _, x
        run += 1


if __name__ == "__main__":
    temp_sensor = ADC(4)
    internal_led = Pin(25, Pin.OUT)

    while True:
        data = input()

        print("Received '" + data + "'.")
        if data == '0':
            print("Turning led off.")
            internal_led(0)
        elif data == '1':
            print("Turning led on.")
            internal_led(1)
        elif data == '2':
            out = temp_sensor.read_u16() * (3.3 / 65535)
            temp = 27 - (out - 0.706) / 0.001721
            print(f"Temperatuur: {temp} °C")
        elif data == '3':
            kitt(LED_PINS, 0.08, 10)
        else:
            print("Unknown command.")
