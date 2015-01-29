from numpy import *
from pylab import *
from scipy import *

from datetime import datetime
import pdb

ion()
i = 1j

def fst(f):
    N = len(f)
    F = zeros(N)
    for k in range(N):
        F[k] = (2.0/N)*sum([f[a]*sin(k*a*pi/N) for a in range(1,N)])
    return F

def ifst(F):
    N = len(F)
    f = zeros(N)
    for x in range(N):
        f[x] = sum([F[k]*sin(x*k*pi/N) for k in range(1,N)])
    return f
    
def ifst_trunc(F, nu):
    N = len(F)
    f = zeros(N)
    for x in range(N):
        f[x] = sum([F[k]*sin(x*k*pi/N) for k in range(1,nu)])
    return f
    
if __name__=="__main__":
    data = genfromtxt('sample-data/monthly-lake-erie-levels-1921-19.csv', delimiter=',',\
                      skip_header=1,dtype=None) 

    raw_x =  [datetime.strptime(dat[0],'"%Y-%m"') for dat in data[:-1]]                   
    data = array([dat[1] for dat in data[:-1]])
    
    figure(1)
    plot(raw_x,data)
    title("Monthly Lake Erie Levels between 1921 - 1970")
    
    figure(2)
    plot(data)
    title("Data with Numeric x-values")
    
    mu = mean(data)
    
#     cdata = data - mu
    cdata = data - (data[0] + (data[-1] - data[0])/len(data))
    
    figure(3)
    plot(cdata)
    title("Removing the Linear Term")
    
    ## here is where we will smooth using Fourier Series
    F = fst(cdata)
    magF = abs(F)
    
    figure(4)
    plot(magF)
    title("Magnitude of Fourier Coefficients")
    
    
    ff1 = ifst(F)
    
    figure(55)
    plot(cdata,label="Original")
    plot(ff1,label="Recovered")
    legend()
    title("Getting Back the Original")
    
    # Fit with sample of Fourier Coefficients
    fit_idx = r_[0:120]
    
    figure(5)
    plot(magF[fit_idx])
    title("Magnitude of Chosen Fourier Coefficients")
    
    ff = ifst_trunc(F,len(fit_idx))
    
    figure(6)
    plot(cdata,label="Original")
    plot(ff,label="Recovered")
    legend()
    title("Smoothed Fit")
    
    figure(7)
    plot(cdata-ff)
    title("Residuals")
    
    figure(8)
    plot(raw_x,data,label="Original")
    plot(raw_x,ff+mu,label="Recovered")
    legend()
    title("Smoothed Fit")
    
       