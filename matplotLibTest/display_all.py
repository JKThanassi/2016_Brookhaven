import matplotlib.pyplot as plt
from scatter_plot import *
from parab_and_cubic import *


def plot_all(start, end):
    assert type(start) is int
    assert type(end) is int

    plot(start, end, plt)
    scatter_plt(plt)

    plt.show()

plot_all(-10,10)


