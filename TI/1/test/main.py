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


def pulse(pin, high_time, low_time):
    pin.value(1)
    time.sleep(high_time)
    pin.value(0)
    time.sleep(low_time)


if __name__ == "__main__":
    morse(Pin(16), 0.3, "_... ._ ...")

