class A:
    def method(self):
        print('this method belomgs to a class A')

class B(A):
    def method(self):
        print('this method belomgs to a class B')

class C(A):
    def method(self):
        print('this method belomgs to a class C')

class D(C,B):
    pass

d1 = D()
d1.method()

