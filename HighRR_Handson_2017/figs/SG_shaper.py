# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import math
import numpy as np
import matplotlib.pyplot as plt

def vo(t,n):
    return 1.0/math.factorial(n)*np.power(t,n)*np.exp(-t)
    
t = np.arange(0.0, 12.0, 0.05)

plt.figure(1)
plt.plot(t, vo(t,1),label="n=1",color='red')
plt.plot(t, vo(t,2),label="n=2",color='green')
plt.plot(t, vo(t,3),label="n=3",color='blue')
plt.plot(t, vo(t,4),label="n=4",color='black')

plt.legend(loc='best')
plt.title("Normalized waveform of $CR-(RC)^n$ shaper",fontsize=14)
plt.xlabel(r"$t/\tau$",fontsize=14)
plt.ylabel("$v_o(t)/(Q/C_f)$",fontsize=14)
plt.grid()
plt.savefig("SGshaper_waveform.jpg",dpi=400)

def doubleFactorial(n):
    if n <= 0:
        return 1
    else:
        return n*doubleFactorial(n-2)

def inferiorityCofficient(n):
    x =[]
    for i in np.arange(1,n,1):
        xx = math.factorial(i)*math.pow(np.e,i)/math.pow(i,i)
        xx = xx*math.pow(2*i-1,1/4)
        xx = xx*math.sqrt(doubleFactorial(2*i-3)/2/doubleFactorial(2*i))
        x.append(xx)
    return x
    
plt.figure(2)
n = 8
plt.plot(np.arange(1,n,1),inferiorityCofficient(n),'bo-')
plt.plot([0, 8], [1.12, 1.12], 'r--', lw=2)
plt.title("SNR inferiority Coefficient as a function of shaper order n",fontsize=14)
plt.xlabel("order n of $CR-(RC)^n$ shaper",fontsize=14)
plt.xlim(0,8)
plt.ylim(1.1,1.4)
plt.ylabel(r"$\eta_{\infty}/\eta_{opt}$",fontsize=14)
plt.grid()
plt.annotate(r"$n=\infty$", xy=(3, 1.12), xytext=(1, 1.18),
            arrowprops=dict(facecolor='red', shrink=0.01),fontsize=16,
            )
plt.savefig("SGshaper_F.jpg",dpi=400)

def ampNormalize(x):
    x_max = x[0]
    y = []
    for xx in x:
        if x_max < xx:
            x_max = xx
            
    for xx in x:
        y.append(xx/x_max)
        
    return y
    

def activeWaveform(t):
    return np.exp(-t)*(t - np.sin(t))

plt.figure(3)
plt.plot(t/np.sqrt(7), ampNormalize(vo(t,4)),label=r"$CR-(RC)^4$",color='red')
plt.plot(2*t/np.sqrt(11), ampNormalize(activeWaveform(t)),label="active filter",color='green')

plt.legend(loc='best')
plt.title("Normalized waveform of $CR-(RC)^4$ and active filter",fontsize=14)
plt.xlabel(r"$t/\tau_{opt}$",fontsize=14)
plt.xlim(0,6)
plt.ylim(-0.2,1.2)
plt.ylabel("Normalized waveform",fontsize=14)
plt.grid()
plt.savefig("SGshaper_activewaveform.jpg",dpi=400)   
    
    
