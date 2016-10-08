from gpiozero import *
from time import sleep

relay_4 = OutputDevice(22)
relay_3 = OutputDevice(27)
relay_2 = OutputDevice(17)
relay_1 = OutputDevice(4)

print('Turn on 1!')
relay_1.on()
sleep(1)
print('Turn off 1!')
relay_1.off()

sleep(1)
print('Turn on 2!')
relay_2.on()
sleep(1)
print('Turn off 2!')
relay_2.off()

sleep(1)
print('Turn on 3!')
relay_3.on()
sleep(1)
print('Turn off 3!')
relay_3.off()

sleep(1)
print('Turn on 4!')
relay_4.on()
sleep(1)
print('Turn off 4!')
relay_4.off()
