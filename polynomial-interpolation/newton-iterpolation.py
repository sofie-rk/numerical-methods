### NEWTON INTERPOLATION ###

import numpy as np
import matplotlib.pyplot as plt


def divided_differences(xdata, ydata):
    
    '''
    The divided differences table is created based
    on the interpolation-data (xdata, ydata)

    This table corresponds to what you normally would make by hand 
    (make documentation of this)



    Inputs:
        xdata: array of nodes x_i, interpolation data
        ydata: array of correspond y_i, interpolation data

    Return:
        Coefficients needed for the interpolation polynomial
        The first row of the table contains the coefficients
    '''

    m = len(xdata)  # Number of evaulation points

    F = np.zeros((m,m)) # square matrix to hold the divided differences

    F[:,0] = ydata  # First column is ydata

    for j in range(m):
        # Go through all of the evaluation points

        for i in range(m-j-1):

            F[i,j+1] = (F[i+1,j]-F[i,j]) / (xdata[i+j+1]-xdata[i])

    
    return F[0]


def newton_interpolation(coeff, xdata, xvalues):
    '''
    Inputs:
        coeff:      coefficients from the divided differences
        xdata:      array of nodes x_i, interpolation data
        xvalues:    array with values in which polynomial is evaluated
    
    Outputs:
        An array with the interpolation polynomial's y-values.
    '''

    n = len(coeff) 

    poly_array = coeff[0] 
    
    for k in range(1, n+1):
        poly_array = coeff[n-k] + (xvalues - xdata[n-k])*poly_array

    return poly_array


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

# Get coefficients (table of divided differences)
F = divided_differences(xdata, ydata)

# Get y-values for the interpolation polynomial, evaluated in x-values
y_interpolation_polynomial = newton_interpolation(F, xdata, x_values_to_be_evaluated)

# Plot the interpolation polynomial
# From the plot, you can see that the interpolation polynom goes through the interpolation points
plt.plot(x_values_to_be_evaluated, y_interpolation_polynomial, label="Interpolation polynomial", color="red")

# Display the plot + some extra spice
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()