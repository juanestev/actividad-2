from machine import ADC, Pin
from time import sleep

adc = ADC(pin(26))
while True: 
    var1 = adc.read_u16()
    var2 = var1 * 3.3 / 65535
    var3 = var2 * 1 / 0.01
    print("{:.2f}".format(var3))
    sleep(2)