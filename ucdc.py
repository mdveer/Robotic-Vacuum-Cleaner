import ultrasonic as us
import com_dc as cd
import black_white as bw
import numpy as np
import RPi.GPIO as GPIO
from time import sleep
import methods as meth
import compass as cmp
import angles as a
N=a.N
S=a.S
E=a.E
W=a.W

n=a.n
s=a.s
e=a.e
w=a.w


#print(W)
#ang=0
size=25
p=[5,int(size/2)]
rem_r=0
try:
    a=np.load('area50.npy')
except:
    a=np.zeros((size,size),dtype=int)
    np.save('area50',a)

def start():
    ang=bw.moveD(n)
    cd.position(n)
    #ang=s
    while(1):
        sleep(0.1)
        cd.position(ang)
        print('angle:')
        print(ang)
        print(p[0])
        print(p[1])
        for i in a:
            print(i)

        l1=us.sense()
        l2=us.sense()
        while(sum(l2) > 2000):
            l2=us.sense()
        print(str(l1[4]) +' -  '+str(l2[4]))
        print(l2)
        if(p[0]==0 and (ang in N)):
            print('turning towards west')
            meth.turnL()
            p[0]=p[0]+1
            p[1]=p[1]-1
            ang=readW()
       # bw.move1()

            

        elif((ang in S)  and p[1]>4 and (((l1[4]+l2[4])/2) > 30) and l2[2]>25 and (a[p[0]-1,p[1]-3]==0)and (a[p[0]-1,p[1]-2]!=2) and(a[p[0]-2,p[1]-4]!=0 or (a[p[0]-1,p[1]-4]!=0) or (a[p[0]-2,p[1]-2]!=0))and((a[p[0]-2,p[1]-3] !=0) or (a[p[0]-2,p[1]-2]!=0))):
            print('Turning towards Right ie. West')
            bw.move1()
            meth.turnR()
            p[1]=p[1]-1
            ang=readW()

        elif( (ang in E) and p[0]<(size-4) and ((l1[4]+l2[4])/2)>30  and l2[2]>25 and a[p[0]+2,p[1]-1]!=2 and a[p[0]+3,p[1]-1]==0 and (a[p[0]+4,p[1]-1]!=0 or a[p[0]+4,p[1]-2]!=0 or a[p[0]+2,p[1]-2]!=0 ) and (a[p[0]+2,p[1]-2]!=0 or a[p[0]+3,p[1]-2]!=0) ):
            print(' Turning towards Right ie. south')
            bw.move1()
            meth.turnR()
            p[0]=p[0]+1
            ang=readS()

        elif((ang in W)   and  ((l1[4]+l2[4])/2) >30  and a[p[0]-3,p[1]+1]==0 and l2[2]>25 and a[p[0]-2,p[1]+1]!=2 and (a[p[0]-4,p[1]+1]!=0 or a[p[0]-4,p[1]+2]!=0 or a[p[0]-2,p[1]+2]!=0 ) and (a[p[0]-2,p[1]+2]!=0 or a[p[0]-3,p[1]+2]!=0)):
            print('Turning towards Right ie. North')
            bw.move1()
            cd.position(n)
            p[0]=p[0]-1
            ang=readN()

        elif((ang in N) and p[1]<(size-4) and ((l1[4]+l2[4])/2)>30 and l2[2]>25 and a[p[0]+1,p[1]+2]!=2 and a[p[0]+1,p[1]+3]==0 and ( a[p[0]+1,p[1]+4]!=0 or a[p[0]+2,p[1]+4]!=0 or a[p[0]+2,p[1]+2]!=0) and (a[p[0]+2,p[1]+2]!=0  or  a[p[0]+2,p[1]+3]!=0)):
            print('Turning Right ie. East')
            bw.move1()
            cd.position(e)
            p[1]=p[1]+1
            ang=readE()
        
        elif((ang in W) and (a[p[0]-1,p[1]]==0 or a[p[0]+1,p[1]]==0)  and l2[1]>=5 and l2[2]>=5  and a[int(p[0]),int(p[1])-1]!=2  and a[p[0]-1,p[1]-1]!=2 and ( a[p[0],p[1]-2]==0  or a[p[0]-1,p[1]-1]==0)and a[p[0]-1,p[1]-1]!=2  and(int(p[1])!=0) and  (a[int(p[0]),int(p[1])]==1)):
            print('reading west')
            ang=readW()

        elif((ang in W) and ((a[p[0]+3,p[1]+1]==0 and (a[int(p[0]),int(p[1])-1]==2 or a[p[0]-1,p[1]-1]==2 or l2[0]<10 or l2[2]<=9) and a[p[0]+3,int(p[1])+1]==0) or ( (a[p[0],p[1]-3]!=0) and (a[p[0],p[1]-2]!=0)))):
            print('turning south')
            meth.turnL()
            cd.position(s)
            p[0]=p[0]+1
            p[1]=p[1]+1
            ang=readS()

        elif((ang in S) and ( a[p[0],p[1]-1]!=2  and  a[p[0],p[1]+1]!=2 ) and (l2[1] >= 5) and (l2[2]>=5) and  (a[int(p[0]+1),int(p[1])]!=2) and (a[p[0]+1,p[1]-1]!=2) and (int(p[0]!=size-1)) and (a[int(p[0]),int(p[1])]==1) and ((a[p[0]+2,p[1]]==0  or a[p[0]+2,p[1]+1]==0 or a[p[0]-1,p[1]-3]!=0))):
            print('reading south')
            ang=readS()

        elif((ang in S) and (a[int(p[0]+1),int(p[1])]==2 or a[p[0]+1,p[1]-1]==2 or l2[0]<10 or l2[2]<=9)):
            print('turning towards east')
            meth.turnL()
            cd.position(e)
            p[0]=p[0]-1
            p[1]=p[1]+1
            ang=readE()

        elif((ang in E) and (a[p[0]+1,p[1]]==0 or a[p[0]-1,p[1]]==0  ) and (l2[1]>=5) and (l2[2]>=5) and (a[int(p[0]),int(p[1])+1]!=2  and  a[p[0]+1,p[1]+1]!=2 ) and(int(p[1]!=size-1)) and (a[int(p[0]),int(p[1])]==1)):
            print('reading East')
            ang=readE()

        elif((ang in E) and (a[int(p[0]),int(p[1]+1)]==2 or a[p[0]+1,p[1]+1]  or l2[0]<10 or l2[2]<=9)):
            print('turning towards North')
            cd.position(n)
            p[0]=p[0]-1
            p[1]=p[1]-1
            ang=readN()

        elif((ang in N) and p[0]>1 and (a[p[0],p[1]+1]!=2  and a[p[0],p[1]-1]!=2 ) and (l2[1]>=5) and (l2[2]>=5)  and (a[int(p[0])-1,int(p[1])]!=2  and a[p[0]-1,p[1]+1]!=2) and (int(p[0])!=0) and (a[int(p[0]),int(p[1])]==1)):
            print('Reading North')
            ang=readN()

        elif((ang in N) and (l2[0]<8  or(p[0]==1) or (a[p[0]-1,p[1]] == 2 or a[p[0]-1,p[1]+1]==2  or l2[0]<10 or l2[2]<=9))):
            print('Turning towards West')
            meth.turnL()
            cd.position(w)
            p[0]=p[0]+1
            p[1]=p[1]-1
            ang=readW()
       
        else:
            
            rem= findrem()
            if(rem!='none'):
                print('Moving to area not sensed')
                moveto(rem)
            else:
                print('Done Mapping')
                minimize()
                for i in a:
                    print(i)
                break

        print('\n\n')



