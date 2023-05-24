# FDM Crank-Nicholson Code Readme

This readme provides an overview and explanation of the FDM (Finite Difference Method) Crank-Nicholson code provided.

## Introduction

The code implements the Crank-Nicholson method to solve a heat conduction problem in a 2D domain. It discretizes the domain using a grid and iteratively calculates the temperature distribution at each grid point over a given number of iterations.

## Code Explanation

Let's go through the code and explain each part:

### Function: nested_sum(L)

- This function calculates the sum of nested lists recursively.
- It takes a nested list `L` as input and returns the sum of all its elements.

### Variable Initialization

- `del_t`: Timestep
- `del_x`: Length between two nodes in the x-axis
- `del_y`: Length between two nodes in the y-axis
- `alpha`: Constant from the question
- `x`: Length in the x-axis
- `y`: Length in the y-axis
- `iterations`: Number of iterations to perform

### Grid Initialization

- `n_x` and `n_y` are calculated based on the given domain dimensions and grid spacing.
- The `u` list represents the domain, where each element `u[j][i]` corresponds to the temperature at grid point `(i, j)`.
- The grid is initialized with zeros, and the boundary conditions are set (first row and last column are set to 1).

### Iterative Calculation

- The code enters a loop that performs the specified number of iterations (`iterations` variable).
- Within each iteration, the temperature at each interior grid point is calculated based on the Crank-Nicholson method.
- The calculated temperatures are stored in `u_nt`, which represents the domain values at the (n+1)th timestep.
- Residual calculation is performed to assess convergence and is printed for each iteration.
- Finally, the `u` domain is updated with the values from `u_nt` using deepcopy.

### Output

- The final temperature distribution in the domain is printed using `pprint(u)`.

## Usage

- Make sure to have the required dependencies installed, such as `pprint` and `deepcopy`.
- Set the variables according to your problem and desired parameters.
- Run the code, and it will output the residual for each iteration and the final temperature distribution in the domain.

## Notes

- This code assumes a heat conduction problem in a 2D domain with given boundary conditions.
- Adjustments may be needed based on your specific problem requirements.

Please ensure you provide the necessary input and adapt the code to your specific problem before running it.
