class base:
    def __init__(self) -> None:
        self._a=2

class derived(base):
    def __init__(self) -> None:
        base.__init__(self)
        print("calling protected member: ",self._a)
        self._a=5
        print('calling protected member outside class: ',self._a)

obj1=derived()
obj2=base()

print('accessing protected mem of obj1: ',obj1._a)

print('accessing protected mem of obj2: ',obj2._a)


# private member
class Base:
    def __init__(self):
        self.a = "bhardawjudhay"
        self.__c = "udhay bhardwaj"
 
class Derived(Base):
    def __init__(self):
 
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)
 
 
obj1 = Base()
print(obj1.a)



