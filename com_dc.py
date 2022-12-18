
import RPi.GPIO as GPIO
from time import sleep
import compass
l1=16      #23
l2=18      #24

r3=11      #17
r4=13      #27

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(l1,GPIO.OUT)
GPIO.setup(l2,GPIO.OUT)
GPIO.setup(r3,GPIO.OUT)
GPIO.setup(r4,GPIO.OUT)


def position(a):
    while(1):
        s=compass.angle()
       # print(s)

        if(a==270 and (s<=90 or s>=265)):
            while(1):
                b=compass.angle()
                if(b<=265 and b>=90):
                    GPIO.output(r4,GPIO.LOW)
                    GPIO.output(r3,GPIO.HIGH)
                    GPIO.output(l1,GPIO.LOW)
                    GPIO.output(l2,GPIO.HIGH)
                    sleep(0.001)
                    GPIO.output(l1,GPIO.LOW)
                    GPIO.output(l2,GPIO.LOW)
                    GPIO.output(r3,GPIO.LOW)
                    GPIO.output(r4,GPIO.LOW)
                elif(((b<=360 and b>275) or b<90)): #3 and (b>265 or b>=0)):
                    GPIO.output(r4,GPIO.HIGH)
                    GPIO.output(r3,GPIO.LOW)
                    GPIO.output(l1,GPIO.HIGH)
                    GPIO.output(l2,GPIO.LOW)
                    sleep(0.001)
                    GPIO.output(l1,GPIO.LOW)
                    GPIO.output(l2,GPIO.LOW)
                    GPIO.output(r3,GPIO.LOW)
                    GPIO.output(r4,GPIO.LOW)
                else:
                    print('in 270')
                    break
            break

        elif((a==0 or a==350) and s>=0 and s<=180):
            if(s>=345 or s<=5):
                print('In position')
                break

            else:
                GPIO.output(r4,GPIO.HIGH)
                GPIO.output(r3,GPIO.LOW)
                GPIO.output(l1,GPIO.HIGH)
                GPIO.output(l2,GPIO.LOW)
                sleep(0.001)
                GPIO.output(l1,GPIO.LOW)
                GPIO.output(l2,GPIO.LOW)
                GPIO.output(r3,GPIO.LOW)
                GPIO.output(r4,GPIO.LOW)
        else:
            if(s<=(a+5) and s>=(a-5)):
                print('In Position')
                break

            elif(s<(a+180) and s>=(a+5)):
                GPIO.output(r4,GPIO.HIGH)
                GPIO.output(r3,GPIO.LOW)
                GPIO.output(l1,GPIO.HIGH)
                GPIO.output(l2,GPIO.LOW)
                sleep(0.001)
                GPIO.output(r4,GPIO.LOW)
                GPIO.output(r3,GPIO.LOW)
                GPIO.output(l1,GPIO.LOW)
                GPIO.output(l2,GPIO.LOW)
            else:
                GPIO.output(l2,GPIO.HIGH)
                GPIO.output(l1,GPIO.LOW)
                GPIO.output(r3,GPIO.HIGH)
                GPIO.output(r4,GPIO.LOW)
                sleep(0.001)
                GPIO.output(r3,GPIO.LOW)
                GPIO.output(r4,GPIO.LOW)
                GPIO.output(l2,GPIO.LOW)
                GPIO.output(l1,GPIO.LOW) 
#        print('Angle'+str(compass.angle()))
'''
for i in range(2):
    position(350)
    sleep(0.01)
    position(350)
    sleep(2)
    position(270)
    sleep(0.01)
    position(270)
    sleep(2)
    position(180)
    sleep(0.01)
    position(180)
    sleep(2)
    position(90)
    sleep(0.01)
    position(90)
    sleep(1)

'''


