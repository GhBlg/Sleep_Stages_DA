import random
from matplotlib import pyplot as plt

 
def chua(n):
    ##m0=random.uniform(-4, -0.1)
    ##m1=random.uniform(-4, -0.1)
    ##alpha=random.uniform(15, 50)
    ##beta=random.uniform(12, 50)

    alpha  = 15.6
    beta   = 31
    m0     = -1.143
    m1     = -0.714

    x=0.7
    y=0
    z=0

    dt=0.01

    sig=[]
    sig1=[]

    for i in range(n):
        
        phi=m1*x+0.5*(m0-m1)*(abs(x+1)-abs(x-1))
        x1=alpha*(y-x-phi)
        y1=x-y+z
        z1=-beta*y

        
        x=x1*dt+x
        y=y1*dt+y
        z=z1*dt+z

        sig.append(x)
        sig1.append(y)

    return sig
