# get packages to help us
import gpiozero
import time

# set up each of the relay pins as outputs
relay_1 = gpiozero.OutputDevice(4)
relay_2 = gpiozero.OutputDevice(17)
relay_3 = gpiozero.OutputDevice(27)
relay_4 = gpiozero.OutputDevice(22)

# toggle relay 1!
print('Turn on 1!')
relay_1.on()
time.sleep(10)
print('Turn off 1!')
relay_1.off()
time.sleep(10)

# toggle relay 2!
print('Turn on 2!')
relay_2.on()
time.sleep(10)
print('Turn off 2!')
relay_2.off()
time.sleep(10)

# toggle relay 3!
print('Turn on 3!')
relay_3.on()
time.sleep(10)
print('Turn off 3!')
relay_3.off()
time.sleep(10)

# toggle relay 4!
print('Turn on 4!')
relay_4.on()
time.sleep(10)
print('Turn off 4!')
relay_4.off()
