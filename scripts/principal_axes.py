import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
from matplotlib import rc
plt.ion()

if __name__ == "__main__":
	a = 3
	b = 0
	c = 0
	d = 2
	A = np.array([[a,b],[c,d]])
	u,s,v = LA.svd(A)

	v_i = v.T

	# Plot
	origin = [0], [0]

	# unit circle
	theta = np.arange(0.0,360.0,1.0)*np.pi/180.
	x = np.cos(theta)
	y = np.sin(theta)

	# U
	fig, ax = plt.subplots(1)
	plt.quiver(*origin,[i*x for i,x in zip(s,u[0,:])], [i*y for i,y in zip(s,u[1,:])], angles='xy', scale_units='xy', color=['r','b'],scale=1)
	theta = np.arange(0.0,360.0,1.0)*np.pi/180.
	phi = np.arccos(np.dot(u[:,0],[1,0]))
	x = s[0]*np.cos(theta)
	y = s[1]*np.sin(theta)
	R = np.array([[np.cos(phi), -np.sin(phi)],
				  [np.sin(phi),  np.cos(phi)],])
	x,y = np.dot(R,np.array([x,y]))
	plt.plot(x,y)
	plt.axis('equal')
	plt.axis([-s[0]-0.1, s[0]+0.1, -s[0]-0.1, s[0]+0.1])
	ax.text(0.75, 0.49, "a", transform=ax.transAxes, fontsize=14,
        verticalalignment='top')
	ax.text(0.45, 0.75, "b", transform=ax.transAxes, fontsize=14,
        verticalalignment='top')
	plt.axis('off')

	#######
	a = 1
	b = 2
	c = 2
	d = 1
	A = np.array([[a,b],[c,d]])
	u,s,v = LA.svd(A)

	v_i = v.T


	# Plot
	origin = [0], [0]

	# unit circle
	theta = np.arange(0.0,360.0,1.0)*np.pi/180.
	x = np.cos(theta)
	y = np.sin(theta)

	# Eigen-decomposition
	w,v = np.linalg.eig(A)
	fig, ax = plt.subplots(1)
	plt.quiver(*origin,[i*x for i,x in zip(w,v[:,0])], [i*y for i,y in zip(w,v[:,1])], angles='xy', scale_units='xy', color=['r','b'],scale=1)
	theta = np.arange(0.0,360.0,1.0)*np.pi/180.
	phi = np.arccos(np.dot(u[:,0],[1,0]))
	x = s[0]*np.cos(theta)
	y = s[1]*np.sin(theta)
	R = np.array([[np.cos(phi), -np.sin(phi)],
				  [np.sin(phi),  np.cos(phi)],])
	x,y = np.dot(R,np.array([x,y]))
	plt.plot(x,y)
	plt.axis('equal')
	plt.axis([-s[0]-0.1, s[0]+0.1, -s[0]-0.1, s[0]+0.1])
	rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
	rc('text', usetex=True)
	ax.text(0.7, 0.3, r"$\displaystyle\lambda_2$", transform=ax.transAxes, fontsize=14,
        verticalalignment='top')
	ax.text(0.4, 0.5, r"$\displaystyle\lambda_1$", transform=ax.transAxes, fontsize=14,
        verticalalignment='top')
	plt.axis('off')
