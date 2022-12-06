import machine
from machine import Pin
import time

led_pins = [
    Pin(0, Pin.OUT),
    Pin(1, Pin.OUT),
    Pin(2, Pin.OUT),
    Pin(3, Pin.OUT),
    Pin(4, Pin.OUT)
]

trigger_pin = Pin(14, Pin.OUT)
echo_pin = Pin(15, Pin.IN)


def measure_distance():
    """
        Meet de afstand met de SR04
    """
    trigger_pin.value(0)
    time.sleep_us(5)

    trigger_pin.value(1)
    time.sleep_us(10)
    trigger_pin.value(0)

    pulse = machine.time_pulse_us(echo_pin, 1, 1_000_000)

    return pulse / 58


def display_distance(distance):
    """
        Laat de afstand d.m.v. de leds zien.
        1 led =  10 cm
        2 leds = 15 cm
        3 leds = 20 cm
        4 leds = 25 cm
        5 leds = 30 cm
    """
    for i in led_pins:
        i.value(0)
    if distance < 10:
        for i in led_pins:
            i.value(0)
    elif 10 < distance < 15:
        led_pins[0].value(1)
    elif 15 < distance < 20:
        led_pins[0].value(1)
        led_pins[1].value(1)
    elif 20 < distance < 25:
        for i in range(3):
            led_pins[i].value(1)
    elif 25 < distance < 30:
        for i in range(4):
            led_pins[i].value(1)
    else:
        for i in range(5):
            led_pins[i].value(1)


if __name__ == "__main__":

    while True:
        distance = measure_distance()
        display_distance(distance)
        time.sleep_ms(100)
