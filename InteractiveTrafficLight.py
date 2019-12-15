# InteractiveTrafficLight.py
from time import sleep
from bottle import route, run
import RPi.GPIO as GPIO

carLED = { 'RED' : 14, 'YELLOW' : 15, 'GREEN' : 18 }
pedLED = { 'RED' : 23, 'GREEN' : 24 }
button = 8

buttonOn = False
buttonCount = 0

pedGreenStatus = False

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set LED pin to OUT
for i in carLED:
	GPIO.setup(carLED[i], GPIO.OUT)

for i in pedLED:
	GPIO.setup(pedLED[i], GPIO.OUT)

# Set Button pin to IN
GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)


def PedGreen():
        global pedGreenStatus
        
        print('PedGreen')
        GPIO.output(carLED['GREEN'], False)
        GPIO.output(carLED['YELLOW'], True)
        sleep(1)
        GPIO.output(carLED['YELLOW'], False)
        GPIO.output(carLED['RED'], True)
        
        GPIO.output(pedLED['RED'], False)
        GPIO.output(pedLED['GREEN'], True)
        pedGreenStatus = True
        sleep(4)
        GPIO.output(pedLED['GREEN'], False)
        pedGreenStatus = False
        GPIO.output(pedLED['RED'], True)
        

def PedGreenButton(channel = None):
        print('PedGreenButton')
        global buttonOn
        buttonOn = True
        PedGreen()


GPIO.add_event_detect(button, GPIO.RISING, callback = PedGreenButton)

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
</script>
"""

webGreen = """
<script>
window.location.href = '/PedRed';
</script>
"""

@route('/')
@route('/PedRed')
def index1():
        while pedGreenStatus:
                sleep(0.5)
        sleep(1)
        GPIO.output(carLED['RED'], False)
        GPIO.output(carLED['GREEN'], True)
        return webRed

@route('/PedGreen')
def index2():
        global buttonOn
        if buttonOn:
                buttonOn = False
        else:
                PedGreen()
        
        return webGreen

run(host = 'localhost', port = 8080)
