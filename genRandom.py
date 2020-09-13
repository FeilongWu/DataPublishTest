import random

def genRandom(a=0,b=100,n=1000):
    # generates a list of n intergers between a to b inclusive
    result=[]
    for i in range(n):
        result.append(random.randint(a,b))
    return result
