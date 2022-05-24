class BankAccount:
    def __init__(self,name,age,amount):
        self.name = name
        self._age = age # protected
        self.__amount = amount # private

    def showMessage(self):
        print('กำลังทำรายการฝาก-ถอนในบัญชี')

    def _deposit(self, deposit):
        self.__amount += deposit
        print(f'ฝากเพิ่ม {deposit} รวมเงิน {self.__amount}')

    @property
    def amounts(self): # Getter
        return self.__amount
    
    @amounts.setter
    def amounts(self, amount): # Setter
        self.__amount = amount

    def __withdrow(self, withdrow):
        self.__amount -= withdrow
        print(f'ถอนออก {withdrow} เหลือเงิน {self.__amount}')

    # data = property(getAmount, setAmount)



class Employee(BankAccount):
    def __init__(self,name,age,amount):
        super().__init__(name,age,amount)



if __name__ == '__main__':
    employee = Employee('สมชาย', 20, 100000)
    print(employee.name)
    print(employee._age)
    print(employee.amounts)

    employee.amounts = 200000
    print(employee.amounts)
    # employee.showMessage()
    # employee._deposit(5000)
    # employee.__withdrow(50000)
