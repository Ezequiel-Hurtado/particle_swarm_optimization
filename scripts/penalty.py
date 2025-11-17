import numpy as np 

def reset(X,N,ub): 
    for i in range(len(X)): 
        for j in range(N): 
            if abs(X[i,j]) > ub : 
                X[i,j] = -ub +2*np.random.rand()*ub
    return X

def abc(X ,N  ,v , ub ): 
    for i in range(len(X)): 
        for j in range(N): 
            if X[i,j] > ub :
                X[i,j] = ub
                v[i,j] = 0 
            elif X[i,j] < -ub:
                X[i,j] = -ub
                v[i,j] = 0 
    return X, v 