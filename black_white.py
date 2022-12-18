import com_dc as cd
import ultrasonic as us
from time import sleep
import RPi.GPIO as GPIO
import compass as cmp
import time
import methods as meth
import angles as a
l1=16      #23
l2=18      #24
r3=11      #17
r4=13      #27
wheel=36
count=0
N=a.N
S=a.S
E=a.E
W=a.W

n=a.n
s=a.s
e=a.e
w=a.w



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(l1,GPIO.OUT)
GPIO.setup(l2,GPIO.OUT)
GPIO.setup(r3,GPIO.OUT)
GPIO.setup(r4,GPIO.OUT)
GPIO.setup(wheel,GPIO.IN)


def move1():
    c=0
    while(1):
        if(GPIO.input(wheel)==True):
            c=c+1
            GPIO.output(r3,GPIO.LOW)
            GPIO.output(l1,GPIO.LOW)
            GPIO.output(r4,GPIO.HIGH)
            GPIO.output(l2,GPIO.HIGH)
            sleep(0.01)
            GPIO.output(l1,GPIO.LOW)
            GPIO.output(l2,GPIO.LOW)
            GPIO.output(r3,GPIO.LOW)
            GPIO.output(r4,GPIO.LOW)
        else:
            if(c!=0):
                GPIO.output(l1,GPIO.LOW)
                GPIO.output(l2,GPIO.LOW)
                GPIO.output(r3,GPIO.LOW)
                GPIO.output(r4,GPIO.LOW)
                break
            else:
                GPIO.output(r3,GPIO.LOW)
                GPIO.output(l1,GPIO.LOW)
                GPIO.output(r4,GPIO.HIGH)
                GPIO.output(l2,GPIO.HIGH)
                sleep(0.05)
                GPIO.output(r3,GPIO.LOW)
                GPIO.output(r4,GPIO.LOW)
                GPIO.output(l1,GPIO.LOW)
                GPIO.output(l2,GPIO.LOW)


def ready2move():
    while(GPIO.input(wheel)==True):
        GPIO.output(r3,GPIO.LOW)
        GPIO.output(l1,GPIO.LOW)
        GPIO.output(r4,GPIO.HIGH)
        GPIO.output(l2,GPIO.HIGH)
        sleep(0.01)
        GPIO.output(r3,GPIO.LOW)
        GPIO.output(r4,GPIO.LOW)
        GPIO.output(l1,GPIO.LOW)
        GPIO.output(l2,GPIO.LOW)


def movec():

    while(GPIO.input(wheel)==False):

        GPIO.output(r3,GPIO.LOW)
        GPIO.output(l1,GPIO.LOW)
        GPIO.output(r4,GPIO.HIGH)
        GPIO.output(l2,GPIO.HIGH)
        sleep(0.01)
        GPIO.output(r3,GPIO.LOW)
        GPIO.output(r4,GPIO.LOW)
        GPIO.output(l1,GPIO.LOW)
        GPIO.output(l2,GPIO.LOW)

    while(1):
#        print('in while')
#        sleep(0.01)
        if(GPIO.input(wheel)==True):
            GPIO.output(r3,GPIO.LOW)
            GPIO.output(l1,GPIO.LOW)
            GPIO.output(r4,GPIO.HIGH)
            GPIO.output(l2,GPIO.HIGH)
            sleep(0.01)
            GPIO.output(l1,GPIO.LOW)
            GPIO.output(l2,GPIO.LOW)
            GPIO.output(r3,GPIO.LOW)
            GPIO.output(r4,GPIO.LOW)
 #           print('Black')
        else:
            break





def moveD(ang):
    cd.position(ang)
    sleep(0.1)
    
    
    while(1):
    
        l=us.sense()
    
        if((l[0]<=8) or (l[1]<=8) or (l[2]<=8)):
            if( l[0]>12 and l[1]<=8 and l[2]>8 and l[4]>12 ):
                if(ang in N):
                    cd.position(w)
                elif(ang in S):
                    cd.position(e)
                if(ang in W):
                    cd.position(n)
                if(ang in E):
                    cd.position(s)
                move1()
                cd.position(ang)

            elif(l[0]>12 and l[2]<=8 and l[1]>8 and l[3]>12 ):
                if(ang in N):
                    cd.position(e)
                elif(ang in S):
                    cd.position(w)
                if(ang in W):
                    cd.position(s)
                if(ang in E):
                    cd.position(n)
                move1()
                cd.position(ang)


            else:
                break
        else:
           # print('in else')
            GPIO.output(r3,GPIO.LOW)
            GPIO.output(l1,GPIO.LOW)
            GPIO.output(r4,GPIO.HIGH)
            GPIO.output(l2,GPIO.HIGH)
            sleep(0.03)
            GPIO.output(l1,GPIO.LOW)
            GPIO.output(l2,GPIO.LOW)
            GPIO.output(r3,GPIO.LOW)
            GPIO.output(r4,GPIO.LOW)
    
    for i in range(5):    
        cd.position(ang)
    print('Reached north wall')
    return(cmp.angle())

#move1()

def mov():
    print(cmp.angle())
    cd.position(0)
    move1()
    print('after move')
    cd.position(0)
    print('angle :'+str(cmp.angle()))

#mov()
#move1()
#movec()
