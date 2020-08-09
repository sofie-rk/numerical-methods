# Numerical solutions to ordinary differential equations (ODEs)

Solve initial value problem (IVP) y'(t)=f(t, y(t)) with initial value y(t=0)=y0

## Euler's method
One step method.
Explicit method.
Degree of exactness: 0.
y_(i+1) = y_i + h*f(t_i, y_i)

## Heun's method
One step method.
More accurate than Euler's method

k1 = f(t_i, y_i)
k2 = f(t_(i+1), y_i + h*f(t_i, y_i)) = f(t_(i+1), y_i + h*k2)
y_(i+1) = y_i + h/2 * (f(t_i, y_i) + f(t_(i+1), y_i + h*f(t_i, y_i))) = y_i + h/2 * (k1 + k2)

