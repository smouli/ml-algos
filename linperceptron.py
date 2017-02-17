#! /usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import math as mt

def linperceptron(itr,trainset,lbls):
	L = itr
	X = trainset
	y = lbls
	n = len(X)
	d = len(X[0])
	theta = np.random.rand(d)
	for i in range(0,L):
		for t in range(0,n):
			if (y[t]*np.dot(theta,X[t]) <= 0):
				for k in range(0,d):
					theta[k] = theta[k] + y[t]*X[t][k]
	return theta

def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi)

def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)

def linperceptronvisual(trainset,lbls,test,theta):
	X = trainset
	y = lbls
	xlabel1 = []
	ylabel1 = []
	xlabel2 = []
	ylabel2 = []
	for i in range(0,len(y)):
		if(y[i] == 1):
			xlabel1.append(X[i][0])
			ylabel1.append(X[i][1])
		else:
			xlabel2.append(X[i][0])
			ylabel2.append(X[i][1])
	rho,phi = cart2pol(theta[0],theta[1])
	deg = mt.degrees(phi)
	xpt1,ypt1 = pol2cart(rho,mt.radians(deg+90))
	xpt2,ypt2 = pol2cart(rho,mt.radians(deg+270))
	plt.plot([0,1.5*xpt1,1.5*xpt2],[0,1.5*ypt1,1.5*ypt2],color='black')
	test = plt.scatter(test[0],test[1],color='green')
	pospts = plt.scatter(xlabel1,ylabel1,color='blue')
	negpts = plt.scatter(xlabel2,ylabel2,color='red')
	plt.legend((test,pospts,negpts),('test','label +1','label -1'))
	plt.show()