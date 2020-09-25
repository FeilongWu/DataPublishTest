def LinMap(x,slop=3,intercept=6):
    # transforn a list of numbers in list x to a new list of numbers
    # by this formula: y=slop*x+intercept
    eq=lambda x: slop*x+intercept
    y=[eq(i) for i in x]
    return y

if __name__=='__main__':
    url='data_x.txt'
    url1='data_y.txt'
    x=[]
    f=open(url)
    for i in f.readlines():
        x.append(int(i[:-1]))
    f.close()
    y=[]
    for i in x:
        y.append(i*3+6)
    f=open(url1,'w')
    for i in y:
        f.write(str(i)+'\n')
    f.close()
