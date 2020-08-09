# Numerical solutions to ordinary differential equations (ODEs)

Solve initial value problem (IVP) y'(t)=f(t, y(t)) with initial value y(t=0)=y0

## Runge-Kutta methods
All methods presented here are Runge-Kutta methods.

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

## RK 4
k1 = f(t_i, y_i)
k2 = f(t_i + h/2, y_i + h/2*k1)
k3 = f(t_i + h/2, y_i + h/2*k2)
k4 = f(t_i + h, y_i + h*k3)

y_(i+1) = y_i + h/6 * (k1 + 2*k2 + 2*k3 + k4)



