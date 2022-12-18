

'''  find not clean with 3/3 array  '''
def test(r,c):
    d=np.load('area51clean.npy')
    if(d[r,c]==1 and d[r,c+1]==1 and d[r,c+2]==1 and d[r+1,c]==1 and d[r+1,c+1]==1 and d[r+1,c+2]==1 and d[r+2,c]==1 and d[r+2,c+1]==1 and d[r+2,c+2]==1   and a[r,c]==1 and a[r,c+1]==1 and a[r,c+2]==1 and a[r+1,c]==1 and a[r+1,c+1]==1 and a[r+1,c+2]==1 and a[r+2,c]==1 and a[r+2,c+1]==1 and a[r+2,c+2]==1   ):
        return(1)
    return(0)

def notcleaned():
    d=np.load("area51clean.npy")
    r=0
    for i in d:
        count=0
        c=0
        for j in i:
            if(j==1 and count<=2 ):
                count=count+1
            if(count==2):
                r=test(r,c-2)
                if(r==1):
                    ucdc.moveto([r+1,c-2])
                    return(1)
            c=c+1
        r=r+1
    return(0)



''' Find not cleaned with 2/2 array'''
def test(r,c):
    d=np.load('area51clean.npy')
    if(d[r,c]==1 and d[r,c+1]==1 and d[r+1,c]==1 and d[r+1,c+1]==1 and  a[r,c]==1 and a[r,c+1]==1 and a[r+1,c]==1 and a[r+1,c+1]==1  ):
        return(1)
    return(0)


def notcleaned():
    d=np.load("area51clean.npy")
    r=0
    for i in d:
        count=0
        c=0
        if(r<(Rsize-1)):
            for j in i:
                if(j==1 and count<=1 ):
                    count=count+1
                if(count==2 and c<(Csize-2)):
                    q=test(r,c-1)
                    if(q==1):
                        moveto([r,c-1])
                        return(1)
                c=c+1
        r=r+1
    return(0)
