def drawStars(list):

    x  = 0
    y = '*'
    z = 0

    for i in list:
        z += 1
        x = list[z - 1]
        if type(x) is str:
            print(x[0] * len(x))
        else:
            print(y * x)

drawStars([1,5,'poop',3])
