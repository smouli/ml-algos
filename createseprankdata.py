#! /usr/bin/env python
import numpy as np
import sys
import matplotlib.pyplot as plt
import math as mt
import scipy.linalg as la

def createseprankdata(numpts,dim,numlbls):
	n = numpts
	d = dim
	k = numlbls
	X = np.random.rand(n,d)
	y = np.zeros(n)
	print y
	i = 0
	#print(n,d,k)
	for l in range(1,k+1):
		j = int(mt.ceil(l*n/k))
		#print(X[0:0][0])
		print j
		#print i,(l/k*n)
		X[i:j][0] = X[i:j][0] + 1.5*l
		y[i:j] = l
		i = j
	U = la.orth(np.random.rand(d,d))
	X = np.matmul(X,U)
	print(X)
	return X,y

'''numpts = int(sys.argv[1])
dim = int(sys.argv[2])
numlbls = int(sys.argv[3])
createseprankdata(numpts,dim,numlbls)'''
