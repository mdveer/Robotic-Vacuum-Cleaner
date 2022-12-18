
import signal
from time import sleep
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

TRIG = 7      #4
ECHO1 =12     #18
ECHO2= 29      #5 
ECHO3=31        #6
ECHO4=22        #25
ECHO5=24         #8
ECHO6=26         #7
ECHO7=32        #12
#ECHO8=21

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO1,GPIO.IN)
GPIO.setup(ECHO2,GPIO.IN)
GPIO.setup(ECHO3,GPIO.IN)
GPIO.setup(ECHO4,GPIO.IN)
GPIO.setup(ECHO5,GPIO.IN)
GPIO.setup(ECHO6,GPIO.IN)
GPIO.setup(ECHO7,GPIO.IN)
#GPIO.setup(ECHO8,GPIO.IN)


def handler(signum,frame):
    raise IOError()

def sen():

    r=[]
    
    GPIO.output(TRIG,True)
    time.sleep(0.0001)
    GPIO.output(TRIG,False)
    start=0
    end=0
    while GPIO.input(ECHO1)== False:
        start = time.time()
    
    while GPIO.input(ECHO1)==True:
        end=time.time()
    sig_time = end-start
    distance = sig_time/0.000058
    r.append(int(distance))
    

    GPIO.output(TRIG,True)
    time.sleep(0.0001)
    GPIO.output(TRIG,False)
    while GPIO.input(ECHO2)==False:
        start=time.time()
    while GPIO.input(ECHO2)==True:
        end=time.time()
    sig_time = end-start
    r.append(int(sig_time/0.000058))
        
    GPIO.output(TRIG,True)
    time.sleep(0.0001)
    GPIO.output(TRIG,False)
    while GPIO.input(ECHO3)==False:
        start=time.time()
    while GPIO.input(ECHO3)==True:
        end=time.time()
    sig_time= end-start
    r.append(int(sig_time/0.000058))



    GPIO.output(TRIG,True)
    time.sleep(0.0001)
    GPIO.output(TRIG,False)
    while GPIO.input(ECHO4)==False:
        start=time.time()
    while GPIO.input(ECHO4)==True:
        end=time.time()
    sig_time=end-start
    r.append(int(sig_time/0.000058))


    GPIO.output(TRIG,True)
    time.sleep(0.0001)
    GPIO.output(TRIG,False)
    while GPIO.input(ECHO5)==False:
        start=time.time()
    while GPIO.input(ECHO5)==True:
        end=time.time()
    sig_time=end-start
    r.append(int(sig_time/0.000058))


    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)
    while GPIO.input(ECHO6)==False:
        start=time.time()
    while GPIO.input(ECHO6)==True:
        end=time.time()
    sig_time=end-start
    r.append(int(sig_time/0.000058))


    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)
    while GPIO.input(ECHO7)==False:
        start=time.time()
    while GPIO.input(ECHO7)==True:
        end=time.time() 
    sig_time=end-start
    r.append(int(sig_time/0.000058))
    #print(r)
    return(r)

def sense():
    signal.signal(signal.SIGALRM,handler)
    signal.alarm(1)
    try:
        r=sen()
    except IOError:
        print('In except block')
        r=sense()
    finally:
        signal.alarm(0)
    return(r)

'''
while(1):
    sleep(1)
    print(sense())
'''

