class car(object):

    def displayAll(self):
        print('Price:', self.price,'\n',
            'Speed:', self.speed,'\n',
            'Fuel:', self.fuel, '\n',
            'Mileage:', self.mpg,'\n',
            'Tax', self.tax)

    def __init__(self, price, speed, fuel, mpg, tax = 0):

        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mpg = mpg
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12

        car.displayAll(self)

F150 = car(30000, 120, 'Full', 32)

Z370 = car(45000, 160, 'Empty', 26)

GTR = car(120000, 188, 'Half Full', 25)

Corvette = car(56000, 170, 'Half Empty', 30)

EFRSkylineGTR = car(20000, 210, 'Doesnt care!!!', 'Also doesnt care!!!')

Civic = car(18000, 90, 'Full', 40)
