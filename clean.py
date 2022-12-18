
import ultrasonic as us
import com_dc as cd
import black_white as bw
import numpy as np

import RPi.GPIO as GPIO
from time import sleep
import methods as meth
import compass as cmp
import ucdc 
import time
p=[]
d=np.load('area50.npy')
np.save('area51clean',d)
np.save('area51',d)

b=np.load('area51clean.npy')
a=np.load('area51.npy')
corners={}
n=ucdc.n
s=ucdc.s
e=ucdc.e
w=ucdc.w
N=ucdc.N
S=ucdc.S
W=ucdc.W
E=ucdc.E
x
Rsize=len(a)
Csize=len(a[0])
print('starting')
print(Rsize)
print(Csize)

def southcor():
    print('started')
    r=0
    nor=len(b)
    noc=len(b[0])
    print(noc)
    c=0
    for i in b:
        c=0
        for j in i:
            if(c>0 and c < (noc-1)):
#                print(str(r)+' '+str(c))
                if(r<(nor-1) and  b[r,c-1]!=1 and b[r,c]==1 and b[r+1,c]!=1 and b[r,c+1]==1):
                    temp=[r,c+1]
                    print(temp)
                    R=r
                    C=c+1
                    des=0
                    while(b[R-1,C]==1 and (b[R-1,C-2]!=1 or b[R-1,C-3]!=1 or C==2)):
                        des=des+1
                        R=R-1
                    corners[des]=temp
            c=c+1
        r=r+1

    print(corners)

def initial():
    ang= bw.moveD(ucdc.w)
    meth.turnL()
    cd.position(ucdc.s)
    ang=bw.moveD(ucdc.s)
    cd.position(ucdc.n)
    
    len=0
    l=us.sense()
    while(sum(l) > 2000):
            l=us.sense()

    while(l[0]>10):
        cd.position(ucdc.n)
        bw.move1()
        len=len+1
        sleep(0.01)
        l=us.sense()
        while(sum(l) > 2000):
            l=us.sense()
    print(len)
    return(len)

def r_c(corners,len):
    l=[]
    for key in corners:
        l.append(key)
    l2=[]
    for i in l:
        if((i+5)-len>0):
            l2.append(i-len)
    val=min(l2)+len
    print(corners[val])
    return(corners[val])
    

def in_pos():
    cd.position(ucdc.s)
    bw.moveD(ucdc.s)
    cd.position(ucdc.w)
    bw.moveD(ucdc.w)
    cd.position(ucdc.n)
    print(p)
    p[0]=p[0]-2

def test(r,c):
    d=np.load('area51clean.npy')
    if(d[r,c]==1 and d[r,c+1]==1 and d[r,c+2]==1 and d[r+1,c]==1 and d[r+1,c+1]==1 and d[r+1,c+2]==1 and d[r+2,c]==1 and d[r+2,c+1]==1 and d[r+2,c+2]==1   and a[r,c]==1 and a[r,c+1]==1 and a[r,c+2]==1 and a[r+1,c]==1 and a[r+1,c+1]==1 and a[r+1,c+2]==1 and a[r+2,c]==1 and a[r+2,c+1]==1 and a[r+2,c+2]==1   ):
        return(1)
    return(0)

