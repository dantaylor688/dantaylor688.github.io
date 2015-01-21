from numpy import *
from pylab import *
from scipy import *

from datetime import datetime

ion()
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
    
       