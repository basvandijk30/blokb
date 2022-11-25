from machine import Pin
import time


def on_off_switch():
    led_pin = Pin(20, Pin.OUT)
    switch_pin = Pin(19, Pin.IN, pull=Pin.PULL_DOWN)
    value = 0

    while True:
        if switch_pin.value():
            if value == 1:
                value = 0
            else:
                value = 1
            led_pin.value(value)
        time.sleep(0.1)


def blink(pin):
    led_pin = Pin(pin, Pin.OUT)

    while True:
        time.sleep(0.5)
        led_pin.value(1)
        time.sleep(0.5)
        led_pin.value(0)

def switch():
    led_pin = Pin(20, Pin.OUT)
    switch_pin = Pin(19, Pin.IN, pull=Pin.PULL_DOWN)

    while True:
        if switch_pin.value():
            led_pin.value(1)
        else:
            led_pin.value(0)
        time.sleep(0.1)


def on_off_switches():
    led_pin = Pin(20, Pin.OUT)
    on_switch_pin = Pin(19, Pin.IN, pull=Pin.PULL_DOWN)
    off_switch_pin = Pin(18, Pin.IN, pull=Pin.PULL_DOWN)

    state = 0

    while True:
        if on_switch_pin.value() and state == 0:
            led_pin.value(1)
            state = 1
        elif off_switch_pin.value() and state == 1:
            led_pin.value(0)
            state = 0
        time.sleep(0.1)


def pulse(pin: Pin, high_time: float, low_time: float):
    pin.value(1)
    time.sleep(high_time)
    pin.value(0)
    time.sleep(low_time)


def tatatataaa():
    led_pin = Pin(20, Pin.OUT)
    short = 0.1
    long = 1

    for _ in range(3):
        led_pin.value(1)
        time.sleep(short)
        led_pin.value(0)
        time.sleep(short)

    led_pin.value(1)
    time.sleep(long)
    led_pin.value(0)
    time.sleep(long)


def morse(pin, dot_length, text):
    """
    Laat de text horen als morse code.
    De pin is de pin die gebruikt wordt.
    De text mag de volgende characters bevatten: spatie, streepje, punt.
    De dot_length is de lengte van een punt (dot).
    De lengte van de andere characters wordt daar van afgeleid.
    """
    chars = (".", "_", " ")
    short = dot_length
    long = dot_length * 3

    for c in text:
        try:
            ind = chars.index(c)
        except ValueError:
            continue

        if ind < 2:
            pin.value(1)
            time.sleep((short, long)[ind])
            pin.value(0)
            time.sleep(short)
        else:
            time.sleep(long)


if __name__ == "__main__":
    morse(Pin(16), 0.3, "_... ._ ...")
