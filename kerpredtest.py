import sys
import numpy as np
from createsepdata import *
from kerperceptron import *
from kerpred import *

itr = int(sys.argv[1])
numpts = int(sys.argv[2])
dim = int(sys.argv[3])

X, y = createsepdata(numpts,dim,0)
alpha = kerperceptron(itr,X,y)
Xtest, ytest = createsepdata(int(numpts/10),dim,0)
'''for i in range(0,len(Xtest)):
	label = kerpred(alpha,Xtest,ytest,Xtest[i])
	print("Actual label %s, Predicted label %s" % (int(ytest[i]),label)) '''
test = np.random.uniform(-2,2,dim)
label = kerpred(alpha,X,y,test)
print("The label for test point %s is %s" % (test,label))
kerperceptronvisual(X,y,test)