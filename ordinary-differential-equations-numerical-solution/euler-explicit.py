### EULER'S EXPLICIT METHOD ###

import numpy as np
import matplotlib.pyplot as plt

def explicit_euler(y0, t0, T, f, N):
    '''
    Inputs:
        y0:     initial y-value
        t0:     initial t-value
        T:      end t-value
        f:      function f(t, y(t))
        N:   maximum number of steps between t0 and T

    Outputs:
        ts:     array of t-values
        ys:     array of y-values
    '''

    ys = [y0]
    ts = [t0]
    dt = (T - t0) / N

    while ts[-1]<T:
        t, y = ts[-1], ys[-1]
        ys.append(y + dt*f(t,y)) # Euler's method
        ts.append(t + dt) 

    return np.array(ts), np.array(ys)

# Example y'(t) = -y(t)
t0 = 0
T = 1
y0 = 1
N = 32
f = lambda t,y: y
ts, ys_euler = explicit_euler(y0, t0, T, f, N)

# Will compare to the exact solution, y(t) = y0 * exp(-t)
y_exact = lambda t: y0*np.exp(t-t0)
ys_exact = y_exact(ts)

plt.plot(ts, ys_euler, "ro", label="Numerical solution")
plt.plot(ts, ys_exact, label="Exact solution")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

# Example where you can see the effect of N
N_list = [4, 8, 16, 32]
color_list = ["green", "black", "yellow", "red"]
plt.plot(ts, ys_exact, label="Exact solution", color="blue")
for i in range(len(N_list)):
    ts, ys_euler = explicit_euler(y0, t0, T, f, N_list[i])
    description = "N =" + str(N_list[i])
    plt.plot(ts, ys_euler, 'ro', label=description, color=color_list[i])
plt.legend() 
plt.show()




