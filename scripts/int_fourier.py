from numpy import *
from scipy import *
from pylab import *

import pdb

ion()

i = 1j

def my_slow_fft(f):
    # a slow ifft that **CAN'T** interpolate!
    N = len(f)
    F = zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            F[k] += f[n]*e**(-2.0*pi*i*k*n/N)
    return (1.0/N)*F
       
def my_slow_ifft_interp(F,t):
    # a slow ifft that **CAN'T** interpolate!
    N = len(F)
    f = zeros(len(t), dtype=complex)
    for n in range(len(t)):
        for k in range(N):
            f[n] += F[k]*e**(2*pi*i*k*t[n])
    return (1.0/N)*f
    
def my_slow_ifft(F):
    # a slow ifft that **CAN'T** interpolate!
    N = len(F)
    f = zeros(N, dtype=complex)
    for n in range(N):
        for k in range(N):
            f[n] += F[k]*e**(2*pi*i*k*t[n])
    return (1.0/N)*f
    
if __name__ == "__main__":
    # Sample measurements
    ts = linspace(0,2,num=21)
    f = zeros(len(ts))
    f[0:len(ts)/2] = ts[0:len(ts)/2]
    f[len(ts)/2:] = e**-ts[len(ts)/2:] + (1.0-1/e)
    
    F = fftshift(fft(f))
    ff = fftshift(ifftshift(f))
    
    # plot where we are so far
    # this includes F^-1{F(f)} for now
    figure(1)
    plot(ts,f)
    ylim(0,1.1)
    
    figure(2)
    plot(ts,F.real,ts,F.imag)
    legend(('real', 'imaginary'))
    
    figure(3)
    plot(ts,ff)
    ylim(0,1.1)
    
    # now interpolate
    # new timestamps
    t = linspace(0,2,num=31)
    
    Fs = my_slow_fft(f)
    # using the Fourier Coefficients "as-is"
    fwi = my_slow_ifft_interp(Fs,t)
    
    figure(4)
    plot(ts,Fs.real,ts,Fs.imag)
    legend(('real', 'imaginary'))
    
    figure(5)
    plot(t,fwi)
    ylim(0,1.1)
    
    show()
    
    
    