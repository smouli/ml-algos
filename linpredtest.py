import sys
import numpy as np
from createsepdata import *
from linperceptron import *
from linpred import *

itr = int(sys.argv[1])
numpts = int(sys.argv[2])
dim = int(sys.argv[3])

X, y = createsepdata(numpts,dim,0)
theta = linperceptron(itr,X,y)
Xtest, ytest = createsepdata(int(numpts/10),dim,0)
'''for i in range(0,len(Xtest)):
	label = linpred(theta,Xtest[i])
	print("Actual label %s, Predicted label %s" % (int(ytest[i]),label))'''
test = np.random.uniform(-2,2,dim)
label = linpred(theta,test)
print("The label for point %s is %s" % (test,label))
linperceptronvisual(X,y,test,theta)