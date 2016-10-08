# Quick Start Relays

Code for hands-on workshops at the [Houston Raspberry Pi Jam: Practical Applications for Relays](http://www.meetup.com/Houston-Raspberry-Pi-Users-Group/events/231550557/)

# How to run

If you have Jessie on your Raspberry Pi, you should be able to download this and run the code from downloaded folder like this:

```sh
python simple-GPIO.py
python simple-gpiozero.py
```

If you get errors called `ImportErrors` about missing modules, you should be to run the code by running:

```sh
pip install RPi.GPIO
pip install gpiozero
```

on your Raspberry Pi.

# Hardware

While this code is written specifically for use with [Robogaia 4 Relays Raspberry Pi Shield](http://www.robogaia.com/4-relays-raspberry-pi-plateshield.html), you can run it to control any relay by switching out the pin numbers.
