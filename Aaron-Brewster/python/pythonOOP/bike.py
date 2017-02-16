class bike(object):

    def __init__(self, price, speed, miles = 0):

        self.price = price
        self.speed = speed
        self.miles = miles

    def displayInfo(self):
        print(self.price, self.speed, self.miles)

    def ride(self):
        self.miles += 10
        return self

    def reverse(self):
        if self.miles > 0:
            self.miles -= 5
        return self

huffy = bike(100, 20)
speedfactory = bike(500, 40)
livestrong = bike(300, 35)

huffy.ride().ride().ride().reverse().displayInfo()

speedfactory.ride().ride().reverse().reverse().displayInfo()

livestrong.reverse()
livestrong.reverse()
livestrong.reverse()
livestrong.displayInfo()
