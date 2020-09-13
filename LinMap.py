def LinMap(x,slop=3,intercept=6):
    # transforn a list of numbers in list x to a new list of numbers
    # by this formula: y=slop*x+intercept
    eq=lambda x: slop*x+intercept
    y=[eq(i) for i in x]
    return y
