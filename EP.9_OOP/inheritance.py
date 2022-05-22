class One:
    name = None

    def __init__(self,name):
        self.name = name

    def walk(self):
        print('He is walking')

class Two(One):
    nickname = None

    def __init__(self,name,nickname):
        super().__init__(name)
        self.nickname = nickname


    def run(self):
        print('He is running')

class Three(One):

    def eat(self):
        print('He is eating')

class Four(Two):

    def fly(self):
        print('I can fly')

if __name__ == '__main__':
    # three = Three()
    # print(three.name)

    # three.eat()
    # three.walk()

    # four = Four()

    # print(four.name)
    # print(four.nickname)

    # four.walk()
    # four.run()


    two = Two('สมชาย','ชาย')


    print(two.name)
    print(two.nickname)

