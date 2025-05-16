import copy
import numpy as np

# Initialize the system matrix
system_matrix = np.array([[2., 2, 1, 1],
                          [1, 2, 1, 1],
                          [0, 1, 1, 2]])
print("Initial matrix:")
print(system_matrix)


def gaussian_elimination(matrix):
    epsilon = 1e-16  # Machine accuracy
    
    # Create working copies of the matrix
    original_matrix = np.array(matrix)
    working_matrix = np.array(matrix)
    
    num_rows = len(working_matrix[:, 0])
    num_cols = len(working_matrix[0, :])
    
    for pivot_row in range(num_rows):
        # Partial pivoting - find row with maximum element in current column
        max_value = abs(working_matrix[pivot_row][pivot_row])
        max_row = pivot_row
        
        for row in range(pivot_row, num_rows):
            if abs(working_matrix[row][pivot_row]) > max_value:
                max_value = abs(working_matrix[row][pivot_row])
                max_row = row
                
        # Swap rows if necessary
        if max_row != pivot_row:
            working_matrix[pivot_row, :], working_matrix[max_row, :] = \
                working_matrix[max_row, :], working_matrix[pivot_row, :]
            
        # Normalize the pivot row
        pivot_element = float(working_matrix[pivot_row][pivot_row])
        working_matrix[pivot_row, pivot_row:] = working_matrix[pivot_row, pivot_row:] / pivot_element
        
        # Eliminate elements below the pivot
        for row_below in range(pivot_row + 1, num_rows):
            factor = working_matrix[row_below][pivot_row]
            working_matrix[row_below, pivot_row:] -= working_matrix[pivot_row, pivot_row:] * factor
            
    # Perform back substitution
    solution = back_substitution(working_matrix, num_rows)
    
    print("\nResidual error:")
    print(calculate_residual(original_matrix, solution, num_rows))
    
    return solution


def back_substitution(matrix, num_rows):
    matrix = np.array(matrix)
    
    for current_row in range(num_rows - 1, 0, -1):
        for row_above in range(current_row - 1, -1, -1):
            matrix[row_above][num_rows] -= matrix[row_above][current_row] * matrix[current_row][num_rows]
            
    return matrix[:, num_rows]


def calculate_residual(original_matrix, solution, num_rows):
    original_matrix = np.array(original_matrix)
    solution = np.array(solution)
    
    right_hand_side = copy.deepcopy(original_matrix[:, num_rows])
    calculated_values = np.zeros(num_rows)
    
    # Calculate Ax 
    for row in range(num_rows):
        for col in range(num_rows):
            calculated_values[row] += original_matrix[row][col] * solution[col]
            
    # Calculate residual: Ax - b
    residual = copy.deepcopy(calculated_values)
    for i in range(num_rows):
        residual[i] = abs(residual[i] - right_hand_side[i])
        
    return residual


solution = gaussian_elimination(system_matrix)
print("\nSolution vector:")
print(solution)
