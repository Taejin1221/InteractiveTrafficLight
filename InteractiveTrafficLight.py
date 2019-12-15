# InteractiveTrafficLight.py
from time import sleep
from bottle import route, run, template
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

def PedGreen():
	GPIO.output(carLED['GREEN'], False)
	GPIO.output(carLED['YELLOW'], True)
	sleep(1)
	GPIO.output(carLED['YELLOW'], False)
	GPIO.output(carLED['RED'], True)

	GPIO.output(pedLED['RED'], False)
	GPIO.output(pedLED['GREEN'], True)
	sleep(4)
	GPIO.output(pedLED['GREEN'], False)
	GPIO.output(pedLED['RED'], True)

# Webpage 
webRed = """
<script>
var myTimer;

function GreenLight() {
	clearTimeout(myTimer);
	document.write("It's green light");
	window.location.href = '/PedGreen';
} 
</script>

Interactive Button: 
<input type = 'button' onClick = 'GreenLight()' value = 'ON' />

<script>
myTimer = setTimeout(GreenLight, 6000);
"""

webGreen = """
<script>
window.location.href = '/PedRed';
</script>
"""

@route('/')
@route('/PedRed')
def index():
	sleep(1)
	GPIO.output(carLED['RED'], False)
	GPIO.output(carLED['GREEN'], True)
	return webRed

@route('/PedGreen')
def index():
	PedGreen()
	return webGreen

run(host = 'localhost', port = 8080)
