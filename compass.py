from time import sleep
from i2clibraries import i2c_hmc5883l
hmc=i2c_hmc5883l.i2c_hmc5883l(1)
hmc.setContinuousMode()
hmc.setDeclination(0,6)

def angle():
    l=str(hmc)
    return(int(l))
'''
while(1):
    print(angle())
    sleep(1)
'''

