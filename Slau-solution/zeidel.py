from math import sqrt
import numpy as np

# Coefficient matrix and right-hand side vector
coefficient_matrix = np.array([
    [35, 10.5, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [10.5, 35, 10.5, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [4, 10.5, 35, 10.5, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 4, 10.5, 35, 10.5, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 4, 10.5, 35, 10.5, 4, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 4, 10.5, 35, 10.5, 4, 2, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 4, 10.5, 35, 10.5, 4, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 4, 10.5, 35, 10.5, 4, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 4, 10.5, 35, 10.5, 4, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 4, 10.5, 35, 10.5, 4, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 4, 10.5, 35, 10.5, 4, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 2, 4, 10.5, 35, 10.5, 4, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 4, 10.5, 35, 10.5, 4],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 4, 10.5, 35, 10.5],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 4, 10.5, 35]
], dtype=float)

right_hand_side = np.array([
    [-125], [-32], [-161.5], [-171], [17], 
    [-258.5], [-132.5], [32.5], [-73], [64.5],
    [-177], [-98], [-144.5], [-12.5], [209.5]
], dtype=float).flatten()

def solve_zeidel(coefficient_matrix, right_hand_side, tolerance=1e-6, max_iterations=1000):
    system_size = len(coefficient_matrix)
    current_solution = np.zeros(system_size)
    iterations = 0
    has_converged = False
    final_error = 0.0
    
    while not has_converged and iterations < max_iterations:
        new_solution = np.copy(current_solution)
        
        for row in range(system_size):
            sum_before = sum(coefficient_matrix[row][col] * new_solution[col] 
                         for col in range(row))
            
            sum_after = sum(coefficient_matrix[row][col] * current_solution[col] 
                         for col in range(row + 1, system_size))
            
            new_solution[row] = (right_hand_side[row] - sum_before - sum_after) / coefficient_matrix[row][row]
            
        final_error = sum(abs(new_solution[i] - current_solution[i]) for i in range(system_size))
        has_converged = final_error < tolerance
        iterations += 1
        current_solution = new_solution
        
    return current_solution, iterations, final_error

solution, iterations, error = solve_zeidel(coefficient_matrix, right_hand_side)

print(f'Number of iterations: {iterations}')
print(f'Solution: {solution}')
print(f'Final error: {error:.6f}')
