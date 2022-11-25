import time

from machine import Pin


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


def blink(pin):
    pin.value(1)
    time.sleep(0.5)
    pin.value(0)
    time.sleep(0.5)


def tatatataaa(pin, short, long):

    for _ in range(3):
        pulse(pin, short, short)

    pulse(pin, long, long)


def pulse(pin, uptime, downtime):
    pin.value(1)
    time.sleep(uptime)
    pin.value(0)
    time.sleep(downtime)


def on_off_switch(led_pin, switch_pin):
    value = 0

    while True:
        if switch_pin.value():
            if value == 1:
                value = 0
            else:
                value = 1
            led_pin.value(value)
        time.sleep(0.1)


def on_off_switches(led_pin, on_pin, off_pin):
    state = 0

    while True:
        if on_pin.value() and state == 0:
            led_pin.value(1)
            state = 1
        elif off_pin.value() and state == 1:
            led_pin.value(0)
            state = 0
        time.sleep(0.1)


if __name__ == "__main__":
    # n_off_switch(Pin(20, Pin.OUT), Pin(17, Pin.IN, pull=Pin.PULL_DOWN))
    on_off_switches(Pin(20, Pin.OUT), Pin(17, Pin.IN, pull=Pin.PULL_DOWN), Pin(16, Pin.IN, pull=Pin.PULL_DOWN))
    # morse(Pin(20, Pin.OUT), 0.3, "_... ._ ...")
