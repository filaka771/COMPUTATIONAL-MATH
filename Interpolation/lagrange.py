import numpy as np
import matplotlib.pyplot as plt

interval_start = 0
interval_end = 8
step_size = 0.01

interpolatin_nodes = np.array([
    [0, 0], [1, 0], [2, 0], 
    [3, 10],  
    [4, 0], [5, 0], 
    [6, 0], [7, 0], [8, 0]
])

def calculate_lagrange_basis(i, node_x_values, x):
    basis_value = 1.0
    for j in range(len(node_x_values)):
        if i == j:
            continue
        basis_value *= (x - node_x_values[j]) / (node_x_values[i] - node_x_values[j])
    return basis_value

def evaluate_lagrange_polynomial(x, nodes):
    node_x = nodes[:, 0]
    node_y = nodes[:, 1]
    
    interpolated_value = 0.0
    for i in range(len(node_y)):
        interpolated_value += node_y[i] * calculate_lagrange_basis(i, node_x, x)
    return interpolated_value

def generate_interpolation_curve(nodes, start, end, step):
    num_points = int((end - start) / step)
    curve_points = np.empty((num_points, 2))
    
    for i in range(num_points):
        x = start + i * step
        curve_points[i, 0] = x
        curve_points[i, 1] = evaluate_lagrange_polynomial(x, nodes)
        
    return curve_points

def plot_results(curve_points, nodes):
    plt.figure(figsize=(10, 6))
    
    plt.plot(curve_points[:, 0], curve_points[:, 1], 
             label='Lagrange Interpolation', color='blue')
    
    plt.scatter(nodes[:, 0], nodes[:, 1], color='red', 
                label='Interpolation Nodes', zorder=5)
    
    plt.title('Lagrange Interpolation')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    curve = generate_interpolation_curve(
        interpolatin_nodes, 
        interval_start, 
        interval_end, 
        step_size
    )
    plot_results(curve, interpolatin_nodes)

main()
