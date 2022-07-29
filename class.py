from karthick import calc

class child(calc):
    num2 = 200

    def __init__(self):
        calc.__init__(self,2,10)

    def getdata1(self):
        return self.num2 + self.num + self.addition()


obj = child()
obj.getdata(10,10)
print(obj.getdata1())

