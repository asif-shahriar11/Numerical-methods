import numpy as np
import matplotlib.pyplot as plt

def gaussian_elimination(A, B, d = False):
    """
    Function to solve a system of linear equations using Gaussian Elimination
    :param A: coefficient matrix
    :param B: constant matrix
    :param d: boolean to print intermediate matrices
    :return: solution vector
    """
    m = len(A[0])
    # forward elimination
    for i in range(m - 1):
        for j in range(i + 1, m, 1):
            f = A[j][i] / A[i][i]
            for k in range(i, m, 1):
                A[j][k] = A[j][k] - f * A[i][k]
            B[j] = B[j] - f * B[i]

            # printing the intermediate matrices
            if d:
                print()
                print("A:")
                print([[round(i, 4) for i in j] for j in A], sep='\n', end='\n\n', flush=True)
                print("B:")
                print([round(i, 4) for i in B], sep='\n', end='\n\n', flush=True)              

    # back substitution
    x = [0.0] * m
    x[m-1] = B[m-1]/A[m-1][m-1]
    for i in range(m-2, -1, -1):
        nom = B[i]
        for j in range(i, m, 1):
            nom = nom - A[i][j] * x[j]
        x[i] = nom/A[i][i]

    return x


def linear_regression(x,z):
    """
    function to find the coefficients of a linear regression model
    :param x: x values
    :param z: z values
    :return: coefficients of the linear regression model
    """
    n = len(x) # number of data points
    A = np.zeros((2,2)) # coefficient matrix
    B = np.zeros(2) # constant matrix
    A[0][0] = n
    A[0][1] = np.sum(x)
    A[1][0] = A[0][1]
    A[1][1] = np.sum(x ** 2)
    B[0] = np.sum(z)
    B[1] = np.sum(x * z)

    return gaussian_elimination(A, B)


def func(k_max, c_s, c):
    """
    function to determine the growth rate of bacteria
    :param k_max: maximum growth rate
    :param c_s: substrate concentration at which growth rate is half of k_max
    :param c: substrate concentration
    :return: growth rate of bacteria
    """
    return (k_max * (c ** 2)) / (c_s + (c ** 2))



def plotline(k_max, c_s, c, k):
    "function to plot the graph of the data points and the regression line"
    x1 = np.arange(0.5, 4.1, 0.1)
    plt.plot(x1, func(k_max, c_s, x1), color = 'red')  # main graph
    # Creating axes
    plt.grid(True, which = 'both')
    plt.axhline(y = 0, color = 'blue')
    plt.axvline(x = 0, color = 'blue')
    # Labeling axis
    plt.xlabel('c')
    plt.ylabel('k')
    # Adding title
    plt.title('Growth Rate of Bacteria')
    
    plt.scatter(c, k)
    plt.show()


def main():
    "main function"
    # nput: c, k
    c = [] # substrate concentration
    k = [] # growth rate of bacteria
    # reading from file
    handler = open("data.txt", 'r')
    for line in handler:
        line = line.rstrip()
        values = line.split()
        c.append(float(values[0]))  # appending to float
        k.append(float(values[1]))
    x = np.array(c)
    z = np.array(k)

    # finding the coefficients of the linear regression model
    # here, x = 1 / (c ** 2) and z = 1 / k
    for i in range(len(c)):
        x[i] = 1 / ( c[i] ** 2)
        z[i] = 1 / k[i]
    sol = linear_regression(x, z) 
    k_max = 1/sol[0]
    c_s = k_max * sol[1]

    print("solution: k_max = ", k_max, ", c_s = ", c_s)

    plotline(k_max, c_s, c, k)


if __name__ == "__main__":
    main()

