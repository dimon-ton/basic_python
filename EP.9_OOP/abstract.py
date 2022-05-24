class Square:
    def __init__(self,length):
        self.length = length

    def calculate(self):
        return self.length * self.length

class Cube(Square):
    def __init__(self,length):
        super().__init__(length)

    def calculate(self):
        return super().calculate() * self.length

if __name__ == '__main__':

    square = Square(5)
    print(f'พท.สี่เหลี่ยมจตุรัส = {square.calculate()} ตารางหน่วย')

    cube = Cube(10)
    print(f'ปริมาตรลูกบาศก์ = {cube.calculate()} ตารางหน่วย')