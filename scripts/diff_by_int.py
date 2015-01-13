from numpy import *
from scipy import *
from pylab import *

import numpy.random as random

import pdb

ion()

if __name__ == "__main__":
    ## first example
    t = linspace(0,10)
    yt = 5.0*t**2 
    noise = random.normal(0,10,len(t))
    y = yt + noise
    
    # theoretical derivative
    yp = 10.0*t
    
    # sum formula
    k = 2
    h=t[1]-t[0]
    b = zeros(len(t))
    data_num = len(t)
    for x in range(2,data_num-2):
        num = sum([alpha*y[x + alpha] for alpha in range(-k,k+1)])
        denom = 2*h*sum([alpha**2 for alpha in range(1,k+1)])
        b[x] = num/denom
    
    # simple diff
    yd = diff(y)/h
    
    # integration formula
    yi = 5.0*t**2
    
    figure(1)
    title("Original Function + Noise")
    plot(t,y,'bo',markerfacecolor='none',mec='blue')
    plot(t,yt,'b-')
    
    figure(2)
    title("Derivative")
    plot(yp,label="Theoretical")
    plot(yd,label="Simple Difference")
    plot(b[:-2],label="Sum Formula")
    legend()