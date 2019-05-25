import numpy as np
import matplotlib.pyplot as plt

X=np.random.rand(100,1)*10+1
X_=np.random.randint(-100,100,(100,1))*0.1+2*X
X=np.append(X,X_,axis=1)

Y=np.array([0]*len(X)).reshape(-1,1)
for i in range(len(X)):
    if X[i][1]>=2*X[i][0]:
        Y[i]=1
        plt.scatter(X[i,0], X[i,1], c='r')
    else:
        Y[i]=0
        plt.scatter(X[i,0],X[i,1], c='b')
        
X_=np.array([1]*len(X)).reshape(-1,1)
X=np.append(X,X_,axis=1)

def sigmoid(X):
    return 1/(1+np.exp(-X))

def sigmoid_derv(X):
    return sigmoid(X)*(1-sigmoid(X))

l_rate=0.05
epochs=10000

h_nodes=10
wh=np.random.rand(X.shape[1],h_nodes)
wo=np.random.rand(h_nodes,1)


for i in range(epochs):
    zh=np.dot(X,wh)
    ah=sigmoid(zh)
    
    zo=np.dot(ah,wo)
    ao=sigmoid(zo)
    
    error=ao-Y
    error_out=np.sum(1/2*np.power(error,2))
    print(error_out)
    
    zo_derv=sigmoid_derv(zo)
    delta=error*zo_derv
    dwo=np.dot(ah.T,delta)
    
    zh_derv=sigmoid_derv(zh)
    temp=np.dot(delta,wo.T)
    dwh=np.dot(X.T,zh_derv*temp)
    
    wh=wh-l_rate*dwh
    wo=wo-l_rate*dwo
    
    
    

