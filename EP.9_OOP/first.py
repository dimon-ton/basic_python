class First:
    language = 'Python'

    def learn(): #static method
        print(f'ฉันกำลังเรียนเขียนโปรแกรมภาษา {First.language}')

    def teach(self):
        First.learn()
        print(f'ฉันสามารถสอนเขียนโปรแกรม {self.language}')

if __name__ == '__main__':
    print(f'นี่คือภาษา {First.language}')
    First.learn()

    first = First()
    first.teach()
