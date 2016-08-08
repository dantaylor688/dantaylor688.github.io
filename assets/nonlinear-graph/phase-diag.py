from numpy import *
from matplotlib import *
from pylab import *

if __name__ == "__main__":
    rc('text', usetex=True)
    rc('font', family='serif')
    fs = 20
    x = arange(-2*pi,2*pi,0.01)
    szx = [-pi,pi]
    uzx = [-2*pi,0,2*pi]
    
    fig = figure(1)
    ax = fig.add_subplot(111)
    ax.plot(x,sin(x),'b')
    xlabel(r'$x$',fontsize=fs)
    ylabel(r'$\dot{x}$',fontsize=fs)
    xlim([-2*pi,2*pi])
    xticks( [-2*pi,-pi,0,pi,2*pi], (r'$-2\pi$', r'-\pi', r'$0$', r'$\pi$', r'$2\pi$') )
    ax.plot(uzx,zeros_like(uzx),'o',mfc='none', mec='b')
    ax.plot(szx,zeros_like(szx),'o',mfc='b', mec='b')
    ax.plot(x,zeros_like(x),'k')
    
    ## arrows
    # -2pi
    annotate('', xy=(-3*pi/2, 0), xytext=(-2*pi, 0),
                arrowprops=dict(facecolor='black', shrink=0.04, width=1),
                )
    # -pi
    annotate('', xy=(-pi/2, 0), xytext=(0, 0),
                arrowprops=dict(facecolor='black', shrink=0.04, width=1),
                )
    
    # 0 - pi
    
    annotate('', xy=(pi/2, 0), xytext=(0, 0),
                arrowprops=dict(facecolor='black', shrink=0.04, width=1),
                )
                
    # 2pi
    annotate('', xy=(3*pi/2, 0), xytext=(2*pi, 0),
                arrowprops=dict(facecolor='black', shrink=0.04, width=1),
                )
    
    t = arange(0,10,0.01)
    x0 = pi/4
    fig = figure(2)
    ax = fig.add_subplot(111)
    ax.plot(t,pi*ones_like(t),'b')
    ax.plot(t,-pi*ones_like(t),'b')
    for x0 in [pi/4,pi/6,pi/2,3*pi/2, 8*pi/3,-3*pi/2,-pi/2,-pi/4, -pi/6, -8*pi/3]:
        xt = 2.0*arctan((1.0/(1.0/sin(x0) + 1.0/tan(x0)))*e**t)            
        ax.plot(t,xt,'b--')
        
    xlabel(r'$t$',fontsize=fs)
    ylabel(r'$x$',fontsize=fs)
    yticks( [-pi,0,pi], (r'-\pi', r'$0$', r'$\pi$') )
    ylim([-pi,pi])
    show()