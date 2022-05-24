from abc import ABC, abstractclassmethod, abstractmethod

class Geometry(ABC):
    def __init__(self,base,height):
        self.base = base
        self.height = height

    @abstractmethod
    def callArea(self):
        # คำนวนหาพื้นที่
        pass

    
# พื้นที่เหลี่ยม
class Triangle(Geometry):
    def __init__(self,base,height):
        super().__init__(base,height)

    def callArea(self):
        return 0.5 * self.base * self.height

# พื้นที่สี่เหลี่ยมด้านขนาน
class Parallel(Geometry):
    def __init__(self, base, height):
        super().__init__(base,height)

    def callArea(self):
        return self.base * self.height

# พื้นที่รูปสี่เหลี่ยมขนมเปียกปูน
class Rhombus(Geometry):
    def __init__(self,base,height):
        super().__init__(base,height)

    def callArea(self):
        return self.base * self.height

if __name__ == '__main__':
    triangle = Triangle(10,6)
    print(f'พท.สามเหลี่ยม = {triangle.callArea()}')

    parallel = Parallel(10,6)
    print(f'พท.สี่เหลี่ยมด้านขนาน = {parallel.callArea()}')

    rhombus = Rhombus(10,6)
    print(f'พท.สี่เหลี่ยมขนมเปียกปูน = {rhombus.callArea()}')