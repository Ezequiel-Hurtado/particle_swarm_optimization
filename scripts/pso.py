import penalty as pnlt;
import updates as upt;
import functions as fct;

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from autograd import grad



def pso_2d_static(function,penalty = None,  w = 0.7 , c1 = 2 , c2 = 2, N = 1, s = 100, max_iter = 100, ub = 5.12, graphs = 'Oui'): 

    X =  -ub + 2*np.random.rand(s,N)*ub
    X_zero = X.copy()
    v = np.empty(shape =[s,N])
    pb = X.copy()
    gb = X[0]
    iter = 1

    iter_table = pd.DataFrame(columns  =['Iteration','GB', 'F(GB)'] )

    while iter < max_iter: 
        v = upt.velocity_update(X,w,v,c1,c2,pb,gb)
        X = upt.position_update(X,v)

        if penalty is None : 
            X, v =  X.copy(), v.copy()
        elif penalty == 'abc': 
            X,v = pnlt.abc(X,N,v,ub)
        elif penalty == 'reset': 
            X, v = pnlt.reset(X,N,ub), v.copy()
        
        pb = upt.pb_update(X,pb,N, function)
        gb = upt.gb_update(X,pb,gb,function, N)
        
        row = {'Iteration': iter , 'GB': gb, 'F(GB)': function(gb,N)}
        row_df = pd.DataFrame([row])
        iter_table = pd.concat([iter_table, row_df], ignore_index=True)
        
        iter += 1

    X_zero_img =np.empty([s,1])
    X_img =np.empty([s,1])

    for i in range(len(X_zero)): 
        X_zero_img[i] = function(X_zero[i], N)
        X_img[i] = function(X[i], N)

    if graphs == 'Oui':
        if N  == 2: 
            fig = plt.figure(figsize = (10,10))
            plt.subplot(1, 2, 1)
            plt.scatter(X_zero[:,0], X_zero[:,1])
            plt.title('Debut')
            plt.ylabel('Values on X1')
            plt.xlabel('Values on X2')


            plt.subplot(1, 2, 2)
            plt.scatter(X[:,0], X[:,1])
            plt.title('Fin')
            plt.xlabel('Values on X1')
            plt.ylabel('Values on X2')

            plt.show()
        elif N == 3 : 
            fig = plt.figure(figsize = (16,16))
            ax1 = fig.add_subplot(121,projection='3d')
            ax1.scatter(xs = X_zero[:,0], ys = X_zero[:,2], zs= X_zero[:,1])
            ax1.set_xlabel('Values on X1')
            ax1.set_ylabel('Values on X3')
            ax1.set_zlabel('Values on X2')

            ax2 = fig.add_subplot(122,projection='3d')
            ax2.scatter(xs = X[:,0], ys= X[:,2], zs= X[:,1])
            ax2.set_xlabel('Values on X1')
            ax2.set_ylabel('Values on X3')
            ax2.set_zlabel('Values on X2')

            plt.tight_layout()
            plt.show()
        elif N ==1 : 
            print(f"Is it not interesting to plot only X1")
        else :
            print(f"Not possible to make a graph.\n GB : {gb} and image : {function(gb,N)}")
        return  gb, function(gb,N), iter_table
    elif graphs =='Non':
        return  gb, function(gb,N), iter_table

def pso_2d_dynamic(function, penalty = None, N = 1, s = 100, max_iter = 100, ub = 5.12, graph = 'Oui'): 

    X =  -ub + 2*np.random.rand(s,N)*ub
    X_zero = X.copy()
    v = np.empty(shape =[s,N])
    pb = X.copy()
    gb = X[0]
    iter = 1

    iter_table = pd.DataFrame(columns  =['Iteration','GB', 'F(GB)'] )


    while iter < max_iter: 
        w = 0.9 - ((0.9-0.4)/max_iter)*iter
        c1 = 2 - ((iter)*(2 - 0.1))/max_iter
        c2 = 0.1 + ((iter)*(2 - 0.1))/max_iter
        v = upt.velocity_update(X,w,v,c1,c2,pb,gb)
        X = upt.position_update(X,v)

        if penalty is None : 
            X, v =  X.copy(), v.copy()
        elif penalty == 'abc': 
            X,v = pnlt.abc(X,N,v,ub)
        elif penalty == 'reset': 
            X, v = pnlt.reset(X,N,ub), v.copy()

        X = pnlt.reset(X,N, ub)
        pb = upt.pb_update(X,pb,N, function)
        gb = upt.gb_update(X,pb,gb,function, N)
        
        row = {'Iteration': iter , 'GB': gb, 'F(GB)': function(gb,N)}
        row_df = pd.DataFrame([row])
        iter_table = pd.concat([iter_table, row_df], ignore_index=True)
        

        iter += 1

    X_zero_img =np.empty([s,1])
    X_img =np.empty([s,1])

    for i in range(len(X_zero)): 
        X_zero_img[i] = function(X_zero[i], N)
        X_img[i] = function(X[i], N)

    if graph == 'Oui':
        if N  == 2 : 
            plt.subplot(1, 2, 1)
            plt.scatter(X_zero[:,0], X_zero[:,1])
            plt.title('Debut')
            plt.ylabel('Values on X2')
            plt.xlabel('Values on X1')


            plt.subplot(1, 2, 2)
            plt.scatter(X[:,0], X[:,1])
            plt.title('Fin')
            plt.xlabel('Values on X')
            plt.ylabel('Values on Y')

            plt.show()
        elif N == 3 : 
            fig = plt.figure(figsize = (16,16))
            ax1 = fig.add_subplot(121,projection='3d')
            ax1.scatter(xs = X_zero[:,0], ys = X_zero[:,2], zs= X_zero[:,1])
            ax1.set_xlabel('X1 label')
            ax1.set_ylabel('X3 label')
            ax1.set_zlabel('X2 label')

            ax2 = fig.add_subplot(122,projection='3d')
            ax2.scatter(xs = X[:,0], ys= X[:,2], zs= X[:,1])
            ax2.set_xlabel('X1 label')
            ax2.set_ylabel('X3 label')
            ax2.set_zlabel('X2 label')

            plt.tight_layout()
            plt.show()
        elif N ==1 : 
            print(f"Is it not interesting to plot only X1")
        else :
            print(f"Not possible to make a graph.\n GB : {gb} and image : {function(gb,N)}")

        return gb, function(gb,N), iter_table
    elif graph =='Non':
        return  gb, function(gb,N), iter_table


    