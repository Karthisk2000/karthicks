class Employee:

    def setnumberofworkinghours(self):
        self.numberofworkinghours=40

    def displaythenumberworkinghours(self):
        print( self.numberofworkinghours)


class trainee(Employee):

    def setnumberofworkinghours(self):
        self.numberofworkinghours=45



    def resetumberofworkinghours(self):
        super().setnumberofworkinghours()


employee = Employee()
employee. setnumberofworkinghours()
print('number of working hours of the employee : ',end ='')
employee. displaythenumberworkinghours()


Trainee = trainee()
Trainee.setnumberofworkinghours()
print('number of working hours of the traine : ',end = '')
Trainee.displaythenumberworkinghours()

Trainee.resetumberofworkinghours()
print('number of working hours in reset: ',end='')
Trainee.displaythenumberworkinghours()