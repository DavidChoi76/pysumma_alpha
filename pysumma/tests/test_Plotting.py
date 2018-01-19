#from pysumma.Plotting import Plotting # This is for testing in cmd window.
from pysumma.pysumma.Plotting import Plotting # This is for testing in this python code.
import unittest
from shutil import copyfile

# import numpy as np
# import matplotlib.pyplot as plt

class test_plot_class(unittest.TestCase):

    # def plot_square(x, y):
    #     y_squared = np.square(y)
    #     return plt.plot(x, y_squared)
    #
    # def test_plot_square1():
    #     x, y = [0, 1, 2], [0, 1, 2]
    #     line, = plot_square(x, y)
    #     x_plot, y_plot = line.get_xydata().T
    #     np.testing.assert_array_equal(y_plot, np.square(y))
    #
    # def test_plot_square2():
    #     f, ax = plt.subplots()
    #     x, y = [0, 1, 2], [0, 1, 2]
    #     plot_square(x, y)
    #     x_plot, y_plot = ax.lines[0].get_xydata().T
    #     np.testing.assert_array_equal(y_plot, np.square(y))