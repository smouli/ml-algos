#! /usr/bin/env python
import numpy as np
from kerperceptron import *

def kerpred(alpha,X,y,x):
	testval = 0
	n = len(X)
	for i in range(0,n):
		testval += alpha[i]*y[i]*kernel(X[i],x)
	if(testval>0):
		label = 1
	else:
		label = -1
	return label