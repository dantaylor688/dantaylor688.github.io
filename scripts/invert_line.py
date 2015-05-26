from itertools import tee

from pylab import *
from matplotlib import colors
import pdb

ion()
i = 1j
if __name__ == "__main__":
    x = arange(-100,100)
    y = 4*ones_like(x)
    
    cir = 1.0/(x + i*y)
    
    # plots
    ## colors
    cit = colors.cnames.iteritems()

    # line
    figure(1)
    xlim(min(x), max(x))
    for xx, yy in zip(x,y):
        try:
            color = cit.next()[0]
        except:
            cit = colors.cnames.iteritems()
            color = cit.next()[0]
        scatter(xx, yy, facecolor='none', edgecolor=color, hold=True)
    
    # circle
    ## colors
    cit = colors.cnames.iteritems()
    figure(2)
    gap = 0.01
    mindim, maxdim = min(min(cir.real),min(cir.imag)) - gap, max(max(cir.real),max(cir.imag)) + gap
    
    ylim(min(cir.imag) - gap,max(cir.imag) + gap)
    xlim(min(cir.real) - gap, max(cir.real) + gap)
    for z in cir:
        try:
            color = cit.next()[0]
        except:
            cit = colors.cnames.iteritems()
            color = cit.next()[0]
        scatter(z.real, z.imag, facecolor='none', edgecolor=color, hold=True)