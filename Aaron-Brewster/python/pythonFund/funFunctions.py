def oddEven():

    x = ''

    for i in range(1, 2001):
        if(i%2 == 0):
            x = 'This is Even'
        elif(i%2 != 0):
            x = 'This is Odd'
        print('The number is', i, x)

oddEven()

def multiply(l, x):

    for i in l:
        l[i - 1] *= x
    return l

print(multiply([1,2,3,4], 5))