def moveto(rem):

    print('Moving to the positon of '+ str(rem))
    if(rem[1]<p[1]):
        cm=w
    else:
        cm=e

    if(rem[0]<p[0]):
        rm=n
    else:
        rm=s
    trymis=0
    while(rem!=p):
        #print('MOVING COLUMN')
        trymis=trymis+1
        tryc=0
        while(rem[1]!=p[1]):
            print('MOVING COLUMN')
            cd.position(cm)
            sleep(0.01)
            l=us.sense()
            while(sum(l) > 2000):
                l=us.sense()
            if(l[0]<=12):
                tryc=tryc+1
            print(l)
            print(tryc)
            if(cm==w and l[0]>12):
                bw.move1()
                p[1]=p[1]-1
            elif(cm==w and rm==s and l[3]>12):
                a[p[0],p[1]-1]=2
                meth.turnL()
                cd.position(rm)
                bw.move1()
                meth.turnR()
                cd.position(cm)
                p[0]=p[0]+1
            elif(cm==w and rm==n and l[4]>12):
                a[p[0],p[1]-1]=2
                meth.turnR()
                cd.position(rm)
                bw.move1()
                meth.turnL()
                cd.position(cm)
                p[0]=p[0]-1
            elif(cm==e and l[0]>12):
                bw.move1()
                p[1]=p[1]+1
            elif(cm==e and rm==s and l[4]>12):
                a[p[0],p[1]+1]=2
                meth.turnL()
                cd.position(rm)
                bw.move1()
                meth.turnR()
                cd.position(cm)
                p[0]=p[0]+1
            elif(cm==e and rm==n and l[3]>12):
                a[p[0],p[1]+1]=2
                meth.turnR()
                cd.position(rm)
                bw.move1()
                meth.turnL()
                cd.position(cm)
                p[0]=p[0]-1
            else:
                print('stable')
            if(tryc > 5):
                break

        print('MOVING ROW')
        tryr=0
        while(rem[0]!=p[0]):
            print('MOVING ROW')
            cd.position(rm)
            sleep(0.01)
            l=us.sense()
            while(sum(l) > 2000):
                l=us.sense()
            if(l[0]<=12):
                tryr=tryr+1
            print(l)
            print(tryr)
            if(rm==n and l[0]>12):
                bw.move1()
                p[0]=p[0]-1
            elif(rm==n and cm==w and l[3]>12):
                a[p[0]-1,p[1]]=2
                meth.turnL()
                cd.position(cm)
                bw.move1()
                meth.turnR()
                cd.position(rm)
                p[1]=p[1]-1
            elif(rm==n and cm==e and l[4]>12):
                a[p[0]-1,p[1]]=2
                meth.turnR()
                cd.position(cm)
                bw.move1()
                meth.turnL()
                cd.position(rm)
                p[1]=p[1]+1

            elif(rm==s and l[0]>12):
                bw.move1()
                p[0]=p[0]+1

            elif(rm==s and cm==w and l[4]>12):
                a[p[0]+1,p[1]]=2
                meth.turnR()
                cd.position(cm)
                bw.move1()
                meth.turnL()
                cd.position(rm)
                p[1]=p[1]-1
           
            elif(rm==s and cm==e and l[3]>12):
                a[p[0]+1,p[1]]=2
                meth.turnL()
                cd.position(cm)
                bw.move1()
                meth.turnR()
                cd.position(rm)
                p[1]=p[1]+1
            else:
                print('stable')

            if(tryr>5):
                break

        if(trymis==1):
            print('quicting the row')
            rem_r=rem[0]
            break
    if(rem==p):
        a[p[0],p[1]]=1


def notcleaned():
    d=np.load("area51clean.npy")
    r=0
    for i in d:
        count=0
        c=0
        if(r<(Rsize-2)):
            for j in i:
                if(j==1 and count<=2 ):
                    count=count+1
                if(count==3 and c<(Csize-2)):
                    print(str(r)+'-'+str(c-2))
                    q=test(r,c-2)
                    if(q==1):
                        #print('moving')
                        ucdc.moveto([r+1,c-2])
                        return(1)
                c=c+1
        r=r+1
    return(0)

def start():
    stp=1
    ang=n
    while(stp):
