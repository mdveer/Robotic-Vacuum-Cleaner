
import numpy as np
a=np.load('area51.npy')
Csize=16
Rsize=13
def nnotcleaned():
    d=np.load("area51clean.npy")
    r=0
    for i in d:
        count=0
        c=0
        if(r<(Rsize-1)):
            for j in i:
                if(j==1 and count<=1 ):
                    count=count+1
                if(count==2 and c<(Csize-1)):
                    print(str(r)+'-'+str(c-1))
                    q=test(r,c-1)
                    if(q==1):
                        print('moving')
                        #moveto([r,c-1])
                        #return(1)
                c=c+1
        r=r+1
    return(0)

def ntest(r,c):
    print('in test')
    d=np.load('area51clean.npy')
    print(d[r,c])
    print(d[r,c+1])
    print(d[r+1,c])
    print(d[r+1,c+1])
    print(a[r,c])
    print(a[r,c+1])
    print(a[r+1,c])
    print(a[r+1,c+1])

    if(d[r,c]==1 and d[r,c+1]==1 and d[r+1,c]==1 and d[r+1,c+1]==1 and  a[r,c]==1 and a[r,c+1]==1 and a[r+1,c]==1 and a[r+1,c+1]==1  ):
        print(r)
        print(c)
        return(1)
    return(0)


def test(r,c):
    print('in test')
    d=np.load('area51clean.npy')
    print(d[r,c])
    print(d[r,c+1])
    print(d[r,c+2])
    print(d[r+1,c])
    print(d[r+1,c+1])
    print(d[r+1,c+2])
    print(d[r+2,c])
    print(d[r+2,c+1])
    print(d[r+2,c+2])
    print( a[r,c])
    print( a[r,c+1])
    print(a[r,c+2])
    print(a[r+1,c])
    print(a[r+1,c+1])
    print(a[r+2,c])
    print(a[r+2,c+1])
    print(a[r+2,c+2])

    if(d[r,c]==1 and d[r,c+1]==1 and d[r,c+2]==1 and d[r+1,c]==1 and d[r+1,c+1]==1 and d[r+1,c+2]==1 and d[r+2,c]==1 and d[r+2,c+1]==1 and d[r+2,c+2]==1   and a[r,c]==1 and a[r,c+1]==1 and a[r,c+2]==1 and a[r+1,c]==1 and a[r+1,c+1]==1 and a[r+1,c+2]==1 and a[r+2,c]==1 and a[r+2,c+1]==1 and a[r+2,c+2]==1   ):
        return(1)
    return(0)


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
                        print('moving')
                        #ucdc.moveto([r+1,c-2])
                        #return(1)
                c=c+1
        r=r+1
    return(0)

notcleaned()
