class Product:
    def __init__(self,name: str,price: float,quantity=0):
        assert price >= 0, f"ราคา {price} ต้องมากกว่าหรือเท่ากับ 0!"
        assert quantity >= 0, f"ปริมาณ {quantity} ต้องมากกว่าหรือเท่ากับ 0!"

        self.name = name
        self.price = price
        self.quantity = quantity

    def total(self,para_quantity):
        return self.price * para_quantity

    def discount(self,num: float):
        assert num >= 0, f"ส่วนลด {num} ต้องมากกว่าหรือเท่ากับ 0!"

        return  num*self.price

class Fruit(Product):
    def __init__(self,name, price, quantity,weight):
        super().__init__(name,price,quantity)
        assert weight >= 0, f"น้ำหนัก {weight} ต้องมากกว่าหรือเท่ากับ 0!"

        self.weight = weight

    def full_weight(self):
        return self.quantity * self.weight

class Customer:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def fullname(self):
        return self.fname + " " + self.lname

    



if __name__ == '__main__':

    product1 = Product('คอมพิวเตอร์',15000,20)
    product2 = Product('ปริ้นเตอร์',3000,15)
    product3 = Product('คีย์บอร์ด',15000,16)
    product4 = Product('เมาส์',450,11)
    product5 = Fruit('ทุเรียน',120,5,0.8)
    product6 = Fruit('เงาะ',90,14,0.1)

    customer1 = Customer('สมชาย','ใจดี')
    customer2 = Customer('สมศรี','เรียนเก่ง')

    product1.total(5)

    print(f'{customer1.fullname()} ต้องการซื้อคอมพิวเตอร์จำนวน 5 เครื่อง คิดเป็นเงิน {product1.total(5)} เนื่องจาก {customer2.fullname()} ซึ่งเป็นภรรยาของ {customer1.fullname()} ต้องการส่วนลดเพราะซื้อสินค้ามากกว่า 1 เครื่อง')
    print(f'ถ้าร้านเลยเสนอลดราคาให้ 15 เปอร์เซ็น เหลือราคา {product1.discount(0.85)*5:,.2f}')
    print('\nเนื่องจากซื้อคอมพิวเตอร์แล้วต้องมีอุปกรณ์เสริมจึงซื้อสินค้าตามรายการดังต่อไปนี้')

    print(f'\n\tซื้อ{product1.name} ราคา {product1.price:,.2f} จำนวน 5 เครื่อง รวม {product1.total(5):,.2f} ได้ส่วนลดเหลือ {product1.discount(0.85)*5:,.2f}')
    print(f'\tซื้อ{product2.name} ราคา {product2.price:,.2f} จำนวน 5 เครื่อง รวม {product2.total(5):,.2f}')
    print(f'\tซื้อ{product3.name} ราคา {product3.price:,.2f} จำนวน 5 เครื่อง รวม {product3.total(5):,.2f}')

    IT_total = product1.discount(0.85)*5 + product2.total(5) + product3.total(5) + product4.total(5)
    print(f'\n\tรวมจำนวนเงินทั้งหมด {IT_total:,.2f}')

    print(f'\n{customer2.fullname()}เหลือบไปเห็น{product5.name}จึงอยากได้และขอซื้อ{product5.name}ในราคา {product5.total(2):,.2f} จำนวน {product5.weight*2} กิโลกรัม ')
    ALL_TOTAL = IT_total + product5.total(2)
    print(f'รวมแล้ว {customer1.fullname()} และ {customer2.fullname()} ต้องจ่ายเงินทั้งหมด {ALL_TOTAL:,.2f}')


