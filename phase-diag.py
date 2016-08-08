from numpy import *
from matplotlib import *
from pylab import *

if __name__ == "__main__":
    x = arange(-2*pi,2*pi,0.01)
    
    figure(1)
    plot(x,sin(x))
    xlabel('x')
    ylabel('\dot{x}')