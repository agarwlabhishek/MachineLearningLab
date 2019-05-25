# -*- coding: utf-8 -*-
"""
Created on Tue May  7 08:03:45 2019

@author: abhis
"""
import numpy as np
X=np.random.rand(100,1)*10+1
X_=np.random.randint(-100,100,(100,1))*0.03
Y=3*X+5+X_

n=len(X)

mean_X=np.mean(X)
mean_Y=np.mean(Y)

SS_XY=np.sum(X*Y)-n*mean_X*mean_Y
SS_XX=np.sum(X*X)-n*mean_X*mean_X

a=SS_XY/SS_XX
b=mean_Y-a*mean_X