def minimize():

    b=a.tolist()
    nl=[]
    for i in b:
        if(sum(i)!=0):
            nl.append(i)
    arr=np.array(nl)
    d=arr.transpose()
    nl=[]
    b=d.tolist()
    for i in b:
        if(sum(i)!=0):
            nl.append(i)
    arr=np.array(nl)
    arr=arr.transpose()
    np.save('area50',arr)


def findrem():
    rc=-1
    print('in findrem()')
    for r in a:
       # print(r)
        rc=rc+1
        if(rc<=rem_r):
            continue
        v1=0
        b=-1
        cc=-1
        d=0
        for c in r:
            cc=cc+1
            if((b==1 and c==0 and v1==0) or (b==0 and c==1 and v1==1)):
                v1=v1+1
            if(v1==1 and d==0):
                s=cc
                d=d+1
            if(v1==2):
                e=cc
                break
            b=c
        if(v1==2):
            return([rc,s])
    return('none')


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



def readW():
   # cd.position(w)
    r=int(p[0])
    c=int(p[1])
    print('['+str(r)+','+str(c)+']')
    a[r,c]=1
    a[r,c+1]=1
    a[r-1,c+1]=1
    a[r,c+2]=1
    a[r+1,c+1]=1
   
    print('before sense in readW')
    l=us.sense()
    while(sum(l) > 2000):
        l=us.sense()
    print(l)
    if(l[0]>10):
        a[r,c-1]=1
    else:
        d=us.sense()
        if(d[0]<=10):
            a[r,c-1]=2
        else:
            a[r,c-1]=1
    if(l[1]>5):
        a[r+1,c]=1
    else:
        a[r+1,c]=2

    if(l[2]>4):
        a[r-1,c]=1
    else:
        a[r-1,c]=2

    if(l[3]>10):
        a[r-2,c+1]=1
    else:
        a[r-2,c+1]=2

    if(r!=1):
        if(l[4]>15):
            a[r+1,c-2]==1
        else:
            a[r+1,c-2]==2


    if(l[5]>8):
        a[r+1,c+2]=1
    else:
        a[r+1,c+2]=2
 
    if(l[6]>8):
        a[r-1,c+2]=1
    else:
        a[r-1,c+2]=2
    if(a[r,c-1]==1 and a[r+1,c]==1):
        cd.position(w)
        if(l[0]>18):
            print('Moving forward')
            p[1]=c-1
            bw.move1()
            cd.position(w)
        else:
            print('AUTO TURN LEFT')
            bw.move1()
            meth.turnL()
            p[0]=r+1
            cd.position(s)
    else:
        print(a[r,c-1])
        print(a[r-1,c])
        print(a[r+1,c])
       # sleep(10)
    np.save('area50',a)
  #  for i in a:
   #     print(i)
   # cd.position(270)
    print('read west')
    return(cmp.angle())


