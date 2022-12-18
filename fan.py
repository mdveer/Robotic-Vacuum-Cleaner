import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) 
 
RELAIS_1_GPIO = 15
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)

for i in range(5):
    GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # on 
    print('off')
    sleep(3)    
    GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)   #off
    print('on')
    sleep(3)

