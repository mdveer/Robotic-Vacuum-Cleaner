import RPi.GPIO as GPIO
from time import sleep
motor1=23
motor2=24

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(motor1,GPIO.OUT)
    GPIO.setup(motor2,GPIO.OUT)

def loop():
    GPIO.output(motor1,GPIO.HIGH)
    GPIO.output(motor2,GPIO.LOW)
    print('front\n')
  #  sleep(1)
   # GPIO.output(motor1,GPIO.LOW)
   # GPIO.output(motor2,GPIO.HIGH)
   # sleep(1)
   # print('back\n')
def destroy():
    GPIO.cleanup()

'''if __name__ =='__main__':
    setup()
    try:
        loop()
    except keyboardInterrupt:
        destroy()
'''
destroy()
setup()
while(1):
    loop()
