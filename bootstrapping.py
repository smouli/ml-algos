#! /usr/bin/env python
import numpy as np
import math as mt
import numpy.linalg as nla
import sys
from createlinregdata import *
import scipy as sc

def bootstrapping(numbootstraps,trainset,lbls):
	B = numbootstraps
	X = trainset
	y = lbls
	n = len(X)
	z = []
	for i in range(0,B):
		u = np.zeros(n)
		S = []
		T = []
		SY = []
		TY = []
		uset = set()
		#print(S)
		for j in range(0,n):
			k = np.random.choice(n)
			u[j] = k
			S.append(X[k])
			SY.append(y[k])
		for m in range(0,n):
			if m not in u:
				T.append(X[m])
				TY.append(y[m])
		#print(S)
		theta  = nla.lstsq(S,SY)[0]
		sqerror = 0
		th = np.reshape(len(theta),1)
		#print(theta)
		#print(th)
		for m in range(0,len(T)):
			sqerror += mt.pow( (TY[m] - np.dot( [ theta[0][0] , theta[1][0]] ,T[m])) , 2)
		sqerror = sqerror/len(T)
		z.append(sqerror)
	return z
		
numbootstraps = int(sys.argv[1])
numpts = int(sys.argv[2])
dim = int(sys.argv[3])
trainset,lbls = createlinregdata(numpts,dim)
print bootstrapping(numbootstraps,trainset,lbls)

