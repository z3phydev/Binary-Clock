from machine import Pin, I2C
import utime

class DS3231:
    def __init__(self, i2c, addr=0x68):
        self.i2c = i2c
        self.addr = addr
    def bcd2dec(self, b):
        return (b >> 4) * 10 + (b & 0x0F)
    def read_time(self):
        data = self.i2c.readfrom_mem(self.addr, 0x00, 7)
        s = self.bcd2dec(data[0])
        m = self.bcd2dec(data[1])
        h = self.bcd2dec(data[2] & 0x3F)
        return h, m, s

i2c = I2C(0, scl=Pin(5), sda=Pin(4))
rtc = DS3231(i2c)

led_map = {
    "h10": [Pin(2, Pin.OUT), Pin(1, Pin.OUT)],
    "h1":  [Pin(8, Pin.OUT), Pin(7, Pin.OUT), Pin(6, Pin.OUT), Pin(3, Pin.OUT)],
    "m10": [Pin(11, Pin.OUT), Pin(10, Pin.OUT), Pin(9, Pin.OUT)],
    "m1":  [Pin(15, Pin.OUT), Pin(14, Pin.OUT), Pin(13, Pin.OUT), Pin(12, Pin.OUT)],
    "s10": [Pin(18, Pin.OUT), Pin(17, Pin.OUT), Pin(16, Pin.OUT)],
    "s1":  [Pin(22, Pin.OUT), Pin(21, Pin.OUT), Pin(20, Pin.OUT), Pin(19, Pin.OUT)],
}

def show_binary(value, pins):
    for i, p in enumerate(pins):
        p.value((value >> i) & 1)

def get_hour_12_24(hour, use_24):
    if use_24:
        return hour
    h12 = hour % 12
    return 12 if h12 == 0 else h12

switch = Pin(0, Pin.IN, Pin.PULL_UP)
use_24 = True
last_state = 1

while True:
    state = switch.value()
    if state == 0 and last_state == 1:
        use_24 = not use_24
        utime.sleep(0.2)
    last_state = state

    h, m, s = rtc.read_time()
    h = get_hour_12_24(h, use_24)

    show_binary(h // 10, led_map["h10"])
    show_binary(h % 10, led_map["h1"])
    show_binary(m // 10, led_map["m10"])
    show_binary(m % 10, led_map["m1"])
    show_binary(s // 10, led_map["s10"])
    show_binary(s % 10, led_map["s1"])

    utime.sleep(0.2)
