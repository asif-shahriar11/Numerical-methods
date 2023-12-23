def bisection_demo(lower_bound, upper_bound, err_expected, max_iteration):
    "this version outputs a table showing the absolute relative approx error after each iteration"

    print("Iteration\t\tpreviously assumed root\t\tcurrent assumed root\t\tapproximate error (%)")
    print("_________\t\t_______________________\t\t____________________\t\t_____________________")
    print()

    for i in range(max_iteration):
        mid = (lower_bound + upper_bound) / 2
        f_lower_bound = (lower_bound / (1 - lower_bound)) * ((6 / (2 + lower_bound)) ** 0.5) - 0.05
        f_mid = (mid / (1 - mid)) * ((6 / (2 + mid)) ** 0.5) - 0.05
        f_upper_bound = (upper_bound / (1 - upper_bound)) * ((6 / (2 + upper_bound)) ** 0.5) - 0.05

        if f_mid == 0.0:    return mid
        elif (f_lower_bound * f_mid) < 0:   upper_bound = mid
        elif (f_upper_bound * f_mid) < 0:   lower_bound = mid
        else:   return "root does not exist in the given interval"
        
        if i == 0:
            mid_old = mid
            continue # first iteration

        err = abs((mid - mid_old) / mid) * 100
        if err <= err_expected: 
            print("{:^9d}".format(i+1), "\t\t","{:^23f}".format(mid_old) , "\t", "{:^20f}".format(mid), "\t\t","{:^21f}".format(err))
            return mid
        else:
            print("{:^9d}".format(i+1), "\t\t","{:^23f}".format(mid_old) , "\t", "{:^20f}".format(mid), "\t\t","{:^21f}".format(err))
            mid_old = mid

    return "Max iteration reached without success"



def main():
    "main function"
    lower_bound = 0.0 # lower bound of the interval in which the root lies - found by plotting the graph
    upper_bound = 0.4 # upper bound of the interval in which the root lies - found by plotting the graph
    err_expected = 0.5 # expected error in percentage
    max_iteration = 20 # maximum number of iterations allowed

    root = bisection_demo(lower_bound, upper_bound, err_expected, max_iteration)
    print("Root =", root)


if __name__ == "__main__":
    main()