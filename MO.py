#polymorphism

class myname:

    def entervalue(self):
        self.entervalue = 40

    def outputvalue(self):
        print(self.entervalue)

class othername(myname):

    def entervalue(self):
        self.entervalue = 50


p1 = myname()
p1.entervalue()
print('number of value enter:')
p1.outputvalue()

o1 = othername()
o1.entervalue()
print('number of value:')
o1.outputvalue()