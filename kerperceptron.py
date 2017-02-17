#! /usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as la
import math as mt

def kernel(x1,x2):
	norm = la.norm(x1-x2)
	normsq = mt.pow(norm,2)
	return mt.exp(-1/2 * normsq)

def kernelmatrix(X):
	n = len(X)
	K = np.ones((n,n))
	for i in range(0,n):
		for j in range(0,n):
			K[i][j] = kernel(X[i],X[j])
	return K

def updatesum(alpha,y,K,ind):
	sumval = 0
	n = len(K)
	for i in range(0,n):
		sumval += alpha[i]*y[i]*K[i][ind]
	return sumval

def kerperceptron(itr,trainset,lbls):
	L = itr
	X = trainset
	y = lbls
	n = len(X)
	d = len(X[0])
	alpha = np.zeros(n)
	K = kernelmatrix(X)
	for i in range(0,L):
		for t in range(0,n):
			sumval = updatesum(alpha,y,K,t)
			if (y[t]*sumval <= 0):
				alpha[t]+=1
	return alpha

def kerperceptronvisual(trainset,lbls,test):
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
	test = plt.scatter(test[0],test[1],color='green')
	pospts = plt.scatter(xlabel1,ylabel1,color='blue')
	negpts = plt.scatter(xlabel2,ylabel2,color='red')
	plt.legend((test,pospts,negpts),('test','label +1','label -1'))
	plt.show()

