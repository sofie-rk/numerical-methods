### FIX POINT ITERATION ###

# Solves equations on the form x = g(x)

# f(x)=0 with a root r, rewrite f(x) such that x = g(x)

# Method: x_(n+1) = g(x_n), for n=0,1,2,3...

import numpy as np
import matplotlib.pyplot as plt


def fixpoint(g, x0, max_iter=25, tol=10e-4):
    '''
    
    Solve x=g(x) by fix point iterations
    
    Iterations are terminated when either the error is less
    than the given tolerance or if maximum number of
    iterations is reached.

    -----------------------------------------------------
    Inputs:
        g:          Function g(x)
        x0:         Initial value
        tol:        Tolerance/accurancy
        max_iter:   Maximum number of iterations  
    -----------------------------------------------------
    Output:
        Printing whether solution is found.
        If solution is found, the tolerance, number of 
        iterations and the solution is printed.
        Return: the solution r which gives r=g(r).

    -----------------------------------------------------
    '''

    x = x0
    n = 1
    err = tol + 1

    while (err > tol and n<max_iter):
        x_n = x # store old x
        x = g(x)    # fix point iteration
        err = abs(x-x_n)
        n += 1

    if n == max_iter:
        print("Reached maximmum number of iterations, no solution found within given tolerance.")
        return None
    
    else:
        print("Found solution after", n, "number of iterations.")
        print("The solution is x =", x)
        return x

    return None





def fixpoint_with_display(g, x0, max_iter=20, tol=10e-4):
    '''
    
    Solve x=g(x) by fix point iterations
    
    Iterations are terminated when either the error is less
    than the given tolerance or if maximum number of
    iterations is reached.

    Will display x_(n+1), g(x_n) and error for each iteration
    Will create a plot with x_n, n=0,1,2,...

    -----------------------------------------------------
    Inputs:
        g:          Function g(x)
        x0:         Initial value
        tol:        Tolerance/accurancy
        max_iter:   Maximum number of iterations  
    -----------------------------------------------------
    Output:
        Printing whether solution is found.
        If solution is found, the tolerance, number of 
        iterations and the solution is printed.
        Return: the solution r which gives r=g(r).

    -----------------------------------------------------
    '''

    x_list = np.linspace(x0-x0/2, x0+x0/2, 101)
    plt.plot(x_list, g(x_list), label="g(x)")
    plt.plot(x_list, x_list, label="x")
    plt.plot(x0, g(x0), "bo", label="x0", color="green")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    

    x = x0
    n = 1
    err = tol + 1

    print("--------------------------------------------------------------------------------")
    print("   Iteration          x              g            Error     ")
    print("--------------------------------------------------------------------------------")

    while (err > tol and n<max_iter):
        x_n = x # store old x
        x = g(x)    # fix point iteration
        plt.plot(x, g(x), "bo", color="red")
        err = abs(x-x_n)
        print('{0:8} {1:15.5f}  {2:15.5f} {3:15.5f} '.format(n, x_n, g(x), err) )
        n += 1
    
    print("--------------------------------------------------------------------------------")

    if n == max_iter:
        print("Reached maximmum number of iterations, no solution found within given tolerance.")
        return None
    
    else:
        print("Found solution after", n, "iterations.")
        print("The solution is x =", x)
        plt.show()
        return x

    return None


g = lambda x: np.cos(x)
x0 = 1 

result_simple = fixpoint(g, x0)

result_with_display = fixpoint_with_display(g, x0)



