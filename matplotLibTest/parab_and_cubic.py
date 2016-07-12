#import matplotlib.pyplot as plt


def plot(list_start, list_end, plt):
    #2nd order vars
    parab_x = range(list_start, list_end)
    parab_y = []

    #for loop to assign values to 2nd order y list
    for x_val in parab_x:
        parab_y.append(x_val**2)

    #3rd order vars
    cubic_x = parab_x[:]
    cubic_y = []

    #for loop to assign 3rd order y vals
    for x_val in cubic_x:
        cubic_y.append(x_val**3)

    #create plot
    plt.plot(parab_x, parab_y)
    plt.plot(cubic_x, cubic_y)

    #plt.show()

    #return plt

#plot(-5,5)