import numpy as np
import matplotlib.pyplot as plot
import sys

def make_grid_with_specified_step(x_min, empty_table, step, n):
    for i in range(n):
        empty_table[i, 0] = x_min + i*step

    return empty_table


def apply_in_range(function, grid, n):    
    for i in range(0, n):
        grid[i, 1] = function(grid[i, 0])  

    return grid


def derivative(grid_of_derivative, grid, x_min, x_max, n):
    for i in range(1, n - 2):
        grid_of_derivative[i, 0] = grid[i, 0]
        grid_of_derivative[i, 1] = (grid[i+1, 1] - grid[i-1, 1]) / (grid[i+1, 0] - grid[i-1, 0])
    grid_of_derivative[  0, 0] = grid[0, 0]
    grid_of_derivative[n-1, 0] = grid[n-1, 0]
    grid_of_derivative[  0, 1] = (grid[  1, 1] - grid[  0, 1]) / (grid[  1, 0] - grid[  0, 0])
    grid_of_derivative[n-1, 1] = (grid[n-1, 1] - grid[n-2, 1]) / (grid[n-1, 0] - grid[n-2, 0])

    return grid_of_derivative


def build_plot(x_min, x_max, step):
    n = round((x_max - x_min) / step) + 1
    empty_table = np.empty([n, 2])
    grid_of_derivative = np.empty([n, 2])
    grid = make_grid_with_specified_step(x_min, empty_table, step, n)
    grid = apply_in_range(np.cos, grid, n)
    grid_of_derivative = derivative(grid_of_derivative, grid, x_min, x_max, n)
   # print("derivative")
    derivative_plot = plot.scatter(grid_of_derivative[:, 0], grid_of_derivative[:, 1])
    plot.show()
    return grid_of_derivative
#---------------------------------------------------------------------------------------------
    # Calculate_second_derivative
def second_derivative( x_min, x_max, step, grid_of_derivative):
    n = round((x_max - x_min) / step) + 1
    print(grid_of_derivative[0, 1])
    grid_of_second_derivative = np.empty([n, 2])
    for i in range(0, n-2):
        grid_of_second_derivative[i, 0] = i * step
        grid_of_second_derivative[i, 1] = (grid_of_derivative[i, 1] - grid_of_derivative[i-1, 1]) / (2* step) 
    grid_of_second_derivative[n-1, 0] = x_max
    grid_of_second_derivative[n-1, 1] = (grid_of_derivative[n-1, 1] - grid_of_derivative[n-2, 1]) / step
    plot.scatter(grid_of_second_derivative[1:n-2, 0], grid_of_second_derivative[1:n-2, 1])
    print("second_derivative")
    plot.show()


#---------------------------------------------------------------------------------------------
def main():
    np.set_printoptions(threshold=sys.maxsize)
    
    x_min = float(input("Begining of segment of differentiation: "))
    x_max = float(input("End of segment of differentiation: "))

    step  = float(input("Step of differentiation: "))
    #build_plot(x_min, x_max, step)
    grid_of_derivative = build_plot(x_min, x_max, step)
    second_derivative(x_min, x_max, step, grid_of_derivative)
if __name__ == '__main__':
    main()


