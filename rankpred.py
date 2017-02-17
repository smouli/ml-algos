#! /usr/bin/env python
import numpy as np

def rankpred(numlbls,theta,b,x):
	val =  np.dot(theta,x)
	lenb = len(b)
	if(val<=b[0]):
		return 0
	for i in range(0,lenb-1):
		if(b[i]< val and val <= b[i+1]):
			return i+1
	if(val > b[lenb-1]):
		return lenb
