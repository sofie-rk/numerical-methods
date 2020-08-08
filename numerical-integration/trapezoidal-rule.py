### TRAPEZOIDAL RULE ###

import numpy as np

def trapezoidal_rule_simple(f, a, b):
    '''
    Inputs:
        f:  integrand
        a:  left interval endpoint
        b:  right interval endpoint

    Outputs:
        Approximated integral.
    '''

    Q = (b-a)/2 * (f(a) + f(b))

    return Q


def trapezoidal_rule_composite(f, a, b, m=4):
    '''
    Inputs:
        f:  integrand
        a:  left interval endpoint
        b:  right interval endpoint
        m:  number of intervals

    Outputs:
        Approximated integral.

    Composite trapezoidal rule: every point except f(a) and f(b) 
    are counted twice. This gives a simplified for-loop.

    '''

    h = (b-a) / m

    composite_quadrature = h/2 * (f(a) + f(b))

    for i in range(1, m):
        composite_quadrature += h * f(a + i*h)

    return composite_quadrature

f = lambda x: x**2
a = 5
b = 10
m = 100

result1 = trapezoidal_rule_simple(f, a, b)
result2 = trapezoidal_rule_composite(f, a, b, m)

print(result1)
print(result2)


    