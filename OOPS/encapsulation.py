class Encap:
    n = 10 #Public variable
    _n = 100 # Protected variable
    __n = 10000 #Private
    
    def myfunc(self):
        print(self.__n)
    
obj = Encap()
print(obj.n)
print(obj._n)

# print(obj.__n)
obj.myfunc()
