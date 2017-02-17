#! /usr/bin/env python
import numpy as np
from createseprankdata import *
from prank import *
from rankpred import *

itr = int(sys.argv[1])
numpts = int(sys.argv[2])
dim = int(sys.argv[3])
numlbls = int(sys.argv[4])
print numlbls
trainset,lbls = createseprankdata(numpts,dim,numlbls)
theta,b = prank(itr,numlbls,trainset,lbls)
Xtest, ytest = createseprankdata(int(numpts/10),dim,numlbls)
for i in range(0,len(Xtest)):
	label = rankpred(numlbls,theta,b,Xtest[i])
	print("Actual label %s, Predicted label %s" % (int(ytest[i]),label)) 

'''test = np.random.rand(2,1)
label = rankpred(numlbls,theta,b,test)
print("The label for point %s is %s" % (test,label))'''