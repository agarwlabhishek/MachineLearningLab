import numpy as np
import matplotlib.pyplot as plt
X=np.random.rand(100,1)*10+1
X_=np.random.randint(-100,100,(100,1))*0.05+2*X
X=np.append(X,X_,axis=1)

Y=np.zeros(len(X)).reshape(-1,1)
for i in range(len(X)):
    if X[i,1]<=2*X[i,0]:
        Y[i]=1
        plt.scatter(X[i,0],X[i,1],c='r')
    else:
        plt.scatter(X[i,0],X[i,1],c='g')

X_=np.array([1]*len(X)).reshape(-1,1)
X=np.append(X,X_,axis=1)

def sigmoid(X):
    return 1/(1+np.exp(-X))

def sigmoid_derv(X):
    return sigmoid(X)*(1-sigmoid(X))

l_rate=0.05
epochs=1000
W=np.random.rand(X.shape[1],1)

for i in range(epochs):
    XW=np.dot(X,W)
    Z=sigmoid(XW)
    
    error=Y-Z
    error_out=np.sum(np.power(error,2))
    print(error_out)
    Z_derv=sigmoid_derv(Z)
    delta=error*Z_derv
    W=W-l_rate*np.dot(X.T,delta)
    


