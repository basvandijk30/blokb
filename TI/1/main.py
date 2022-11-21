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


def blink():
    led_pin = Pin(20, Pin.OUT)

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

if __name__ == "__main__":
    on_off_switch()
