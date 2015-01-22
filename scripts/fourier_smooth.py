from numpy import *
from pylab import *
from scipy import *

from datetime import datetime
import pdb

ion()
i = 1j

def ifft_trunc(A,nu, N):
    a = zeros(N)
    for m in range(N):
        a[m] = (1.0/N)*sum([A[k]*exp(2.0*pi*i*(m*k/N)) for k in range(nu)])
    return a
    
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
    
    cdata = data - mu
    
    figure(3)
    plot(cdata)
    title("Removing the Mean")
    
    ## here is where we will smooth using Fourier Series
    F = fftshift(fft(cdata))
    magF = abs(F)
    
    figure(4)
    plot(magF)
    title("Magnitude of Fourier Coefficients")
    
    figure(5)
    plot(magF[225:376])
    title("Magnitude of Chosen Fourier Coefficients")
    
    # Fit with sample of Fourier Coefficients
    fit_idx = r_[225:376]
    Fc = F[fit_idx]
    
#     ff = fftshift(ifft(ifftshift(Fc)))
    ff = ifft_trunc(Fc,len(fit_idx), len(data))
    
    figure(6)
    plot(ff)
    title("Smoothed Fit")
    
    
       