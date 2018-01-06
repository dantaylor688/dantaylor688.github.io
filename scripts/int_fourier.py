from numpy import *
from scipy import *
from pylab import *

import numpy.random as random

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
    return F
    
def my_slow_ifft(F):
    # a slow ifft that **CAN'T** interpolate!
    N = len(F)
    f = zeros(N, dtype=complex)
    for n in range(N):
        for k in range(N):
            f[n] += F[k]*e**(2.0*pi*i*k*n/N)
    return (1.0/N)*f

def my_slow_ifft_interp(F,t):
    # a slow ifft that **CAN'T** interpolate!
    N = len(F)
    f = zeros(len(t), dtype=complex)
    for n in range(len(t)):
        for k in range(N):
            f[n] += F[k]*e**(2.0*pi*i*k*t[n])
    return (1.0/N)*f
    
def my_correct_slow_ifft_interp(F,t):
    # an ifft that **CAN** interpolate
    N = len(F)
    f = zeros(len(t), dtype=complex)
    for n in range(len(t)):
        for k in range(int(N/2)):
            f[n] += F[k]*e**(2.0*pi*i*k*t[n])
        for k in range(int(N/2),N):
            f[n] += F[k]*e**(-2.0*pi*i*(N-k)*t[n])
    return (1.0/N)*f
    
if __name__ == "__main__":
    # Sample measurements
    ts = linspace(0,1,num=21)
    f = zeros(len(ts))
    hf = int(len(ts)/2)
    f[0:hf] = ts[0:hf]
    #f[hf:] = e**-ts[hf:] + 0.5 - e**-0.5
    f[hf:] = 1.0/ts[hf:] - 1.5
    #f = ts*(ts-1)
    #f = sin(ts*(2.*pi)) + cos(ts*(2.*pi))#-1.0*ts**2#exp(ts)
    
    F = fftshift(fft(f))
    F_unshifted = fft(f)
    ff = fftshift(ifftshift(f))
    
    # plot where we are so far
    # this includes F^-1{F(f)} for now
    figure(1)
    plot(ts,f, 'bo-',markerfacecolor='none', mec='blue')
    #ylim(-0.6,0.6)
    title("Original Function")
    
    figure(2)
    plot(ts,F.real,ts,F.imag)
    legend(('real', 'imaginary'))
    title("Shifted Fourier Transform")
    
    figure(22)
    plot(ts,F_unshifted.real,ts,F_unshifted.imag)
    legend(('real', 'imaginary'))
    title("Unshifted Fourier Transform")
    
    figure(3)
    plot(ts,ff)
    #ylim(-0.6,0.6)
    title("Getting Back The Original")
    
    # now interpolate
    # new timestamps, m samples between former samples. 
    Nf = len(ts)
    
    t = linspace(0,1,num=len(ts)*3)
    
    Fs = my_slow_fft(f)
    fm = my_slow_ifft(Fs)
    
    # using the Fourier Coefficients "sas-is"
    fwi = my_slow_ifft_interp(F_unshifted,t)
    fci = my_correct_slow_ifft_interp(F_unshifted,t)
    
    figure(4)
    plot(ts,Fs.real,ts,Fs.imag)
    legend(('real', 'imaginary'))
    title("My Unshifted Fourier Transform")

    figure(5)
    plot(ts,f, 'bo-',markerfacecolor='none', mec='blue')
    plot(ts,fm,'g^-',markerfacecolor='none', mec='green')
    #ylim(-0.6,0.6)
    title("Original Using My Inverse")
    
    figure(500)
    plot(ts,f, 'bo-',markerfacecolor='none', mec='blue')
    plot(ts[:-1],my_correct_slow_ifft_interp(fft(f[:-1]),ts[:-1]),'g^-',markerfacecolor='none', mec='green')
    #ylim(-0.6,0.6)
    title("Original Using My Inverse Interp ")
	
    figure(6)
    plot(ts,f, 'bo-',markerfacecolor='none', mec='blue')
    plot(t,fwi,'go-',markerfacecolor='none', mec='green')
    #ylim(-0.6,0.6)
    legend(('original', 'interpolatation'))
    title("Interpolating with Fourier Coefficients, No Change")
    
    figure(7)
    plot(ts,f,'bo-',markerfacecolor='none', mec='blue')
    plot(t[:-1],my_correct_slow_ifft_interp(fft(f[:-1]),t[:-1]),'g^-',markerfacecolor='none', mec='green')
    #ylim(-0.6,0.6)
    legend(('original', 'interpolatation'))
    title("Interpolating with Fourier Coefficients Accounting for Aliasing")
    
    show()