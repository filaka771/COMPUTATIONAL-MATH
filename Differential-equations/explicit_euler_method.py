import numpy as np
import matplotlib.pyplot as plt
# Initial conditions and parameters
initial_y = 0.5
start_time = 0.0
end_time = 20.0
step_size = 0.001

def dydt(t, y):
    return y - t**2 + 1

def explicit_euler(f, y0, t0, t_end, step):
    t_values = [t0]
    y_values = [y0]

    t = t0
    y = y0

    while t < t_end:
        y = y + step * f(t, y)
        t = t + step

        t_values.append(t)
        y_values.append(y)

    return t_values, y_values

def main():
    # Solve the ODE
    times, solutions = explicit_euler(dydt, initial_y, start_time, end_time, step_size)

    # Plot the solution
    plt.figure(figsize=(8, 5))
    plt.plot(times, solutions, label="Solution", color="blue", marker="o")
    plt.title("Solution")
    plt.xlabel("t")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

main()

