# BISECTION METHOD
#
# Other names: Interval Halving Method, Binary Search Method
# 
# Finds a solution for f(x)=0

# Given an interval [x_lower, x_upper], check if f has a root in the interval,
# divide it in two, check in which of the two halves the root is.
# Divide intervals in two until a root is located with sufficient accurancy.

# Starting by guessing a interval [x_lower x_upper] where the solution might be

# If f(x_lower)*f(x_mid) <= 0, the root is located between x_lower and x_mid
# If f(x_upper)*f(x_mid) <= 0, the root is located between x_mid and x_upper

import numpy as np
import matplotlib.pyplot as plt

def bisection_method(f, x_lower, x_upper, N=25, tol=10e-4):
    '''
    Approximate solution for f(x)=0 on interval [x_lower, x_upper] by bisection method.

    f: function, f(x)=0
    x_lower: lower interval boundary
    x_upper: upper interval boundary
    N: maximum number of iterations (optional)
    tol: tolerance (optional)

    example:
    f = lambda x: cos(x) - x 
    bisection(f, 0, 3)
    '''

    if x_upper <= x_lower:
        print("Upper interval limit is not larger than lower interval limit")
        return None

    if f(x_upper)*f(x_lower) >= 0:
        print("f(x_upper)*f(x_lower)>=0, bisection method will fail")
        return None

    if N<=0:
        print("Number of iterations must be a positive integer")
        return None

    if tol<=0:
        print("Tolerance must be positive integer")
        return None

    n = 1

    x_lower_n = x_lower
    x_upper_n = x_upper

    while (n<=N):
        x_mid = (x_lower_n + x_upper_n) / 2
        f_mid = f(x_mid)
       
        if abs(f_mid) < tol:
            print("Found a solution with the given tolerance (", tol, ") within", n, "iterations.") # (", tol, ") within ", n " number of iterations.")
            print("Solution: x =", x_mid)
            return x_mid
        
        elif f(x_lower_n)*f_mid < 0:
            x_lower_n = x_lower_n
            x_upper_n = x_mid
        
        elif f(x_upper_n)*f_mid < 0:
            x_lower_n = x_mid
            x_upper_n = x_upper_n
        
        else:
            print("Bisection method failed.")
            return None
    
        n += 1
    print("Bisection method failed.")
    return None

f = lambda x: np.cos(x) - x
# bisection_method(f, 0, np.pi/2)


def bisection_method_with_display(f, x_lower, x_upper, N=25, tol=10e-4):

    if x_upper <= x_lower:
        print("Upper interval limit is not larger than lower interval limit")
        return None

    if f(x_upper)*f(x_lower) >= 0:
        print("f(x_upper)*f(x_lower)>=0, bisection method will fail")
        return None

    if N<=0:
        print("Number of iterations must be a positive integer")
        return None

    if tol<=0:
        print("Tolerance must be positive integer")
        return None


    x_list = np.linspace(x_lower, x_upper, 100)
    zero_list = np.zeros(len(x_list))
    y_list = f(x_list)

    plt.plot(x_list, y_list, label="f(x)", color="red")
    plt.plot(x_list, zero_list, color="black")
    plt.plot(x_lower, 0, "bo", label="x lower", color="blue")
    plt.plot(x_upper, 0, "bo", label="x upper", color="blue")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    

    n = 1

    x_lower_n = x_lower
    x_upper_n = x_upper

    print("--------------------------------------")
    print("Iteration        x           f(x)")
    print("--------------------------------------")

    

    while (n<=N):
        x_mid = (x_lower_n + x_upper_n) / 2
        f_mid = f(x_mid)
        plt.plot(x_mid, f_mid, "bo", color="green")

        #print("Iteration: ", n, "x =", x_mid, "")

        print('{0:8} {1:12.5f}  {2:11.5f} '.format(n, x_mid, f_mid) )
       
        if abs(f_mid) < tol:
            print("--------------------------------------")
            print("Found a solution within tolerance", tol, "with", n, "iterations.") # (", tol, ") within ", n " number of iterations.")
            print("Solution: x =", x_mid)
            plt.show()
            return x_mid
        
        elif f(x_lower_n)*f_mid < 0:
            x_lower_n = x_lower_n
            x_upper_n = x_mid
        
        elif f(x_upper_n)*f_mid < 0:
            x_lower_n = x_mid
            x_upper_n = x_upper_n
        
        else:
            print("--------------------------------------")
            print("Bisection method failed.")
            return None
    
        n += 1
    print("Bisection method failed.")
    return None



bisection_method_with_display(f, 0, np.pi/2)