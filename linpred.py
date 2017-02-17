#! /usr/bin/env python
import numpy as np

def linpred(theta,x):
	label = 0
	val = np.dot(theta,x)
	if(val > 0):
		label = 1
	else:
		label = -1
	return label