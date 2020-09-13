import matplotlib.pyplot as plt

def Vis(x,y):
    # create a scatter plot of s and y

    plt.scatter(x,y)
    plt.xlabel('x',fontsize='large')
    plt.ylabel('y',fontsize='large')
    plt.show()
