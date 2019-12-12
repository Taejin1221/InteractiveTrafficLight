# InteractiveTrafficLight.py
import RPi.GPIO as GPIO

carLED = { 'RED' : 14, 'YELLOW' : 15, 'GREEN' : 18 }
pedLED = { 'RED' : 23, 'GREEN' : 24 }
button = 8

GPIO.setmode(GPIO.BCM)

# Set LED pin to OUT
for i in carLED:
	GPIO.setup(carLED[i], GPIO.OUT)

for i in pedLED:
	GPIO.setup(pedLED[i], GPIO.OUT)

# Set Button pin to IN
GPIO.setup(button, GPIO.IN)