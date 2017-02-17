#! /usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import math as mt
from createseprankdata import *

def prank(itr,numlbls,trainset,lbls):
	L = itr
	k = numlbls
	X = trainset
	y = lbls
	n = len(X)
	d = len(X[0])
	theta =  np.zeros(d)
	b = np.zeros(k-1)
	s = np.zeros((n,k-1))
	for i in range(0,k-1):
		b[i] = i
	for t in range(0,n):
		for l in range(0,k-1):
			if (y[t] <= l):
				s[t][l] = -1
			else:
				s[t][l] = 1

	for it in range(0,L):
		for t in range(0,n):
			E = np.zeros(k-1)
			for l in range(0,k-1):
				if ( (s[t][l]*( np.dot(theta,X[t]) - b[l])) <= 0):
					E[l] = l
			#print(E)
			if(sum(E) > 0):
				sumval = 0
				for m in range(0,k-1):
					if(E[m] > 0):
						sumval += s[t][int(E[m])]
				for n in range(0,d):
					theta[n] +=  sumval*X[t][n]
				for m in range(0,k-1):
					if(E[m] > 0):
						b[int(E[m])] -= s[t][int(E[m])]
	return theta,b