#        for i in a:
 #           print(i)
  #      print('cleaned area')
        for i in b:
            print(i)
        print("\n"+str(p)+str(ang))
        r=p[0]
        c=p[1]
        sleep(0.02)
        l=us.sense()
        while(sum(l) > 2000):
            l=us.sense()
        l1=us.sense()
        while(sum(l1) > 2000):
            l1=us.sense()
       # print(r)
       # print(Rsize)
        print(l)
       # print(l1)
        if((ang in N) and r>2 and ((l[0]+l1[0])/2)>=10 and ((l[1]+l1[1])/2)>=6 and ((l[2]+l1[2])/2)>=6 and (((l[3]+l1[3])/2)<18 or b[r+1,c-2]==3 or c<=2) ):
            print('clean north') 
            ang=readN()

        elif(ang in N and c>2 and ((l[3]+l1[3])/2)>=18 and b[r+1,c-2]!=3):
            meth.turnL()
            bw.movec()
            meth.turnR()
            p[1]=p[1]-1

        elif(ang in N and (((l[0]+l1[0])/2)<10 or ((l[1]+l1[1])/2)<12 or ((l[2]+l1[2])/2)<12 or r<=2) and ((l[4]+l1[4])/2)>10 ):
            print('Turning Right ie. East')
            bw.movec()
            meth.turnR()
            p[1]=p[1]+1
            ang=readE()

        elif(ang in S and (((((l[0]+l1[0])/2)<10 or ((l[1]+l1[1])/2)<12 or ((l[2]+l1[2])/2)<12) and ((l[3]+l1[3])/2)>10) or (r>=(Rsize-2) and ((l[3]+l1[3])/2)>10) )):
            print('turning east')
           # meth.turnL()
            cd.position(e)
            p[0]=p[0]-1
            p[1]=p[1]+1
            ang=readE()


        elif(ang in S and ((l[4]+l1[4])/2)>=18 and b[r-1,c-2]!=3):
            print('turning right')
            meth.turnR()
            bw.movec()
            meth.turnL()
            p[1]=p[1]-1


        elif( (ang in S) and r<(Rsize-2)  and ((l[0]+l1[0])/2)>=10 and ((l[1]+l1[1])/2)>=6 and ((l[2]+l1[2])/2)>=6 and (b[r+1,c]!=3 or b[r+1,c-1]!=3 or b[r+1,c+1]!=3)):
            print('clean south')
            ang=readS()

   
        elif(ang in E and c<(Csize-1)  and((l[0]+l1[0])/2)>12 and ((l[1]+l1[1])/2)>=6 and ((l[2]+l1[2])/2)>=6 and (((l[3]+l1[3])/2)<12 or ((l[4]+l1[4])/2)<12 or ((l[6]+l1[6])/2)<12  or ((l[2]+l1[2])/2)<12  or ((l[1]+l1[1])/2)<12)):
            print('clean east')
            ang=readE()

        elif(ang in E and r<(Rsize-3) and ( ((l[0]+l1[0])/2)>10 and ((l[1]+l1[1])/2)>6 and ((l[2]+l1[2])/2)>6) and  ((l[4]+l1[4])/2)>12  and b[r+2,c-1]!=3 and b[r-2,c-1]!=3 ):
            #meth.turnR()
            cd.position(s)
            p[0]=p[0]+1
            p[1]=p[1]-1
            ang=readS()

        elif(ang in E and r<(Rsize-3) and ( ( ((l[0]+l1[0])/2)<10 or ((l[1]+l1[1])/2)<6 or ((l[2]+l1[2])/2)<6) or (b[r-2,c-2]==3 and b[r+2,c-1]!=3 and  ((l[6]+l1[6])/2)>10 and ((l[4]+l1[4])/2)>10 and ((l[2]+l1[2])/2)>10) ) and (((l[3]+l1[3])/2)<10 or b[r-2,c-2]==3) and ((l[4]+l1[4])/2)>12 ):
            meth.turnR()
            bw.movec()
            meth.turnL()
            p[0]=p[0]+1

        elif(ang in E and ( ((l[0]+l1[0])/2)<10 or ((l[1]+l1[1])/2)<6 or ((l[2]+l1[2])/2)<6) and (((l[4]+l1[4])/2)<10 or b[r+2,c-1]==3) and ((l[3]+l1[3])/2)>12 ):
            cd.position(n)
            bw.movec()
            meth.turnR()
            p[0]=p[0]-1

        else:
            res=notcleaned()
            if(res==0):
                print('done cleaning')
                break

