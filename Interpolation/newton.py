import math
import sympy
import numpy as np
import matplotlib.pyplot as plt


def target_function(x):
    return 1 / (x**4 + 1)


def divided_difference(nodes):
    result = 0.0
    for i in range(len(nodes)):
        denominator = 1.0
        for j in range(len(nodes)):
            if j == i:
                continue
            denominator *= (nodes[i] - nodes[j])
            result += (target_function(nodes[i]) / denominator)
    return result


def generate_newton_polynomial(interpolation_nodes):
    polynomial = target_function(interpolation_nodes[0])
    
    if len(interpolation_nodes) == 1:
        return polynomial
    
    product_term = 1
    for i in range(len(interpolation_nodes) - 1):
        product_term *= (x - interpolation_nodes[i])
        polynomial += divided_difference(interpolation_nodes[:i + 2]) * product_term
        
    return polynomial


def plot_interpolation(original_func, interpolated_poly, x_range=(-10, 10)):
    x_vals = np.linspace(x_range[0], x_range[1], 100)
    
    # Evaluate functions
    original_y = [original_func(x_val) for x_val in x_vals]
    interpolated_y = [interpolated_poly.subs(x, x_val) for x_val in x_vals]
    
    # Create plot
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, original_y, label=r'Original: $\frac{1}{x^4+1}$', color='blue', linewidth=2)
    plt.plot(x_vals, interpolated_y, label='Newton Interpolation', color='red', linestyle='--')
    
    # Add interpolation nodes
    nodes_x = np.linspace(x_range[0], x_range[1], 11)
    nodes_y = [original_func(x_val) for x_val in nodes_x]
    plt.scatter(nodes_x, nodes_y, color='green', label='Interpolation Nodes', zorder=5)
    
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Newton Interpolation Comparison')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    x = sympy.symbols('x')
    
    interpolation_nodes = np.linspace(-10, 10, 11)
    newton_polynomial = sympy.expand(generate_newton_polynomial(interpolation_nodes))
    plot_interpolation(target_function, newton_polynomial)
