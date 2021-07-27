from random import gauss
import numpy as np
import math
from matplotlib import pyplot
from Chua import chua

def SNR_Set(Signal, Desired_SNR_dB):
    Npts = len(Signal)
    #Gaussian Noise
##    Noise = [gauss(0.0, 1.0) for i in range(Npts)] # Generate initial noise;
##                                                #mean zero, variance one
    #Poisson noise
    Noise = np.random.poisson(5, Npts)


    #Chaotic noise (chua model)
    #Noise = chua(Npts)


    
    Signal_Power = sum(abs(Signal)*abs(Signal))/Npts
    absN=[abs(i) for i in Noise]
    absnsqrd=[i*i for i in absN]
    Noise_Power = sum(absnsqrd)/Npts
            

    K = (Signal_Power/Noise_Power)*10**(-Desired_SNR_dB/10)  

    New_Noise = [math.sqrt(K)*i for i in Noise]

    Noisy_Signal = Signal + New_Noise
    return Noisy_Signal

##time= np.arange(0, 10, 0.001)
##amplitude= np.sin(time)
##pyplot.plot(time, amplitude)
##ss=SNR_Set(amplitude, 25)
##pyplot.plot(time, ss)
##pyplot.show()
