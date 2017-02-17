#! /usr/bin/env python
import numpy as np
import sys
import matplotlib.pyplot as plt


def createsepdata(numpts,dim,flag):
	n = numpts
	d = dim
	y = np.ones(n)
	X = np.random.uniform(-2,2,(n,d))
	if (flag == 0):
		for i in range(0,n):
			if(X[i][0]<X[i][1]):
				y[i] = 1
			else:
				y[i] = -1
	elif (flag == 1):
		for i in range(0,int(n/2)):
			X[i][1] += 6
			X[i][0] += 0.5
			y[i] = 1

		for i in range(int(n/2),n):
			X[i][0] += 6
			X[i][1] += 0.5
			y[i] = -1
			
	return X,y

