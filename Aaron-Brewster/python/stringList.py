str = "if monkeys like bananas, then I must be a monkey!"

print(str.find('monkey'))

print(str.replace('monkey','alligator'))

x = [2,5,-6,7,8,-8,54,99,3,-2,45454]

print(min(x), max(x))

print(x[0], x[len(x)-1])

newList = []

newList.extend((x[0], x[len(x) - 1]))

print(newList)

x.sort()
y = []

for i in x[:]:
    if(i < 0):
        y.append(i)
        x.remove(i)

x.insert(0, y)

print(x)
