import matplotlib.pyplot as plt
from scatter_plot import *
from parab_and_cubic import *


def plot_all(start, end):
    """
    This function plots a scatterplot, a second order function, and a 3rd order function on one canvas.


    :param start: the start point for the grapg
    :param end: the end point for the graph
    :return: Void
    """
    assert type(start) is int
    assert type(end) is int

    plot(start, end, plt)
    scatter_plt(plt)

    plt.show()

plot_all(-10,10)


