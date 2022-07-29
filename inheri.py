from inheritance import person

class people(person):

    def __init__(self, course, passout):
        self.course = course
        self.passout = passout
        print('people details')
        print("$$$$$$$$$$$$$$$$")


p1 = people("MCA", 2022)
print(p1.course)
print(p1.passout)
