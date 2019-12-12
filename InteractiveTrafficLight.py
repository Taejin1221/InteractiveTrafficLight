# InteractiveTrafficLight.py
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
	pass

# Webpage 
webRed = """
<script>
function GreenLight() {
	window.location.href = '/PedGreen'
} 
</script>

Interactive Button: 
<input type = 'button' onClick = 'GreenLight()' value = 'ON' />
"""

webGreen = """
<script>
window.location.href = '/PedRed'
</script>
"""

@route('/')
@route('/PedRed')
def index():
	return webRed

@route('/PedGreen')
def index():
	PedGreen()
	return webGreen

run(host = 'localhost', port = 8080)