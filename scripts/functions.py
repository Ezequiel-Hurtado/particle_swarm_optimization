import numpy as np 

def sphere(X,N): 
    y = np.sum(np.square(x -1) for x in X) - 4
    return y

def rastrigin(X,N):
    y = 10*N + np.sum(np.square(x) - 10*np.cos(2*np.pi*x) for x in X)
    return y 

def easom(X, N = 2): 
    '''
    args : 
        X  : Values that the funciton will take. 
        N = 2 : Function is only defined in the second dimension. 
    '''
    X1 = X[0]
    X2 = X[1]
    y = -np.cos(X1)*np.cos(X2)*np.exp(-(np.square(X1-np.pi)+np.square(X2-np.pi)))
	
    return y

def ackley(X,N, a = 20, b = 0.2, c = 2*np.pi): 
  
  sum1 = np.sum(np.square(x) for x in X)
  sum2 = np.sum(np.cos(c*x) for x in X)

  term1 = -a * np.exp(-b*np.sqrt(sum1/N))
  term2 = -np.exp(sum2/N)

  y  = term1 + term2 + a + np.exp(1)
  return y 

def rosenbrock(X,N): 
    '''
    args:
        X  : Values that the funciton will take. 
        N = 2 : Function is only defined from the second dimension and beyond. 
    '''
    somme = 0
    for i in range(len(X)-1):
        Xi = X[i]  
        Xi_next =  X[i+1]  
        new = 100*np.square(Xi_next-np.square(Xi)) + np.square(Xi-1)
        somme = somme + new  
    y = somme 
    return y 

def absolute_value(X,N): 
     y = np.sum(np.abs(x) for x in X)
     return y