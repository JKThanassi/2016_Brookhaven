#import matplotlib.pyplot as plt

def scatter_plt(plt):

    #list init
    x = []
    y = []

    #get list length
    list_length = int(input("How many data sets would you like to enter"))

    #get input
    for i in range(0, list_length):
        x.append(int(input("enter x var for dataset " + str(i))))
        y.append(int(input("enter y var for dataset " + str(i))))
        print()

    #create scatterplot
    plt.scatter(x, y, marker='*')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Test scatter plt")
    #plt.show(



