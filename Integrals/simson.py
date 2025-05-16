import math
import numpy as np
import matplotlib.pyplot as plt  # Uncommented since you're using it for error analysis

def function(x):
    return math.sin(x) * math.cos(x)

def simpsons_integrate(b_seg_int, e_seg_int, step_size):
    integral_sum = 0.0
    num_intervals = int((e_seg_int - b_seg_int) / step_size)
    
    for i in range(num_intervals):
        left_point = b_seg_int + i * step_size
        midpoint = b_seg_int + (2*i + 1) * step_size / 2
        right_point = b_seg_int + (i + 1) * step_size
        
        # Simpson's rule formula
        integral_sum += (step_size / 6) * (
            function(left_point) + 
            4 * function(midpoint) + 
            function(right_point)
        )
    
    return integral_sum

def error_analysis(reference_value, b_seg_int, e_seg_int, initial_step):
    error_table = np.empty((20, 2))  
    
    for i in range(19):
        current_step = initial_step / (2 * (i + 1))
        numerical_result = simpsons_integrate(b_seg_int, e_seg_int, current_step)
        
        error_table[i, 0] = math.log(current_step)  
        error_table[i, 1] = math.log(abs(reference_value - numerical_result))  
    
    slope, intercept = np.polyfit(error_table[:, 0], error_table[:, 1], 1)
    return error_table, round(slope)

def main():
    b_seg_int = float(input("Enter lower bound (a): "))  
    e_seg_int = float(input("Enter upper bound (b): "))  
    step_size = float(input("Enter initial step size: "))
    
    reference_value = 0.147979484546652
    
    error_data, convergence_order = calculate_error_analysis(
        reference_value, b_seg_int, e_seg_int, step_size)
    
    integral_result = simpsons_integrate(b_seg_int, e_seg_int, step_size)
    
    print(f"\nIntegral result: {integral_result:.12f}")
    print(f"Reference value: {reference_value:.12f}")
    print(f"Estimated convergence order: {convergence_order}")

main()
