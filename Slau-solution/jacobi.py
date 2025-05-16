import numpy as np
import math

# Reference solution for verification
reference_solution = np.array([3, 2, 5], dtype=float)

# Coefficient matrix and right-hand side vector
coefficient_matrix = np.array([[10, 1, -1],
                               [1, 10, -1],
                               [-1, 1, 10]], dtype=float)

rhs_vector = np.array([27, 18, 49], dtype=float)

def is_matrix_valid(matrix, vector):
    for row_index in range(len(matrix)):
        if len(matrix[row_index]) != len(vector):
            print('Wrong size')
            return False
        
    for row_index in range(len(matrix)):
        if matrix[row_index][row_index] == 0:
            print('Zero elements on the diagonal')
            return False
    return True

def has_converged(old_solution, new_solution, tolerance=0.0001):
    numerator_sum = 0.0
    denominator_sum = 0.0
    for index in range(len(old_solution)):
        numerator_sum += (new_solution[index] - old_solution[index]) ** 2
        denominator_sum += new_solution[index] ** 2
        
    return math.sqrt(numerator_sum / denominator_sum) < tolerance

def solve_system(matrix, vector):
    if not is_matrix_valid(matrix, vector):
        print('Error in initial data')
        return None
    
    system_size = len(vector)
    current_solution = np.ones(system_size)  # initial value
    
    iteration_count = 0
    max_iterations = 100
    
    while iteration_count < max_iterations:
        previous_solution = current_solution.copy()
        
        for row in range(system_size):
            sum_other_terms = 0.0
            for col in range(system_size):
                if col != row:
                    sum_other_terms += matrix[row][col] * previous_solution[col]
                    current_solution[row] = vector[row]/matrix[row][row] - sum_other_terms/matrix[row][row]
                    
        if has_converged(previous_solution, current_solution):
            break
        
        iteration_count += 1

    print('Number of iteration:', iteration_count)
    print('Solution:', current_solution) 
    return current_solution    

def calculate_error(solution, reference):
    error_sum = 0.0
    for i in range(len(solution)):
        error_sum += (reference[i] - solution[i]) ** 2
    return math.sqrt(error_sum)

solution_vector = solve_system(coefficient_matrix, rhs_vector)
if solution_vector is not None:
    print('Accuracy', calculate_error(solution_vector, reference_solution))
