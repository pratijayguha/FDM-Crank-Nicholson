from pprint import pprint
from copy import deepcopy

def nested_sum(L):
    total = 0  # don't use `sum` as a variable name
    for i in L:
        if isinstance(i, list):  # checks if `i` is a list
            total += nested_sum(i)
        else:
            total += i
    return total

# Set variables
del_t = 0.001 # Timestep
del_x = 0.01 # Length between two nodes in x axis
del_y = 0.01 # Length between two nodes in y axis
alpha = 0.1 # Constant from question
x = 1 # Length in X axis
y = 1 # Length in Y axis
iterations = 500 # Define number of iterations

# Number of points along each side
n_x = int(x / del_x)
n_y = int(y / del_y)

# Initialise Domain
row = [0.0] * n_x # Create a row of zeroes
u = []
for i in range(n_y): # Create a column if rows
	u.append(row.copy())

# Set Boundary Conditions
for i in range(n_x):
	u[0][i] = 1.
for j in range(n_y):
	u[j][n_x-1] = 1.

u_nt = deepcopy(u) # Domain conatining values of u wrt n+1 timestep

# Iterating
for z in range(iterations):
	for i in range(1,n_x-1):
		for j in range(1,n_y-1):
			u_nt[j][i] = (u[j][i]*((1/del_t) - (alpha/del_x**2) - (alpha/del_y**2)) + ((alpha / (2 * del_x**2)) * (u[j+1][i] + u[j-1][i] + u_nt[j+1][i] + u_nt[j-1][i])) + ((alpha / (2 * del_y**2)) * (u[j][i+1] + u[j][i-1] + u_nt[j][i+1] + u_nt[j][i-1]))) / (1/del_t + alpha * (1/del_x**2 + 1/del_y**2))
	residual = (nested_sum(u_nt) - nested_sum(u))**2 / nested_sum(u)**2
	print(residual)
	u = deepcopy(u_nt)

pprint(u)
