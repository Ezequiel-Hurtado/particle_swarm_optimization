import numpy as np 

def velocity_update(X,w,v,c1,c2,pb,gb): 
    r1 = np.random.rand()
    r2 = np.random.rand()
    v_update = w*v + c1*r1*(pb - X) + c2*r2*(gb - X)
    v = v_update
    return v

def position_update(X, v): 
    X_update = X + v 
    X = X_update
    return X

def pb_update(X,pb, N, function):
    for i in range(len(X)): 
        if function(X[i], N) < function(pb[i], N): 
            pb[i] = X[i]
    return  pb

def gb_update(X,pb, gb, function , N ): 
    for i in range(len(pb)): 
         if function(pb[i], N) < function(gb, N) : 
            gb = pb[i]
    return gb
