from numpy import *
from matplotlib import *
from pylab import *
import matplotlib.lines as mlines

if __name__ == "__main__":
    rc('text', usetex=True)
    rc('font', family='serif')
    fs = 20
    ### Example 1
    x = arange(-5,5,0.1)
    

    # r > 0
    fig= figure(1)
    ax = fig.add_subplot(313)
    frame1 = plt.gca()
    hold
    r = 10
    xdot = r*x - x**3
    ax.plot(x,xdot,'b-')
    ylim([min(xdot),max(xdot)+3])
    xlim([min(x),max(x)])
    ax.plot(x,zeros_like(x),'k-')
    ax.plot(sqrt(r),0,'bo',fillstyle='full',mec='b')
    ax.plot(-sqrt(r),0,'bo',fillstyle='full',mec='b')
    ax.plot(0,0,'bo',mfc='none',mec='b')
    ax.set_title(r'$r > 0$')
    frame1.axes.get_xaxis().set_visible(False)
    frame1.axes.get_yaxis().set_visible(False)

    ax.annotate('', xy=(-2, 0), xytext=(-1, 0),
             arrowprops=dict(facecolor='black', shrink=0.04, width=1),
             )
    ax.annotate('', xy=(2, 0), xytext=(1, 0),
             arrowprops=dict(facecolor='black', shrink=0.04, width=1),
             )


    # lft = mlines.Line2D.fillStyles
    # r = 0
    ax = fig.add_subplot(312)
    frame1 = plt.gca()
    r = 0
    xdot = r*x - x**3
    ax.plot(x,xdot,'b-')
    ax.plot(0,0,'bo',fillstyle='full',mec='b')
    ylim([min(xdot),max(xdot)+3])
    xlim([min(x),max(x)])
    ax.plot(x,zeros_like(x),'k-')
    ax.set_title(r'$r = 0$')
    frame1.axes.get_xaxis().set_visible(False)
    frame1.axes.get_yaxis().set_visible(False)

    ax.annotate('', xy=(-2, 0), xytext=(-3, 0),
             arrowprops=dict(facecolor='black', shrink=0.04, width=1),
             )
    ax.annotate('', xy=(2, 0), xytext=(3, 0),
                arrowprops=dict(facecolor='black', shrink=0.04, width=1),
                )

    # r < 0
    ax = fig.add_subplot(311)
    frame1 = plt.gca()
    r = -5
    xdot = r*x - x**3
    ax.plot(x,xdot,'b-')
    ax.plot(0,0,'bo',fillstyle='full',mec='b')
    ax.plot(r,0,'bo', mfc='none',mec='b')
    ylim([min(xdot)-1,max(xdot)+3])
    xlim([min(x),max(x)])
    ax.plot(x,zeros_like(x),'k-')
    ax.set_title(r'$r < 0$')
    xlabel(r'$x$',fontsize=fs)
    ylabel(r'$\dot{x}$',fontsize=fs)
    frame1.axes.get_xaxis().set_visible(False)
    frame1.axes.get_yaxis().set_visible(False)

    ax.annotate('', xy=(-2, 0), xytext=(-3, 0),
             arrowprops=dict(facecolor='black', shrink=0.04, width=1),
             )
    ax.annotate('', xy=(2, 0), xytext=(3, 0),
                arrowprops=dict(facecolor='black', shrink=0.04, width=1),
                )
                
    # bifurcation diagram
    x = arange(-5,5,0.1)
    fig= figure(2)
    ax = fig.add_subplot(111)
    frame1 = plt.gca()
    hold
    rpp = sqrt(arange(0,5,0.1))
    rpn = -1*sqrt(arange(0,5,0.1))
    rn = zeros_like(arange(-5,0,0.1))
    rzp = zeros_like(arange(0,5,0.1))
    rzn = zeros_like(arange(-5,0,0.1))
    ax.plot(arange(-5,0,0.1),rzn,'b-')
    ax.plot(arange(0,5,0.1),rzp,'b--')
    ax.plot(arange(0,5,0.1),rpp,'b-')
    ax.plot(arange(0,5,0.1),rpn,'b-')
    axvline(x=0,color='k')
    ax.set_title(r'$x^* = 0$')
    frame1.axes.get_xaxis().set_visible(False)
    frame1.axes.get_yaxis().set_visible(False)
    
    # subcritical
    
    # bifurcation diagram
    x = arange(-5,5,0.1)
    fig= figure(3)
    ax = fig.add_subplot(111)
    frame1 = plt.gca()
    hold
    rpp = sqrt(arange(0,5,0.1))
    rpn = -1*sqrt(arange(0,5,0.1))
    rn = zeros_like(arange(-5,0,0.1))
    rzp = zeros_like(arange(0,5,0.1))
    rzn = zeros_like(arange(-5,0,0.1))
    ax.plot(arange(-5,0,0.1),rzn,'b-')
    ax.plot(arange(0,5,0.1),rzp,'b--')
    ax.plot(arange(-5,0,0.1),rpp[::-1],'b--')
    ax.plot(arange(-5,0,0.1),rpn[::-1],'b--')
    axvline(x=0,color='k')
    ax.set_title(r'$x^* = 0$')
    frame1.axes.get_xaxis().set_visible(False)
    frame1.axes.get_yaxis().set_visible(False)
    
    # stabilize
    x = arange(-5,5,0.1)
    fig= figure(4)
    ax = fig.add_subplot(111)
    frame1 = plt.gca()
    hold
    rpp = sqrt(arange(0,5,0.1))
    rpn = -1*sqrt(arange(0,5,0.1))
    rn = zeros_like(arange(-5,0,0.1))
    rzp = zeros_like(arange(0,5,0.1))
    rzn = zeros_like(arange(-5,0,0.1))
    rps = sqrt(arange(0,10,0.1)) + rpp[-1]
    rpns = -1*sqrt(arange(0,10,0.1)) + rpn[-1]
    
    ax.plot(arange(-5,0,0.1),rzn,'b-')
    ax.plot(arange(0,5,0.1),rzp,'b--')
    ax.plot(arange(-5,0,0.1),rpp[::-1],'b--')
    ax.plot(arange(-5,0,0.1),rpn[::-1],'b--')
    
    ax.plot(arange(-5,5,0.1),rps,'b-')
    ax.plot(arange(-5,5,0.1),rpns,'b-')
    axvline(x=0,color='k')
    ax.set_title(r'$x^* = 0$')
    frame1.axes.get_xaxis().set_visible(False)
    frame1.axes.get_yaxis().set_visible(False)
    
    show()