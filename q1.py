class Class1():
    def __init__(self, x=5):
        self.x = x
class Class2(Class1):
    def test(self):
        pass

c2 =  Class2(2)
print(c2.x)

c2b = Class2()
print(c2b.x)

