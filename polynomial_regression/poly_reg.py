import numpy as np
import matplotlib.pyplot as plt

def calculate_matrix(x, n):
    m = len(x)
    matrix = np.zeros((n+1, n+1))
    for i in range(n+1):
        for j in range(n+1):
            matrix[i][j] = np.sum(x**(i+j))
    return matrix

def calculate_vector(x, y, n):
    m = len(x)
    vector = np.zeros(n+1)
    for i in range(n+1):
        vector[i] = np.sum(y * x**i)
    return vector

def calculate_b(x, y, n):
    k = calculate_matrix(x, n)
    l = calculate_vector(x, y, n)
    return np.linalg.solve(k, l)

if __name__ == "__main__":
    X = np.array([1, 2, 3, 4, 5, 6, 7])
    Y = np.array([45000, 50000, 60000, 80000, 110000, 150000, 200000])

    n = 3  # Adjust the degree of polynomial as needed
    b_coeffs = calculate_b(X, Y, n)
    x_vals = np.linspace(1, 7, 100)
    y_vals = sum(b_coeffs[i] * x_vals**i for i in range(n+1))
    plt.scatter(X, Y, color='blue')
    plt.plot(x_vals, y_vals, label='Polynomial Regression')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Plot of Polynomial Regression')
    plt.legend()
    plt.grid(True)
    plt.show()
