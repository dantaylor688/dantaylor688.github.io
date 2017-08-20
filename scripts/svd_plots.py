import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
from matplotlib import rc
plt.ion()

if __name__ == "__main__":
	a = 1
	b = 2
	c = 0
	d = 2
	A = np.array([[a,b],[c,d]])
	u,s,v = LA.svd(A)
	
	v_i = v.T
	
	
	# Plot
	origin = [0], [0]
	
	# V
	plt.subplot(121)
	plt.quiver(*origin,v_i[0,:], v_i[1,:], angles='xy', scale_units='xy', color=['r','b'],scale=1)
	# unit circle
	theta = np.arange(0.0,360.0,1.0)*np.pi/180.
	x = np.cos(theta)
	y = np.sin(theta)
	plt.plot(x,y)
	plt.axis('equal')
	plt.axis([-s[0]-0.1, s[0]+0.1, -s[0]-0.1, s[0]+0.1])

	plt.title('v')
	# U
	plt.subplot(122)
	plt.quiver(*origin,[i*x for i,x in zip(s,u[0,:])], [i*y for i,y in zip(s,u[1,:])], angles='xy', scale_units='xy', color=['r','b'],scale=1)
	theta = np.arange(0.0,360.0,1.0)*np.pi/180.
	phi = np.arccos(np.dot(u[:,0],[1,0]))
	x = s[0]*np.cos(theta)
	y = s[1]*np.sin(theta)
	R = np.array([[np.cos(phi), -np.sin(phi)],
				  [np.sin(phi),  np.cos(phi)],])
	x,y = np.dot(R,np.array([x,y]))
	plt.plot(x,y)
	plt.title('Av=u')
	plt.axis('equal')
	plt.axis([-s[0]-0.1, s[0]+0.1, -s[0]-0.1, s[0]+0.1])
	
	"""
	plt.figure(1)
	
	ax1.arrow(0,0,v_i[0,0],v_i[1,0], head_width=0.05, head_length=0.1, fc='k', ec='k')
	ax1.arrow(0,0,v_i[0,1],v_i[1,1], head_width=0.05, head_length=0.1, fc='k', ec='k')
	ax1.set_title('V')
	ax1.arrow(0,0,s[0]*u[0,0],s[0]*u[1,0], head_width=0.05, head_length=0.1, fc='k', ec='k')
	ax1.arrow(0,0,s[1]*u[0,1],s[1]*u[1,1], head_width=0.05, head_length=0.1, fc='k', ec='k')
	ax2.set_title('U')
	"""
	
	