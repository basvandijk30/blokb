import time

from machine import Pin

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


def kitt(led_pins, delay):
    rev = 1  # Heenweg +1, terugweg -1. Vermenigvuldig met index.
    x, _ = 0, 1  # Extra switch waarde om op terugweg af te trekken van index zodat de uiteindes niet dubbel knipperen.
    while True:
        for i in range(0, len(led_pins) - 1):
            led_pins[i * rev - x].value(1)
            time.sleep(delay)
            led_pins[i * rev - x].value(0)
            time.sleep(delay)
        rev = -rev
        x, _ = _, x


if __name__ == "__main__":
    kitt(LED_PINS, 0.08)
    # delay = 0.2
    # while True:
    #     leds(1, delay)
    #     leds(2, delay)
    #     leds(4, delay)
    #     leds(8, delay)
    #     leds(16, delay)
