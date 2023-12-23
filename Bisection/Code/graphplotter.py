import numpy as np
import matplotlib.pyplot as plt

plt.style.use('classic')


def f(n):
    return (n / (1 - n)) * ((6 / (2 + n)) ** 0.5) - 0.05


# for our given function, root cannot be less than 0 or greater than or equal to 1
# but negative starting point is used to get a better understanding of the root
x = np.linspace(-0.5, 0.99, 1000) # 1000 points between -0.5 and 0.99
# x = np.arange(-0.1,1.0,0.01)
plt.figure(num=0, dpi=120) # dpi = dots per inch
plt.grid()
# plotting the x & y axis, colour = blue, linewidth = 2, linestyle = solid, arrowstyle = ->
plt.axhline(0, color='blue', linewidth=2, linestyle='solid')
plt.axvline(0, color='blue', linewidth=2, linestyle='solid')
# plotting the function, colour = red, linewidth = 2, linestyle = solid
plt.plot(x, f(x), color='red', linewidth=2, linestyle='solid')


plt.show()
