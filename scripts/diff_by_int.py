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
    
    ## second example
    t2 = linspace(1,4)
    yt2 = cos(t2)
#     yt2 = log(t2)
    noise = random.normal(0,0.1,len(t2))
    y2 = yt2 + noise
    
    # theoretical derivative
    yp2 = -1.0*sin(t2)
#     yp2 = 1.0/t2
    
    # sum formula
    k = 2
    h2=t2[1]-t2[0]
    b2 = zeros(len(t2))
    data_num = len(t2)
    for x in range(2,data_num-2):
        num = sum([alpha*y2[x + alpha] for alpha in range(-k,k+1)])
        denom = 2*h2*sum([alpha**2 for alpha in range(1,k+1)])
        b2[x] = num/denom
        
    # simple diff
    yd2 = diff(y2)/h2
    
#     h2 = 0.5
    # integration formula
    yi2 = (3/(h2**3))*sin(t2)*(h2*cos(h2) - sin(h2))
    
    figure(3)
    title("Original Function + Noise")
    plot(t2,y2,'bo',markerfacecolor='none',mec='blue')
    plot(t2,yt2,'b-')
    
    figure(4)
    title("Derivative")
    plot(t2,yp2,label="Theoretical")
    plot(t2[1:],yd2,label="Simple Difference")
    plot(t2[2:-2],b2[2:-2],label="Sum Formula")
    legend()
    
    # integration formula for different h's
    h2 = array([t2[1]-t2[0],0.5,1.0])
    yi2 = zeros((len(h2),len(t2)))
    for ii in range(len(h2)):
        yi2[ii] = (3.0/(h2[ii]**3))*sin(t2)*(h2[ii]*cos(h2[ii]) - sin(h2[ii]))
    
    figure(5)
    title("Integration Formula")
    plot(t2,yp2,label="Theoretical",linewidth=2.5)
    for i in range(len(h2)):
        plot(t2,yi2[i],label="h = %.2f"%h2[i])
    legend()