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
    ax = fig.add_subplot(311)
    frame1 = plt.gca()
    hold
    r = 2
    xdot = r*x - x**2
    ax.plot(x,xdot,'b-')
    ylim([min(xdot),max(xdot)+3])
    xlim([min(x),max(x)])
    ax.plot(x,zeros_like(x),'k-')
    ax.plot(0,0,'bo',mfc='none',mec='b')
    ax.plot(r,0,'bo',fillstyle='full',mec='b')
    ax.set_title(r'$r > 0$')
    frame1.axes.get_xaxis().set_visible(False)
    frame1.axes.get_yaxis().set_visible(False)

    ax.annotate('', xy=(-2, 0), xytext=(-1, 0),
             arrowprops=dict(facecolor='black', shrink=0.04, width=1),
             )
    ax.annotate('', xy=(r-1, 0), xytext=(0.5, 0),
             arrowprops=dict(facecolor='black', shrink=0.04, width=1),
             )
    ax.annotate('', xy=(r+1, 0), xytext=(r+2, 0),
             arrowprops=dict(facecolor='black', shrink=0.04, width=1),
             )

    # lft = mlines.Line2D.fillStyles
    # r = 0
    ax = fig.add_subplot(312)
    frame1 = plt.gca()
    r = 0
    xdot = r*x - x**2
    ax.plot(x,xdot,'b-')
    ax.plot(0,0,'bo',fillstyle='right',mec='b')
    ylim([min(xdot),max(xdot)+3])
    xlim([min(x),max(x)])
    ax.plot(x,zeros_like(x),'k-')
    ax.set_title(r'$r = 0$')
    frame1.axes.get_xaxis().set_visible(False)
    frame1.axes.get_yaxis().set_visible(False)

    ax.annotate('', xy=(r-2, 0), xytext=(r-1, 0),
                arrowprops=dict(facecolor='black', shrink=0.04, width=1),
                )
    ax.annotate('', xy=(2, 0), xytext=(3, 0),
                arrowprops=dict(facecolor='black', shrink=0.04, width=1),
                )

    # r < 0
    ax = fig.add_subplot(313)
    frame1 = plt.gca()
    r = -2
    xdot = r*x - x**2
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

    ax.annotate('', xy=(r - 2, 0), xytext=(r-1, 0),
                arrowprops=dict(facecolor='black', shrink=0.04, width=1),
                )
    ax.annotate('', xy=(-0.5, 0), xytext=(r+0.5, 0),
                arrowprops=dict(facecolor='black', shrink=0.04, width=1),
                )
    ax.annotate('', xy=(-r-1, 0), xytext=(-r, 0),
                arrowprops=dict(facecolor='black', shrink=0.04, width=1),
                )
                
    # bifurcation diagram
    x = arange(-5,5,0.1)
    fig= figure(2)
    ax = fig.add_subplot(111)
    frame1 = plt.gca()
    hold
    rp = arange(0,5,0.1)
    rn = arange(-5,0,0.1)
    rzp = zeros_like(arange(0,5,0.1))
    rzn = zeros_like(arange(-5,0,0.1))
    ax.plot(arange(-5,0,0.1),rzn,'b-')
    ax.plot(arange(0,5,0.1),rzp,'b--')
    ax.plot(arange(-5,0,0.1),rn,'b--')
    ax.plot(arange(0,5,0.1),rp,'b-')
    axvline(x=0,color='k')
    ax.set_title(r'$x^* = 0$')
    frame1.axes.get_xaxis().set_visible(False)
    frame1.axes.get_yaxis().set_visible(False)
    
    ## log example
    
    x = arange(-0.999, 5, 0.02)
    fig = figure(3)
    i = 1
    my_xticks = ['' for j in x]
    zidx = nonzero(x == min(abs(x)))[0][0]
    my_xticks[zidx] = '0'
    for r in [-2,1,2]:
        ax = fig.add_subplot(310+i)
        plot(r*x - log(1+x))
        plot(zeros_like(x),'k-')
        a = ax.get_xticks().tolist()
        a[0:1] = ['',0]
        a[2:] = ['' for k in a[2:]]
        ax.set_xticklabels(a)
        frame1 = plt.gca()
        # frame1.axes.get_xaxis().set_visible(False)
        frame1.axes.get_yaxis().set_visible(False)
        i += 1
    
    fig = figure(4)
    rn = arange(-0.999,0.01,0.1)
    rp = arange(0.01,5,0.1)    
    r = log(1+rp)/rp
    rr = log(1+rn)/rn
    ax = fig.add_subplot(111)
    plot(zeros(8),'k-')
    plot(r,rp,'b--')
    plot(rr,rn,'b-')
    
    
    a[0:1] = ['',1]
    a[2:] = ['' for k in a[2:]]
    ax.set_xticklabels(a)
    frame1 = plt.gca()
    # frame1.axes.get_xaxis().set_visible(False)
    frame1.axes.get_yaxis().set_visible(False)
    xlabel(r'$r$',fontsize=fs)
    ylabel(r'$x^*$',fontsize=fs)
    ax.set_title(r'$x^* = 0$')
    
    # linear approximation
    fig = figure(5)    
    ax = fig.add_subplot(111)
    rn = arange(0,1,0.01)
    rp = arange(1,2,0.1)
    plot(rn,2-2*rn,'b--')
    plot(rp,2-2*rp,'b')
    plot(zeros(4),'k-')
    plot(rn,zeros_like(rn),'b-')
    a[0:1] = ['',1]
    a[2:] = ['' for k in a[2:]]
    ax.set_xticklabels(a)
    frame1 = plt.gca()
    # frame1.axes.get_xaxis().set_visible(False)
    frame1.axes.get_yaxis().set_visible(False)
    xlabel(r'$r$',fontsize=fs)
    ax.set_title(r'$x^* = 0$')
    
    # both
    fig = figure(6)    
    ax = fig.add_subplot(111)
    rn = arange(0,1,0.1)
    rp = arange(1,2,0.1)
    plot(zeros(8),'k-')
    plot(rn,2-2*rn,'b--')
    plot(rp,2-2*rp,'b')
    rn = arange(-0.999,0.01,0.1)
    rp = arange(0.01,2,0.1)
    r = log(1+rp)/rp
    rr = log(1+rn)/rn
    plot(r,rp,'g--')
    plot(rr,rn,'g-')
    plot(rn,zeros_like(rn),'-')
    a[0:1] = ['',1]
    a[2:] = ['' for k in a[2:]]
    ax.set_xticklabels(a)
    frame1 = plt.gca()
    # frame1.axes.get_xaxis().set_visible(False)
    frame1.axes.get_yaxis().set_visible(False)
    xlabel(r'$r$',fontsize=fs)
    ax.set_title(r'$x^* = 0$')
    
    show()
    
    