def readS():
   # cd.position(s)
    print(cmp.angle())
    r=int(p[0])
    c=int(p[1])
    print('['+str(r)+','+str(c)+']')
    a[r,c]=1
    a[r-1,c]=1
    a[r-2,c]=1
    a[r-1,c+1]=1
    a[r-1,c-1]=1
    print('Before sense')
    l=us.sense()
    while(sum(l) > 2000):
        l=us.sense()
    print(l)
    if(l[0]>10):
        a[r+1,c]=1
    else:
        d=us.sense()
        if(d[0]<=10):
            a[r+1,c]=2
        else:
            a[r+1,c]=1
    if(l[1]>5):
        a[r,c+1]=1
    else:
        a[r,c+1]=2

    if(l[2]>4):
        a[r,c-1]=1
    else:
        a[r,c-1]=2

    if(l[3]>10):
        a[r-1,c+2]=1
    else:
        a[r-1,c+2]=2

    if(l[4]>15):
        a[r-1,c-2]=1
    else:
        a[r-1,c-2]=2

    if(l[5]>8):
        a[r-2,c+1]=1
    else:
        a[r-2,c+1]=2

    if(l[6]>8):
        a[r-2,c-1]=1
    else:
        a[r-2,c-1]=2

    print('cloumn ::'+str(c))

    if(a[r+1,c]==1 and a[r,c-1]==1  and a[r,c+1]==1):
        cd.position(s)
        if(l[0]>18):
            print('moving forward')
            p[0]=r+1
            bw.move1()
            cd.position(s)
        else:
            print('AUTO TURN LEFT')
            bw.move1()
            meth.turnL()
            p[1]=c+1
            cd.position(e)
    np.save('area50',a)
   # for i in a:
    #    print(i)

    print('read south')
    return(cmp.angle())



