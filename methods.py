import black_white as bw
import com_dc as cd
import ultrasonic as us
import RPi.GPIO as GPIO
from time import sleep
import compass as c
import angles as e

n=e.n
s=e.s
w=e.w
e=e.e

#bw.moveN()
def turnL():
    a=c.angle()
    b=a-90
    turn(b)

def turn(b):
    if(b>160 and b<200):
        cd.position(b)
    elif(b>-15 and b<=15):
        cd.position(b)
    elif(b>70 and b<105):
        cd.position(b)
    else:
        cd.position(270)
    bw.ready2move()

def turnR():
    a=c.angle()
    b=a+90
    turn(b)