def readN():
   # cd.position(n)
    r=p[0]
    c=p[1]
    print('['+str(r)+','+str(c)+']')
    b[r,c]=3
    b[r+1,c]=3
    b[r+1,c+1]=3
    b[r+1,c-1]=3
    b[r,c+1]=3
    b[r,c-1]=3
    b[r+2,c]=3
    b[r+2,c-1]=3
    b[r+2,c+1]=3
    a[r,c]=1
    a[r+1,c]=1
    a[r+1,c+1]=1
    a[r+1,c-1]=1
    a[r+2,c]=1

    l=us.sense()
    while(sum(l) > 2000):
        l=us.sense()
    #print(l)
    if(b[r-1,c]!=3):
        if(l[0]>10):
            a[r-1,c]=1
        else:
            d=us.sense()
            if(d[0]<=10):
                a[r-1,c]=2
            else:
                a[r-1,c]=1

    if(b[r,c-1]!=3):
        if(l[1]>5):
            a[r,c-1]=1
        else:
            a[r,c-1]=2

    if(b[r,c+1]!=3):
        if(l[2]>=3):
            a[r,c+1]=1
        else:
            a[r,c+1]=2

    if(b[r,c-2]!=3):
        if(l[3]>10):
            a[r,c-2]=1
        else:
            a[r,c-2]=2

    if(c<(Csize-2)):
        if(b[r+1,c+2]!=3):
            if(l[4]>15):
                a[r+1,c+2]=1
            else:
                a[r+1,c+2]=2

    if(b[r+2,c-1]!=3):
        if(l[5]>8):
            a[r+2,c-1]=1
        else:
            a[r+2,c-1]=2

    if(b[r+2,c+1]!=3):
        if(l[6]>8):
            a[r+2,c+1]=1
        else:
            a[r+2,c+1]=2

    if(a[r-1,c]==1 and l[1]>10 and l[2]>10):
        cd.position(n)
        if(l[0]>18):
            p[0]=r-1
            bw.movec()
            cd.position(n)
        if(l[0]<=18 and r>=2):
            print('AUTO TURN RIGHT')
            bw.movec()
            #meth.turnR()
            p[1]=c+1
            cd.position(e)
            readE()
    np.save('area51',a)
    np.save('area51clean',b)
   # for i in a:
    #    print(i)

    print('cleaned North')
    return(cmp.angle())





def readS():
   # cd.position(s)
    print(cmp.angle())
    r=int(p[0])
    c=int(p[1])
    print('['+str(r)+','+str(c)+']')
    b[r,c]=3
    b[r-1,c]=3
    b[r-2,c]=3
    b[r-2,c-1]=3
    b[r-2,c+1]=3
    b[r-1,c+1]=3
    b[r-1,c-1]=3
    b[r,c-1]=3
    b[r,c+1]=3
    a[r,c]=1
    a[r-1,c]=1
    a[r-2,c]=1
    a[r-1,c+1]=1
    a[r-1,c-1]=1
    print('Before sense')
    l=us.sense()
    while(sum(l) > 2000):
        l=us.sense()
   # print(l)

    if(b[r+1,c]!=3):
        if(l[0]>10):
            a[r+1,c]=1
        else:
            d=us.sense()
            if(d[0]<=10):
                a[r+1,c]=2
            else:
                a[r+1,c]=1

    if(b[r,c+1]!=3):
        if(l[1]>5):
            a[r,c+1]=1
        else:
            a[r,c+1]=2

    if(b[r,c-1]!=3):
        if(l[2]>4):
            a[r,c-1]=1
        else:
            a[r,c-1]=2

    if(p[1]<(Csize-2)):
        if(b[r-1,c+2]!=3):
            if(l[3]>10):
                a[r-1,c+2]=1
            else:
                a[r-1,c+2]=2
    if(c>1):
        if(b[r-1,c-2]!=3):
            if(l[4]>15):
                a[r-1,c-2]=1
            else:
                a[r-1,c-2]=2

    if(b[r-2,c+1]!=3):
        if(l[5]>8):
            a[r-2,c+1]=1
        else:
            a[r-2,c+1]=2

    if(b[r-2,c-1]!=3):
        if(l[6]>8):
            a[r-2,c-1]=1
        else:
            a[r-2,c-1]=2

    print('cloumn ::'+str(c))

    if(a[r+1,c]==1 and l[1]>10  and l[2]>10):
        cd.position(s)
        if(l[0]>18):
            print('moving forward')
            p[0]=r+1
            bw.movec()
            cd.position(s)
        else:
            print('AUTO TURN LEFT')
            bw.movec()
            cd.position(e)
            p[1]=c+1
            cd.position(e)
            readE()
            

    np.save('area51',a)
    np.save('area51clean',b)
   # for i in a:
    #    print(i)

    print('cleaned south')
    return(cmp.angle())







