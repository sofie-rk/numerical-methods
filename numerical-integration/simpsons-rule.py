### SIMPSONS RULE ###

import numpy as np

def simpsons_simple(f, a, b):
    '''
    Inputs:
        f:  integrand
        a:  left interval endpoint
        b:  right interval endpoint

    Outputs:
        Approximated integral.
    '''

    Q = (b-a)/6 * (f(a) + 4*f((a+b)/2) + f(b))

    return Q


def simpsons_composite(f, a, b, m=4):
    '''
    Inputs:
        f:  integrand
        a:  left interval endpoint
        b:  right interval endpoint
        m:  number of intervals

    Outputs:
        Approximated integral.
    '''
    h = (b-a)/m
    x = np.linspace(a, b, m+1)
    xhalf = np.linspace(a+h/2, b-h/2, m)

    composite_quadrature = h/6 * (f(a) + f(b))
    
    for i in range(1, m):
        composite_quadrature += h/6 * 2 * f(x[i])
    for i in range(m):
        composite_quadrature += h/6 * 4 * f(xhalf[i])
    
    return composite_quadrature

f = lambda x: np.cos(np.pi/2 * x)
a = 0
b = 1
m = 11

result1 = simpsons_simple(f, a, b)
result2 = simpsons_composite(f, a, b, m)
