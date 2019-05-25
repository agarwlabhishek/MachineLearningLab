import numpy as np
import matplotlib.pyplot as plt

X=np.random.rand(100,2)
Y=2*X[:,0:1]+3*X[:,1:2]-2.5
labels=[]
for i in range(len(X)):
    if Y[i]>0:
        labels.append(1)
        plt.scatter(X[i][0],X[i][1],c='g')
    else:
        labels.append(0)
        plt.scatter(X[i][0],X[i][1],c='r')

labels=np.array(labels).reshape(-1,1)
X_=np.array([1]*len(X)).reshape(-1,1)
X=np.append(X,X_,axis=1)

w=np.zeros(X.shape[1])
epochs=100

Y_pred=np.zeros(len(X))
for i in range(epochs):
    for j in range(len(X)):
        f=np.dot(w,X[j])
        if f>=0:
            Y_pred[j]=1
        else:
            Y_pred[j]=0
        w=w+(labels[j]-Y_pred[j])*X[j]
        
    Y_pred=Y_pred.reshape(-1,1)    
    error=np.sum(np.power((labels-Y_pred),2))
    print(error)
