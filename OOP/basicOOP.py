class Student:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def study(self):
        print(f'{self.name}กำลังเรียนอยู่...')

    def sawatdee(self):
        if self.gender == "ชาย":
            suffix = 'ครับ'
            callme = 'ผม'
        else:
            suffix = 'ค่ะ'
            callme = 'หนู'

        print(f'สวัสดี{suffix} {callme}ชื่อ{self.name}')

class SpecialStudent(Student):
    def __init__(self,name,age,gender,parent):
        super().__init__(name,age,gender)
        self.parent = parent
    def hello(self, person='เพื่อน'):
        if person == 'เพื่อน':
            print('เฮ้ย! ว่ายังไง! มีขนมกินไหม')
        else:
            print('รีบเดินหนีดีกว่าไม่อยากคุย')

    def sawatdee(self):
        print('หวัดดี ชื่อ{}'.format(self.name))
    def myfather(self):
        print('รู้ไหม? ผมลูกใคร')
        print(f'ผมลูก{self.parent}')

class Teacher:
    def __init__(self,name,gender, subject):
        self.name = name
        self.gender = gender
        self.subject = subject

    def teach(self):
        print('คุณครู{}กำลังสอนวิชา{}'.format(self.name, self.subject))


if __name__ == '__main__':
    student1 = Student('สมชาย',14,'ชาย')
    student2 = Student('สมศรี',14,'หญิง')
    special_student = SpecialStudent('จ๊อย',16,'ชาย','นายกอบต.')

    teacher1 = Teacher('จอห์น','ชาย','ภาษาอังกฤษ')

    print(teacher1.name)
    print(teacher1.subject)

    print('----------------8.30 น.-------------------')

    teacher1.teach()

    student1.sawatdee()
    student1.study()

    student2.sawatdee()
    student2.study()

    print('----------------8.45 น.-------------------')
    special_student.sawatdee()
    print('เดินไปที่โต๊ะตัวเอง')
    special_student.hello()
    print(f'ครู{teacher1.name}! ขอเกรดดี ๆ หน่อย')
    special_student.myfather()