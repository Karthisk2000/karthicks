class calc:
    num=100

    def getdata(self,a,b):
        self.firstnumber = a
        self.secondnumber = b
        #print('hi in a fun')

    def addition(self):
        return self.firstnumber + self.secondnumber +\
        self.thirdnumber + self.fourthnumber+ calc.num

    def __init__(self,c,d):
        self.thirdnumber = c
        self.fourthnumber = d
        #print('hii')

m= calc(20,20)
m.getdata(40,40)
print(m.addition())

m1 = calc(10,30)
m1.getdata(20,30)
print(m1.addition())