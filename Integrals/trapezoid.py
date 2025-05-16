import math

def function(x):
    return math.sin(x) * math.cos(x)

def integrate(b_seg_int, e_seg_int, step_size):
    integral_sum = 0.0
    num_intervals = int((e_seg_int - b_seg_int) / step_size)
    
    for i in range(num_intervals):
        left_point = b_seg_int + i * step_size
        right_point = left_point + step_size
        
        integral_sum += (function(left_point) + function(right_point)) / 2 * step_size
        
        exact_solution = -0.5 * (math.cos(e_seg_int)**2 - math.cos(b_seg_int)**2)
        absolute_error = abs(exact_solution - integral_sum)
        
        return integral_sum, absolute_error

def main():
    b_seg_int = float(input("Enter lower bound: "))
    e_seg_int = float(input("Enter upper bound: "))
    step_size = float(input("Enter step size: "))
    
    result, error = integrate(b_seg_int, e_seg_int, step_size)
    
    print(f"\nNumerical result: {result:.8f}")
    print(f"Analitical solution: {-0.5 * (math.cos(e_seg_int)**2 - math.cos(b_seg_int)**2)}")
    print(f"Error: {error:}")

main()
