# calculate_pi.py
# MIT License
# github.com/viktor40/HammerBotPython

"""
Calculate the value of π using the Leibniz formula for pi: https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80.
This is a rather slow way to calculate π since the series converges slowly. This was mostly a personal exercise.

ITERATIONS will determine the number of iterations to perform to calculate the value of pi.
"""

import matplotlib.pyplot as plt
import numpy as np

ITERATIONS = 50
PLOT = True
x, y = [], []


def calculate_pi(iterations: int):
    """
    Use leibniz series to calculate pi.
    :param iterations: sets the number of iterations to be executed. After this has been reach the program will stop
    :param plot: set if you want to plot the values
    :yield: the function will yield the nth iteration of the leibniz series, together with n.
    """
    pi_ = 0
    for n_ in range(0, iterations):
        pi_ += 4 * ((-1) ** n_) / (2 * n_ + 1)
        yield pi_, n_


pi_iterator = calculate_pi(ITERATIONS)
for value in pi_iterator:
    pi, n = value
    print("After {} iteration{}, the value of π equals {}".format(n + 1, "s" if n else "", pi))

    if PLOT:
        x.append(n)
        y.append(pi)

if PLOT:
    plt.plot(x, y, color='blue')
    plt.plot([0, ITERATIONS], [np.pi, np.pi], color='red')
    plt.xlabel('Number of iterations n')
    plt.ylabel('Value of pi')
    plt.show()
