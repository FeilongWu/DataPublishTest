import random

def genRandom(a=0,b=100,n=1000):
    # generates a list of n intergers between a to b inclusive
    result=[]
    for i in range(n):
        result.append(random.randint(a,b))
    return result

if __name__=='__main__':
    url='data_x.txt'
    x=genRandom()
    f=open(url,'w')
    for i in x:
        f.write(str(i)+'\n')
    f.close()
