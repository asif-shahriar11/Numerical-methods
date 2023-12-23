def GaussianElimination(A, B, d):
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



def main():
    "main function"
    A = [] # coefficient matrix
    B = [] # constant matrix
    n = int(input("Enter the number of unknowns: "))
    print("Enter the coefficients: ")
    for r in range(n):
        elements = input()
        row = elements.split(' ')
        f_row = [float(i) for i in row]
        A.append(f_row)
    print()
    print("Enter the constant magnitudes of each equation: ")
    for i in range(n):
        B.append(float(input()))

    sol = GaussianElimination(A, B, True)

    print()
    print("Solution: ")
    for i in range(len(sol)):
        print(round(sol[i], 4))


if __name__ == '__main__':
    main()

