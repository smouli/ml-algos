#! /usr/bin/env python
import numpy as np
import math as mt
import numpy.linalg as nla
import sys
from createlinregdata import *
import scipy as sc

def kfoldcv(numfolds,trainset,lbls):
	k = numfolds
	X = trainset
	y = lbls
	n = len(X)
	z = []
	for i in range(0,k):
		S = []
		T = []
		SY = []
		TY = []
		for j in range(0,n):
			if(j < mt.floor((n*i)/k) or j > (mt.floor((n*(i+1))/k) - 1)):
				S.append(X[j])
				SY.append(y[j])
			else:
				T.append(X[j])
				TY.append(y[j])
		theta  = nla.lstsq(S,SY)[0]
		sqerror = 0
		for m in range(0,len(T)):
			sqerror += mt.pow( (TY[m] - np.dot( [ theta[0][0] , theta[1][0]] ,T[m])) , 2)
		sqerror = sqerror/len(T)
		z.append(sqerror)
	return z
		
numfolds = int(sys.argv[1])
numpts = int(sys.argv[2])
dim = int(sys.argv[3])
trainset,lbls = createlinregdata(numpts,dim)
print kfoldcv(numfolds,trainset,lbls)

