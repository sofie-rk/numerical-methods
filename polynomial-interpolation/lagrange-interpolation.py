### LAGRANGE INTERPOLATION ###

import numpy as np
import matplotlib.pyplot as plt

def cardinal(xdata, xvalues):

    '''
    Inputs:
        xdata:      array with nodes x_i
        xvalues:    array with values in which the cardinal functions are evaluated
    
    Return:
        List with m arrays containing the evaluated xvalues in the cardinal function, l_i(xvalues)
    '''

    m = len(xdata)  # Number of evaluation points 

    l = []          # Array will contain the cardinal functions l_i 

    for i in range(m):
        li = np.ones(len(xvalues)) # Array will contain values for l_i

        for j in range(m):
            
            if i != j:
                li *= (xvalues - xdata[j]) / (xdata[i] - xdata[j])
    
        l.append(li)

    return l


def lagrange(ydata, l):

    '''
    What:
        p_n = sum (y_i * l_i)

    Inputs:
        ydata:  array of the interpolation y-values
        l:      list of the cardinal function values, may be given by cardinal(xdata, x)
    
    Return:
        An array with the interpolation polynomial's y-values.
    '''

    p_n = 0

    for i in range(len(ydata)):
        p_n += ydata[i] * l[i] 

    return p_n



# EXAMPLE

# Known polynomial: f(x) = cos(pi*x/2)
f = lambda x: np.cos(np.pi*x/2)

# Nodes
xdata = [0, 2/3, 1]
ydata = [1, 1/2, 0]

# x-list, grid points for plotting/evaluation
x_values_to_be_evaluated = np.linspace(0, 1, 101)

# Plot known function with the interpolation data (nodes)
plt.plot(x_values_to_be_evaluated, f(x_values_to_be_evaluated), label="f(x)", color="blue")
plt.plot(xdata, ydata, "ok", label="Interpolation data")

# Get values of the cardinal functions evaluated in x_values_to_be_evaluated
l = cardinal(xdata, x_values_to_be_evaluated)

# Get y-values for the interpolation polynomial, evaluated in x_values_to_be_evaluated
y_interpolation_polynomial = lagrange(ydata, l)

# Plot the interpolation polynomial
# From the plot, you can see that the interpolation polynom goes through the interpolation points
plt.plot(x_values_to_be_evaluated, y_interpolation_polynomial, label="Interpolation polynomial", color="red")


# Display the plot + some extra spice
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()



