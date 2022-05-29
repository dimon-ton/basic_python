from turtle import Turtle


class Car:
    brand = None
    year = None
    fuel = None
    status = None

    def __init__(self, brand='Toyota', year=2020, fuel=100.00, status=True):
        self.brand = brand
        self.year = year
        self.fuel = fuel
        self.status = status

    def checkStatus(self):
        if self.status == True:
            print('This car is passed')
        else:
            print('This car is not passed')


    def drive(self):
        print('This car is driving.')

if __name__ == '__main__':
    car01 = Car('Benz',2020,10.00,True)
    car02 = Car('Ford',2019,50.00,False)
    
    print('ยี่ห้อ: {}'.format(car01.brand))
    print('ปีที่ผลิต: {}'.format(car01.year))
    print('ระดับเชื้อเพลิง: {}'.format(car01.fuel))

    car01.drive()
    car01.checkStatus()

    car02.drive()
    car02.checkStatus()