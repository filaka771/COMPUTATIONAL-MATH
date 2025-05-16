import math
import numpy as np
import matplotlib.pyplot as plt

def function(x):
    return math.sin(x) * math.cos(x)

def rectangle_integrate(b_seg_int, e_seg_int, step_size):
    integral_sum = 0.0
    num_rectangles = int((e_seg_int - b_seg_int) / step_size)
    
    for i in range(num_rectangles):
        # Evaluate at left endpoint of each subinterval
        x = b_seg_int + i * step_size
        integral_sum += function(x) * step_size
        
        return integral_sum

def calculate_convergence(reference_value, b_seg_int, e_seg_int, initial_step):
    error_data = np.empty((20, 2))  # Columns: [log(step_size), log(error)]
    
    for i in range(19):
        current_step = initial_step / (2 * (i + 1))
        numerical_result = rectangle_integrate(b_seg_int, e_seg_int, current_step)
        
        error_data[i, 0] = math.log(current_step)
        error_data[i, 1] = math.log(abs(reference_value - numerical_result))
        
    # Linear regression to estimate convergence order
    slope, intercept = np.polyfit(error_data[:, 0], error_data[:, 1], 1)
    return error_data, round(slope)

def plot_error_convergence(error_data):
    plt.scatter(error_data[:, 0], error_data[:, 1])
    plt.xlabel('log of step size)')
    plt.ylabel('log of error)')
    plt.title('Error')
    plt.grid(True)
    plt.show()

def main():
    b_seg_int = float(input("Enter upper bound: "))  
    e_seg_int = float(input("Enter upper bound : "))  
    initial_step = float(input("Step size: "))
    
    # Reference value for sin(x)*cos(x) from 0 to 10
    reference_value = 0.147979  
    
    error_data, convergence_order = calculate_convergence(
        reference_value, b_seg_int, e_seg_int, initial_step)
    
    print(f"\nConvergence order: {convergence_order}")
    
    plot_error_convergence(error_data)
    plt.scatter(error_data[:, 0], error_data[:, 1])
    plt.xlabel('log(step size)')
    plt.ylabel('log(error)')
    plt.title('Error')
    plt.grid(True)
    plt.show()

main()
