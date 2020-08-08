# Numerical integration

Numerical integration based on interpolation techniques.

If we want to solve a finite integral f (with boundaries from a to b) but are unable to compute the integral analytically. 

Approximated integral Q = sum(weight * f(x_i))

You can find codes for both simple quadrature rules and composite quadrature rules. 

## Mid-point rule

Q = (b-a) * f((a+b)/2)

weight = (b-a)
x_0 = (a+b)/2


## Trapezoidal rule

Q = (b-a)/2 * (f(a) + f(b))

weights: w_0 = (b-a)/2, w_1 = (b-a)/2
x_0 = a, x_1 = b


## Simpsons rule

Q = (b-a)/6 * (f(a) + 4*f((a+b)/2) + f(b))

w_0 = (b-a)/6   w_1 = 4*(b-a)/6   w_2 = (b-a)/6
x_0 = a     x_1 = (a+b)/2       x_2 = b

