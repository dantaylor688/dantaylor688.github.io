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
    r = 5
    xdot = r + x**2
    ax.plot(x,xdot,'b-')
    ylim([min(xdot)-(r+1),max(xdot)])
    ax.plot(x,zeros_like(x),'k-')
    ax.set_title(r'$r > 0$')
    frame1.axes.get_xaxis().set_visible(False)
    frame1.axes.get_yaxis().set_visible(False)

    ax.annotate('', xy=(-2, 0), xytext=(-3, 0),
             arrowprops=dict(facecolor='black', shrink=0.04, width=1),
             )
    ax.annotate('', xy=(3, 0), xytext=(2, 0),
             arrowprops=dict(facecolor='black', shrink=0.04, width=1),
             )

    # lft = mlines.Line2D.fillStyles
    # r = 0
    ax = fig.add_subplot(312)
    frame1 = plt.gca()
    r = 0
    xdot = r + x**2
    ax.plot(x,xdot,'b-')
    ax.plot(0,0,'bo',fillstyle='left',mec='b')
    ylim([-1,max(xdot)])
    ax.plot(x,zeros_like(x),'k-')
    ax.set_title(r'$r = 0$')
    frame1.axes.get_xaxis().set_visible(False)
    frame1.axes.get_yaxis().set_visible(False)

    ax.annotate('', xy=(-2, 0), xytext=(-3, 0),
                arrowprops=dict(facecolor='black', shrink=0.04, width=1),
                )
    ax.annotate('', xy=(3, 0), xytext=(2, 0),
                arrowprops=dict(facecolor='black', shrink=0.04, width=1),
                )

    # r < 0
    ax = fig.add_subplot(313)
    frame1 = plt.gca()
    r = -5
    xdot = r + x**2
    ax.plot(x,xdot,'b-')
    ax.plot(sqrt(-r),0,'bo',mfc='none',mec='b')
    ax.plot(-sqrt(-r),0,'bo',fillstyle='full',mec='b')
    ylim([min(xdot)-1,max(xdot)])
    ax.plot(x,zeros_like(x),'k-')
    ax.set_title(r'$r < 0$')
    xlabel(r'$x$',fontsize=fs)
    ylabel(r'$\dot{x}$',fontsize=fs)
    frame1.axes.get_xaxis().set_visible(False)
    frame1.axes.get_yaxis().set_visible(False)

    ax.annotate('', xy=(-sqrt(-r)-1, 0), xytext=(-sqrt(-r) - 2, 0),
                arrowprops=dict(facecolor='black', shrink=0.04, width=1),
                )
    ax.annotate('', xy=(0, 0), xytext=(sqrt(-r)/2., 0),
                arrowprops=dict(facecolor='black', shrink=0.04, width=1),
                )
                
    ax.annotate('', xy=(sqrt(-r)+2, 0), xytext=(sqrt(-r) + 1, 0),
                arrowprops=dict(facecolor='black', shrink=0.04, width=1),
                )
    ### Just axes
    # r > 0
    fig= figure(500)
    ax = fig.add_subplot(311)
    frame1 = plt.gca()
    hold
    r = 5
    ylim([-1,1])
    ax.plot(x,zeros_like(x),'k-')
    ax.set_title(r'$r > 0$')
    frame1.axes.get_xaxis().set_visible(False)
    frame1.axes.get_yaxis().set_visible(False)

    ax.annotate('', xy=(-2, 0), xytext=(-3, 0),
             arrowprops=dict(facecolor='black', shrink=0.04, width=1),
             )
    ax.annotate('', xy=(3, 0), xytext=(2, 0),
             arrowprops=dict(facecolor='black', shrink=0.04, width=1),
             )

    # lft = mlines.Line2D.fillStyles
    # r = 0
    ax = fig.add_subplot(312)
    frame1 = plt.gca()
    r = 0
    ax.plot(0,0,'ko',fillstyle='left',mec='k')
    ylim([-1,1])
    ax.plot(x,zeros_like(x),'k-')
    ax.set_title(r'$r = 0$')
    frame1.axes.get_xaxis().set_visible(False)
    frame1.axes.get_yaxis().set_visible(False)

    ax.annotate('', xy=(-2, 0), xytext=(-3, 0),
                arrowprops=dict(facecolor='black', shrink=0.04, width=1),
                )
    ax.annotate('', xy=(3, 0), xytext=(2, 0),
                arrowprops=dict(facecolor='black', shrink=0.04, width=1),
                )

    # r < 0
    ax = fig.add_subplot(313)
    frame1 = plt.gca()
    r = -5
    ax.plot(sqrt(-r),0,'ko',mfc='none',mec='k')
    ax.plot(-sqrt(-r),0,'ko',fillstyle='full',mec='k')
    ylim([-1,1])
    ax.plot(x,zeros_like(x),'k-')
    ax.set_title(r'$r < 0$')
    xlabel(r'$x$',fontsize=fs)
    ylabel(r'$\dot{x}$',fontsize=fs)
    frame1.axes.get_xaxis().set_visible(False)
    frame1.axes.get_yaxis().set_visible(False)

    ax.annotate('', xy=(-sqrt(-r)-1, 0), xytext=(-sqrt(-r) - 2, 0),
                arrowprops=dict(facecolor='black', shrink=0.04, width=1),
                )
    ax.annotate('', xy=(0, 0), xytext=(sqrt(-r)/2., 0),
                arrowprops=dict(facecolor='black', shrink=0.04, width=1),
                )
                
    ax.annotate('', xy=(sqrt(-r)+2, 0), xytext=(sqrt(-r) + 1, 0),
                arrowprops=dict(facecolor='black', shrink=0.04, width=1),
                )
                
    ### Example 2
    #r > 0 
    x = arange(-0.99,5,0.01)
    lx = arange(-2,5,0.01)
    r = 1
    fig= figure(2)
    ax = fig.add_subplot(311)
    frame1 = plt.gca()
    hold
    ax.plot(lx,r+lx,'b-')
    ax.plot(x,log(1+x),'g-')
    ax.plot(lx,zeros_like(lx),'k-')
    xlabel(r'$x$',fontsize=fs)
    ylabel(r'$\dot{x}$',fontsize=fs)
    xlim([-2,5])
    ylim([-4,5])
    title(r'$r > 0$')
    ax.annotate('', xy=(-0.5, 0), xytext=(-1, 0),
             arrowprops=dict(facecolor='black', shrink=0.04, width=1),
             )
    ax.annotate('', xy=(2.5, 0), xytext=(2, 0),
             arrowprops=dict(facecolor='black', shrink=0.04, width=1),
             )
    frame1.axes.get_xaxis().set_visible(False)
    frame1.axes.get_yaxis().set_visible(False)
    
    # r = 0 
    x = arange(-0.99,5,0.01)
    lx = arange(-2,5,0.01)
    r = 0
    # fig= figure(3)
    ax = fig.add_subplot(312)
    frame1 = plt.gca()
    hold
    ax.plot(lx,r+lx,'b-')
    ax.plot(x,log(1+x),'g-')
    ax.plot(lx,zeros_like(lx),'k-')
    ax.plot(0,0,'ko',fillstyle='left',mec='b')
    xlabel(r'$x$',fontsize=fs)
    ylabel(r'$\dot{x}$',fontsize=fs)
    xlim([-2,5])
    ylim([-4,5])
    ax.set_title(r'$r = 0$')
    ax.annotate('', xy=(-0.5, 0), xytext=(-1, 0),
             arrowprops=dict(facecolor='black', shrink=0.04, width=1),
             )
    ax.annotate(r'$r_c$', xy=(0, 0), xytext=(-0.3, 0.3))
    ax.annotate('', xy=(2.5, 0), xytext=(2, 0),
             arrowprops=dict(facecolor='black', shrink=0.04, width=1),
             )
    frame1.axes.get_xaxis().set_visible(False)
    frame1.axes.get_yaxis().set_visible(False)
    
    # r < 0 
    x = arange(-0.99,5,0.01)
    lx = arange(-2,5,0.01)
    r = -1
    # fig= figure(4)
    ax = fig.add_subplot(313)
    xlabel(r'$x$',fontsize=fs)
    ylabel(r'$\dot{x}$',fontsize=fs)
    frame1 = plt.gca()
    hold
    ax.plot(lx,r+lx,'b-')
    ax.plot(x,log(1+x),'g-')
    ax.plot(lx,zeros_like(lx),'k-')
    ax.plot(-0.8,0,'ko',fillstyle='full',mec='k')
    ax.plot(2.1,0,'ko',mfc='none',mec='k')
    xlim([-2,5])
    ylim([-4,5])
    ax.set_title(r'$r < 0$')
    ax.annotate('', xy=(0.1, 0), xytext=(0.8, 0),
             arrowprops=dict(facecolor='black', shrink=0.04, width=1),
             )
    ax.annotate('', xy=(-1.5, 0), xytext=(-1.9, 0),
      arrowprops=dict(facecolor='black', shrink=0.04, width=1),
      )
    ax.annotate('', xy=(3, 0), xytext=(2.5, 0),
             arrowprops=dict(facecolor='black', shrink=0.04, width=1),
             )
    frame1.axes.get_xaxis().set_visible(False)
    frame1.axes.get_yaxis().set_visible(False)
    
    # r < 0 again as a separate plot
    x = arange(-0.99,5,0.01)
    lx = arange(-2,5,0.01)
    r = -1
    fig= figure(4)
    ax = fig.add_subplot(111)
    frame1 = plt.gca()
    hold
    ax.plot(lx,r+lx,'b-')
    ax.plot(x,log(1+x),'g-')
    xlabel(r'$x$',fontsize=fs)
    ylabel(r'$\dot{x}$',fontsize=fs)
    ax.plot(lx,zeros_like(lx),'k-')
    ax.plot(-0.8,0,'ko',fillstyle='full',mec='k')
    ax.plot(2.1,0,'ko',mfc='none',mec='k')
    xlim([-2,5])
    ylim([-4,5])
    ax.set_title(r'$r < 0$')
    ax.annotate('', xy=(0.1, 0), xytext=(0.8, 0),
             arrowprops=dict(facecolor='black', shrink=0.04, width=1),
             )
    ax.annotate('', xy=(-1.5, 0), xytext=(-1.9, 0),
      arrowprops=dict(facecolor='black', shrink=0.04, width=1),
      )
    ax.annotate('', xy=(3, 0), xytext=(2.5, 0),
             arrowprops=dict(facecolor='black', shrink=0.04, width=1),
             )
    frame1.axes.get_xaxis().set_visible(False)
    frame1.axes.get_yaxis().set_visible(False)
    
    ## Bifurcation diagram example log(1+x)
    x = arange(-0.99,5,0.01)
    lx = arange(-2,5,0.01)
    r = -1
    fig= figure(4)
    ax = fig.add_subplot(111)
    frame1 = plt.gca()
    hold
    ax.plot(lx,r+lx,'b-')
    ax.plot(x,log(1+x),'g-')
    ax.plot(lx,zeros_like(lx),'k-')
    ax.plot(-0.8,0,'ko',fillstyle='full',mec='k')
    xlabel(r'$x$',fontsize=fs)
    ylabel(r'$\dot{x}$',fontsize=fs)
    ax.plot(2.1,0,'ko',mfc='none',mec='k')
    xlim([-2,5])
    ylim([-4,5])
    ax.set_title(r'$r < 0$')
    ax.annotate('', xy=(0.1, 0), xytext=(0.8, 0),
             arrowprops=dict(facecolor='black', shrink=0.04, width=1),
             )
    ax.annotate('', xy=(-1.5, 0), xytext=(-1.9, 0),
      arrowprops=dict(facecolor='black', shrink=0.04, width=1),
      )
    ax.annotate('', xy=(3, 0), xytext=(2.5, 0),
             arrowprops=dict(facecolor='black', shrink=0.04, width=1),
             )
    frame1.axes.get_xaxis().set_visible(False)
    frame1.axes.get_yaxis().set_visible(False)
    
    ### Bifurcation diagram
    ## r = log(1+x)-x
    nx = arange(-0.99,0,0.01)
    px = arange(0,5,0.01)
    fig= figure(650)
    ax = fig.add_subplot(111)
    frame1 = plt.gca()
    hold
    ax.plot(log(1+nx)-nx,nx,'b-')
    ax.plot(log(1+px)-px,px,'b--')
    ax.plot(arange(-5,6),zeros_like(arange(-5,6)),'k-')
    ylabel(r'$x^*$',fontsize=fs)
    xlabel(r'$r$',fontsize=fs)
    xlim([-5,5])
    ax.annotate('Stable', xy=(-4, 16), xytext=(-3,17),
             arrowprops=dict(facecolor='black', shrink=0.04, width=1),
             )
    ax.annotate('Unstable', xy=(4, 16), xytext=(2, 17),
             arrowprops=dict(facecolor='black', shrink=0.04, width=1),
             )
    frame1.axes.get_xaxis().set_visible(True)
    frame1.axes.get_yaxis().set_visible(True)
    

    ## x = +-sqrt(-r)
    rp = arange(0,5,0.01)
    fig= figure(6001)
    lx = arange(-5,3,0.01)
    ax = fig.add_subplot(111)
    frame1 = plt.gca()
    hold
    ax.plot(-rp,sqrt(rp),'b--')
    ax.plot(-rp,-sqrt(rp),'b-')
    ax.plot(lx,zeros_like(lx),'k-')
    xlabel(r'$r$',fontsize=fs)
    ylabel(r'$x^*$',fontsize=fs)
    xlim([-5,3])
    ax.annotate('Stable', xy=(-4, -2), xytext=(-3,-2.5),
             arrowprops=dict(facecolor='black', shrink=0.04, width=1),
             )
    ax.annotate('Unstable', xy=(-4, 2), xytext=(-3, 2.5),
             arrowprops=dict(facecolor='black', shrink=0.04, width=1),
             )
    frame1.axes.get_xaxis().set_visible(True)
    frame1.axes.get_yaxis().set_visible(True)
    show()
    
    