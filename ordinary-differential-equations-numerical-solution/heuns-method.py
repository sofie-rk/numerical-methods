### HEUN'S METHOD ###

import numpy as np
import matplotlib.pyplot as plt

def heun(y0, t0, T, f, N):
    ts = [t0]
    ys = [y0]
    dt = (T-t0)/N

    while ts[-1]<T:
        t, y = ts[-1], ys[-1]
        k1 = f(t,y)
        k2 = f(t+dt, y+dt*k1)
        
        ys.append(y + dt/2 * (k1 + k2))
        ts.append(t + dt)

    return np.array(ts), np.array(ys)

# Example y'(t) = -y(t)
t0 = 0
T = 1
y0 = 1
N = 4
f = lambda t,y: y
ts, ys_heun = heun(y0, t0, T, f, N)

# Will compare to the exact solution, y(t) = y0 * exp(-t)
y_exact = lambda t: y0*np.exp(t-t0)
ys_exact = y_exact(ts)

plt.plot(ts, ys_heun, "ro", label="Numerical solution")
plt.plot(ts, ys_exact, label="Exact solution")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

# Example where you can see the effect of N
N_list = [4, 8]
color_list = ["green", "red", "yellow", "black"]
plt.plot(ts, ys_exact, label="Exact solution", color="blue")
for i in range(len(N_list)):
    ts, ys_heun = heun(y0, t0, T, f, N_list[i])
    description = "N =" + str(N_list[i])
    plt.plot(ts, ys_heun, 'ro', label=description, color=color_list[i])
plt.legend() 
plt.show()
