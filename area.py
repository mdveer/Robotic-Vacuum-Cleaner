
import numpy as np

a=np.load('area50.npy')


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
for i in arr:
    print(i)
