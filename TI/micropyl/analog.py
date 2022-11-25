import time

from machine import ADC, PWM, Pin


def potmeter(led_pin, adc_pin):
    led = PWM(led_pin)
    led.freq(1000)
    adc = ADC(adc_pin)

    val = adc.read_u16()
    led.duty_u16(val)
    time.sleep(0.01)


def inv_potmeter(led_pin, adc_pin):
    led = PWM(led_pin)
    led.freq(1000)
    adc = ADC(adc_pin)

    val = 65535 - adc.read_u16()
    led.duty_u16(val)
    time.sleep(0.01)


def blink_potmeter(led_pin, adc_pin):
    adc = ADC(adc_pin)
    val = adc.read_u16()

    blink = val / 65535
    pulse(led_pin, blink, blink)
    time.sleep(0.01)


def pulse(pin, uptime, downtime):
    pin.value(1)
    time.sleep(uptime)
    pin.value(0)
    time.sleep(downtime)


if __name__ == "__main__":
    ledpin, adcpin = Pin(16, Pin.OUT), Pin(26)
    while True:
        potmeter(ledpin, adcpin)
