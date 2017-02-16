class mathDojo(object):

    def __init__(self):
        self.val = 0

    def add(self, x, y = 0):
        self.y = y
        if type(x) == list:
            for i in x:
                self.val += i
        else:
            self.val += x
        if type(y) == list:
            for i in y:
                self.val += i
        else:
            self.val += y
        return self

    def sub(self, x, y = 0):
        self.y = y
        if type(x) == list:
            for i in x:
                self.val -= i
        else:
            self.val -= x
        if type(y) == list:
            for i in y:
                self.val -= i
        else:
            self.val -= y
        return self

md = mathDojo()

md.add(2, [2,3]).add([4,3,6]).sub([3], [4,7])

print(md.val)