def readE():
   # cd.position(e)
    r=p[0]
    c=p[1]
    print('['+str(r)+','+str(c)+']')
    b[r,c]=3
    b[r,c-1]=3
    b[r,c-2]=3
    b[r-1,c-2]=3
    b[r+1,c-2]=3
    b[r-1,c-1]=3
    b[r+1,c-1]=3
    b[r-1,c]=3
    b[r+1,c]=3
    a[r,c]=1
    a[r,c-1]=1
    a[r,c-2]=1
    a[r-1,c-1]=1
    a[r+1,c-1]=1
    print('Before sense')
    l=us.sense()
    while(sum(l) > 2000):
        l=us.sense()
    #print(l)

    if(b[r,c+1]!=3):
        if(l[0]>10):
            a[r,c+1]=1
        else:
            d=us.sense()
            if(d[0]<=10):
                a[r,c+1]=2
            else:
                a[r,c+1]=1

    if(b[r-1,c]!=3):
        if(l[1]>5):
            a[r-1,c]=1
        else:
            a[r-1,c]=2

    if(b[r+1,c]!=3):
        if(l[2]>4):
            a[r+1,c]=1
        else:
            a[r+1,c]=2

    if(b[r-2,c-1]!=3):
        if(l[3]>10):
            a[r-2,c-1]=1
        else:
            a[r-2,c-1]=2


    if(c!=(Csize-2)):
        if(b[r+2,c-1]!=3):
            if(l[4]>15):
                a[r+2,c-1]=1
            else:
                a[r+2,c-1]=2

    if(b[r-1,c-2]!=3):
        if(l[5]>8):
            a[r-1,c-2]=1
        else:
            a[r-1,c-2]=2

    if(b[r-1,c-2]!=3):
        if(l[6]>8):
            a[r+1,c-2]=1
        else:
            a[r+1,c-2]=2

    if(a[r-2,c-1]==2 ):
        cd.position(e)
    j=0
    for i in range(2):
        l=us.sense()
        while(sum(l) > 2000):
            l=us.sense()

        if(l[0]>12):
            j=j+1
            p[1]=p[1]+1
            b[p[0],p[1]]=3
            b[p[0],p[1]-1]=3
            b[p[0],p[1]-2]=3
            b[p[0]-1,p[1]-1]=3
            b[p[0]+1,p[1]-1]=3
            b[p[0]-1,p[1]]=3
            b[p[0]+1,p[1]]=3
            b[p[0]+1,p[1]-2]=3
            b[p[0]-1,p[1]-1]=3
            a[p[0],p[1]]=1
            a[p[0],p[1]-1]=1
            a[p[0],p[1]-2]=1
            a[p[0]-1,p[1]-1]=1
            a[p[0]+1,p[1]-1]=1
            bw.movec()
            cd.position(e)
            if(b[p[0]-2,p[1]-1]!=3):
                if(l[3]>10):
                    a[p[0]-2,p[1]-1]=1
                else:
                    a[p[0]-2,p[1]-1]=2
            r=p[0]
            c=p[1]
        else:
            print(' TURN RIGHT')
            meth.turnR()
            p[0]=r+1
            p[1]=c-1
            cd.position(s)
            break
    print(str(j)+'  '+str(l[3]))
    if(j==2 and l[3]<12):
        meth.turnR()
        p[0]=r+1
        p[1]=c-1
        cd.position(s)
    if(j==2 and (a[r+2,c-1]==2 or l[4]<=15 or r>=Rsize-3 or c>=(Csize-2))):
        cd.position(n)
        p[0]=r-1
        p[1]=c-1
        cd.position(n)
    np.save('area51',a)
    np.save('area51clean',b)
   # for i in a:
    #    print(i)
    print('read east')
    return(cmp.angle())










c=b

southcor()

len =initial()

p=r_c(corners,len)
print(p)
in_pos()
start()
