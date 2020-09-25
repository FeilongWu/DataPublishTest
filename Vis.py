import matplotlib.pyplot as plt

def Vis(x,y,path):
    # create a scatter plot of s and y

    plt.scatter(x,y)
    plt.xlabel('x',fontsize='large')
    plt.ylabel('y',fontsize='large')
    plt.title('Scatter Plot')
    plt.savefig(path)
    plt.show()

if __name__=='__main__':
    url='data_x.txt'
    url1='data_y.txt'
    plot='Scatter_Plot.png'
    x,y=[],[]
    f=open(url)
    for i in f.readlines():
        x.append(int(i[:-1]))
    f.close()
    f=open(url1)
    for i in f.readlines():
        y.append(int(i[:-1]))
    f.close()
    Vis(x,y,plot)
    
