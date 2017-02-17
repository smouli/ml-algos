#! /usr/bin/env python
import numpy as np
import sys
import matplotlib.pyplot as plt
import math as mt
import numpy.linalg as nla

def createlinregdata(numpts,dim):
	n = numpts
	d = dim
	w = 2*np.random.rand(d,1)-1
	w = w/nla.norm(w)
	X = np.random.rand(n,d)
	y = np.matmul(X,w) + 0.25*np.random.rand(n,1)
	return X,y
	
numpts = int(sys.argv[1])
dim = int(sys.argv[2])
createlinregdata(numpts,dim)