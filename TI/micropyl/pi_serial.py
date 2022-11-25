#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oriëntatie op TI
Voorbeeld voor communicatie met Raspberry Pi Pico. Flash dit bestand
eerst naar de Raspberry Pi Pico. Start dan in de folder serial/PC-serial `main.py` op je laptop/PC.
(c) 2022 Hogeschool Utrecht,
Hagen Patzke (hagen.patzke@hu.nl) en
Tijmen Muller (tijmen.muller@hu.nl)
"""

from machine import ADC, Pin
import time

# Use on-board led
led = Pin(25, Pin.OUT)
temp_sensor = ADC(4)

# Blink led to confirm succesful flashing
for _ in range(5):
    led(0)
    time.sleep(.1)
    led(1)
    time.sleep(.1)

# Wait for data from the connection
while True:
    data = input()

    print("Received '" + data + "'.")
    if data == '0':
        print("Turning led off.")
        led(0)
    elif data == '1':
        print("Turning led on.")
        led(1)
    elif data == '2':
        out = temp_sensor.read_u16() * (3.3 / 65535)
        temp = 27 - (out - 0.706) / 0.001721
        print(f"Temperatuur: {temp} °C")
    else:
        print("Unknown command.")
