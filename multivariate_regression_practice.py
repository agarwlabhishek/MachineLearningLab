# -*- coding: utf-8 -*-
"""
Created on Tue May  7 07:40:18 2019

@author: abhis
"""

import numpy as np
import matplotlib.pyplot as plt

X=np.random.rand(100,2)*10+1
X_=np.random.randint(-100,100,(100,1))*0.01
Y=2*X[:,0:1] + 3*X[:,1:2] - 5 + X_

X_=np.array([1]*len(X)).reshape(-1,1)
X=np.append(X,X_,axis=1)

lhs=np.dot(X.T,X)
rhs=np.dot(X.T,Y)
mat=np.append(lhs,rhs,axis=1)

for i in range(len(mat)):
    if mat[i][i]!=0:
        mat[i]=mat[i]/mat[i][i]
    for j in range(len(mat)):
        if j!=i:
            pro=mat[j][i]/mat[i][i]
            for k in range(mat.shape[1]):
                mat[j][k]=mat[j][k]-pro*mat[i][k]
                
print("Weights are:" + str(mat[:,-1]))
