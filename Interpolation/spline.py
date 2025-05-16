import numpy as np
from math import sqrt

def cubic_spline_coefficients(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    n = len(x)
    
    if np.any(np.diff(x) < 0):
        idx = np.argsort(x)
        x, y = x[idx], y[idx]
        
    x_diff = np.diff(x)
    y_diff = np.diff(y)
    
    lower_diag = np.zeros(n-1)
    main_diag = np.zeros(n)
    z = np.zeros(n)
    
    main_diag[0] = sqrt(2 * x_diff[0])
    z[0] = 0
    
    for i in range(1, n-1):
        lower_diag[i] = x_diff[i-1] / main_diag[i-1]
        main_diag[i] = sqrt(2 * (x_diff[i-1] + x_diff[i]) - lower_diag[i-1]**2)
        b = 6 * (y_diff[i]/x_diff[i] - y_diff[i-1]/x_diff[i-1])
        z[i] = (b - lower_diag[i-1] * z[i-1]) / main_diag[i]
        
    # Backward pass - substitution
    z[n-1] = 0
    for i in range(n-2, -1, -1):
        z[i] = (z[i] - lower_diag[i] * z[i+1]) / main_diag[i]
        
    return x, y, z

def evaluate_cubic_spline(x0, x, y, z):
    x0 = np.asarray(x0)
    idx = np.searchsorted(x, x0)
    np.clip(idx, 1, len(x)-1, out=idx)
    
    xi0, xi1 = x[idx-1], x[idx]
    yi0, yi1 = y[idx-1], y[idx]
    zi0, zi1 = z[idx-1], z[idx]
    h = xi1 - xi0
    
    # Cubic spline formula
    term1 = zi0/(6*h) * (xi1-x0)**3
    term2 = zi1/(6*h) * (x0-xi0)**3
    term3 = (yi1/h - zi1*h/6) * (x0-xi0)
    term4 = (yi0/h - zi0*h/6) * (xi1-x0)
    
    return term1 + term2 + term3 + term4

def cubic_spline_interpolation(x_new, x_orig, y_orig):
    x, y, z = cubic_spline_coefficients(x_orig, y_orig)
    return evaluate_cubic_spline(x_new, x, y, z)

if __name__ == '__main__':
    x = np.linspace(0, 10, 11)
    y = np.sin(x)
    
    x_new = np.linspace(0, 10, 201)
    y_new = cubic_spline_interpolation(x_new, x, y)
    
    import matplotlib.pyplot as plt
    plt.scatter(x, y, label='Original Data')
    plt.plot(x_new, y_new, label='Cubic Spline', color='orange')
    plt.legend()
    plt.show()
