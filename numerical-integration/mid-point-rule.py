### MID-POINT RULE ###

import numpy as np

def mid_point_rule_simple(f, a, b):
    '''
    Inputs:
        f:  integrand
        a:  left interval endpoint
        b:  right interval endpoint

    Outputs:
        Approximated integral.
    '''

    Q = (b-a) * f((a+b)/2)

    return Q



def mid_point_rule_composite(f, a, b, m):
    '''
    Inputs:
        f:  integrand
        a:  left interval endpoint
        b:  right interval endpoint
        m:  number of intervals

    Outputs:
        Approximated integral.
    '''

    x = np.linspace(a, b, m+1)
    h = (b-a)/m

    composite_quadrature = 0

    for i in range(1, m+1):
        composite_quadrature += h * f((x[i-1] + x[i])/2)
    
    return composite_quadrature


f = lambda x: x**2 + 2*x
a = 0
b = 1
m = 4

result1 = mid_point_rule_simple(f, a, b)
result2 = mid_point_rule_composite(f, a, b, m)

print(result1)
print(result2)