def readE():
   # cd.position(e)
    r=p[0]
    c=p[1]
    print('['+str(r)+','+str(c)+']')
    a[r,c]=1
    a[r,c-1]=1
    a[r,c-2]=1
    a[r-1,c-1]=1
    a[r+1,c-1]=1
    print('Before sense')
    l=us.sense()
    while(sum(l) > 2000):
        l=us.sense()
    print(l)

    if(l[0]>10):
        a[r,c+1]=1
    else:
        d=us.sense()
        if(d[0]<=10):
            a[r,c+1]=2
        else:
            a[r,c+1]=1

    if(l[1]>5):
        a[r-1,c]=1
    else:
        a[r-1,c]=2

    if(l[2]>4):
        a[r+1,c]=1
    else:
        a[r+1,c]=2

    if(l[3]>10):
        a[r-2,c-1]=1
    else:
        a[r-2,c-1]=2

    if(c!=(size-2)):
        if(l[4]>15):
            a[r+2,c-1]=1
        else:
            a[r+2,c-1]=2

    if(l[5]>8):
        a[r-1,c-2]=1
    else:
        a[r-1,c-2]=2

    if(l[6]>8):
        a[r+1,c-2]=1
    else:
        a[r+1,c-2]=2

    if(a[r-1,c]==1 and a[r,c+1]==1 ):
        cd.position(e)
        if(l[0]>25):
            p[1]=c+1
            bw.move1()
            cd.position(e)
        else:
            print('AUTO TURN LEFT')
            bw.move1()
            cd.position(n)
            p[0]=r-1
            cd.position(n)
    np.save('area50',a)
   # for i in a:
    #    print(i)
    print('read east')
    return(cmp.angle())



def readN():
   # cd.position(n)
    r=p[0]
    c=p[1]
    print('['+str(r)+','+str(c)+']')
    a[r,c]=1
    a[r+1,c]=1
    a[r+1,c+1]=1
    a[r+1,c-1]=1
    a[r+2,c]=1
    l=us.sense()
    while(sum(l) > 2000):
        l=us.sense()
    print(l)

    if(l[0]>10):
        a[r-1,c]=1
    else:
        d=us.sense()
        if(d[0]<=10):
            a[r-1,c]=2
        else:
            a[r-1,c]=1

    if(l[1]>5):
        a[r,c-1]=1
    else:
        a[r,c-1]=2

    if(l[2]>=3):
        a[r,c+1]=1
    else:
        a[r,c+1]=2

    if(l[3]>10):
        a[r,c-2]=1
    else:
        a[r,c-2]=2

    if(c!=(size-2)):
        if(l[4]>15):
            a[r+1,c+2]=1
        else:
            a[r+1,c+2]=2

    if(l[5]>8):
        a[r+2,c-1]=1
    else:
        a[r+2,c-1]=2

    if(l[6]>8):
        a[r+2,c+1]=1
    else:
        a[r+2,c+1]=2

    if(a[r-1,c]==1 and a[r,c-1]==1 and a[r,c+1]==1):
        cd.position(n)
        if(l[0]>18):
            p[0]=r-1
            bw.move1()
            cd.position(n)
        else:
            print('AUTO TURN LEFT')
            bw.move1()
            meth.turnL()
            p[1]=c-1
            cd.position(w)
    np.save('area50',a)
   # for i in a:
    #    print(i)

    print('read North')
    return(cmp.angle())




def map(l,pr,pc): 
    f=np.load('area1.npy') 
    if(l[0]>10):
        f[int(pr-1),int(pc)]=1
    else:
        f[int(pr-1),int(pc)]=2
    if(l[1]>8):
        f[int(pr),int(pc-1)]=1
    else:
        f[int(pr),int(pc-1)]=2
    if(l[2]>8):
        f[int(pr),int(pc+1)]=1
    else:
        f[int(pr),int(pc+1)]=2
    if(l[4]>10):
        f[int(pr+1),int(pc-2)]=1
    else:
        f[int(pr+1),int(pc-2)]=2
    if(l[5]>10):
        f[int(pr+1),int(pc+2)]=1
    else:
        f[int(pr+1),int(pc+2)]=2
    np.save('area1',f)
    return( [pr,pc])


'''cd.position(ang)
l=us.sense()
print(l)'''
#rc=map(l,r,c)
#p=np.load('area1.npy')
#for i in p:
 #   print(i)

#start()
