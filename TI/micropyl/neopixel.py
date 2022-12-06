import math
import time

import machine
import neopixel

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
OFF = (0, 0, 0)


def looplight(np, delay):
    while True:
        for i in range(8):
            np[i] = RED
            np.write()
            time.sleep(delay)
        for i in range(8):
            np[i] = GREEN
            np.write()
            time.sleep(delay)
        for i in range(8):
            np[i] = OFF
        np.write()
        time.sleep(delay)


def thingy(np, delay):
    """
    1: 0 t/m 7 aan en uit
    2: als 7: desc
    3: als 0: asc
    """
    rev = 1
    x, _ = 0, 1
    while True:
        for i in range(7):
            np[i * rev - x] = GREEN
            np.write()
            time.sleep(delay)
            np[i * rev - x] = OFF
            np.write()
            time.sleep(delay)
        rev = -rev
        x, _ = _, x


def rainbow(np, l):

    for g in range(256):
        np[l] = (255, g, 0)
        np.write()
        time.sleep(0.01)
    for r in reversed(range(256)):
        np[l] = (r, 255, 0)
        np.write()
        time.sleep(0.01)
    for b in range(256):
        np[l] = (0, 255, b)
        np.write()
        time.sleep(0.01)
    for g in reversed(range(256)):
        np[l] = (0, g, 255)
        np.write()
        time.sleep(0.01)
    for r in range(256):
        np[l] = (r, 0, 255)
        np.write()
        time.sleep(0.01)
    for b in reversed(range(256)):
        np[l] = (255, 0, b)
        np.write()
        time.sleep(0.01)


if __name__ == "__main__":
    np = neopixel.NeoPixel(machine.Pin(13), 8)
    thingy(np, 0.08)
    # while True:
    #     rainbow(np, 7)
