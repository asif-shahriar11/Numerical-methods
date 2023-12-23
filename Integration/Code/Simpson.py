import numpy as np

def f(t):
    """
    distance covered by rocket at time t
    :param t: time (s)
    :return: distance covered by rocket at time t (m)
    """
    m0 = 140000 # initial mass of rocket (kg)
    q = 2100 # rate at which fuel is expelled (kg/s)
    u = 2000 # velocity at which fuel is being expelled (m/s)
    g = 9.8 # acceleration due to gravity (m/s^2)

    # f(t) = u * ln(m0/(m0 - qt)) - gt
    return u * np.log(m0 / (m0 - q * t)) - g * t


def simpson(a, b, n):
    """
    function to calculate the value of integral using simpson's 1/3 rule
    :param a: lower limit of integral
    :param b: upper limit of integral
    :param n: number of intervals
    :return: value of integral
    """

    h = (b - a) / n # width of each interval
    l = [] # list to store the values of x0, x1, x2, ..., xn
    for i in range(n + 1):
        l.append(a + i * h)
    oddsum = 0.0
    evensum = 0.0
    for i in range(1, n):
        if i % 2 == 0:  evensum = evensum + 2 * f(l[i])
        else:   oddsum = oddsum + 4 * f(l[i])

    return h/3 * (f(a) + evensum + oddsum + f(b)) # return the value of integral


def main():
    "main function"
    lower_limit = 8
    upper_limit = 30
    n = input("Enter the number of intervals: ")
    # if no value of n is provided, then the default value of n is 5
    if n == "": 
        n = 5
        print("Default value of n = 5 is used.")
    else:   n = int(n)
    print("  n  \tDistance Covered\tAbsolute Relative Error")
    print("-----\t----------------\t-----------------------")
    for i in range(1, n + 1):
        approxval = simpson(lower_limit ,upper_limit, 2 * i)
        if i == 1:
            prev = approxval
            print("{:^5d}".format(2*i), "\t", "{:^16f}".format(approxval), "\t","          -        ")
        else:
            error = np.abs((approxval - prev) / approxval) * 100
            print("{:^5d}".format(2*i), "\t", "{:^16f}".format(approxval), "\t", "{:^23f}".format(error))
            prev = approxval


if __name__ == "__main__":
    main()