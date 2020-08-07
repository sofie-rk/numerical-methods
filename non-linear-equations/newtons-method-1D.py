### NEWTON'S METHOD ###

# Solves equations on the form f(x)=0

# Method: x_(n+1) = x_n - f(x_n)/f'(x_n) for n=0,1,2,3...

import numpy as np
import matplotlib.pyplot as plt


def newton(f, df, x0, max_iter=25, tol=10e-4):
    '''
    Solves f(x)=0 by Newtons method

    Terminates when either f(x) is less than the tolerance, or when
    maximum number of iterations is reached

    --------------------------------------------------------------
    Input:
        f:          function f
        df:         derivative of function f
        x0:         initial value
        max_iter:   maximum number of iterations
        tol:        tolerance/accuracy
    --------------------------------------------------------------
    Output:
        Prints whether solution is found.
        If solution is found, the solution and the number of 
        iterations is printed.
        Return: the solution r such that f(r)=0
    --------------------------------------------------------------
    
    '''

    x = x0
    n=1
    err = abs(f(x)) 

    while (n<=max_iter and err>tol):
        if (df(x) == 0):
            print("No derivative. No solution is found.")
            return None

        else:
            x = x - f(x)/df(x)
            err = f(x)
            n+=1
    
    if n == max_iter:
        print("Maximum number of iterations (", n, ") is reached, no solution is found.")
        return None

    else:
        print("Found solution after", n, "iterations.")
        print("The solution is x =", x)
        return x

    return None


def newton_with_display(f, df, x0, max_iter=25, tol=10e-4):
    '''
    Solves f(x)=0 by Newtons method

    Terminates when either f(x) is less than the tolerance, or when
    maximum number of iterations is reached

    --------------------------------------------------------------
    Input:
        f:          function f
        df:         derivative of function f
        x0:         initial value
        max_iter:   maximum number of iterations
        tol:        tolerance/accuracy
    --------------------------------------------------------------
    Output:
        Prints whether solution is found.
        If solution is found, the solution and the number of 
        iterations is printed.
        Return: the solution r such that f(r)=0
    --------------------------------------------------------------
    
    '''

    x_list = np.linspace(x0-x0/2, x0+x0/2, 101)
    plt.plot(x_list, f(x_list), label="f(x)")
    plt.plot(x_list, [0 for i in range(len(x_list))], color="black")
    plt.plot(x0, f(x0), "bo", label="x0", color="green")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    

    print("--------------------------------------------------------------------------------")
    print("   Iteration          x            Error     ")
    print("--------------------------------------------------------------------------------")

    x = x0
    n=1
    err = abs(f(x)) 

    while (n<=max_iter and err>tol):
        if (df(x) == 0):
            print("No derivative. No solution is found.")
            return None

        else:
            x = x - f(x)/df(x)
            err = f(x)
            plt.plot(x, f(x), "bo", color="red")
            print('{0:8} {1:15.5f}  {2:15.5f}'.format(n, x, err) )
            n+=1
    
    if n == max_iter:
        print("Maximum number of iterations (", n, ") is reached, no solution is found.")
        return None

    else:
        print("Found solution after", n, "iterations.")
        print("The solution is x =", x)
        plt.show()
        return x

    return None

f = lambda x: x - np.cos(x)
df = lambda x: 1 + np.sin(x)
x0 = 1

result = newton_with_display(f, df, x0)