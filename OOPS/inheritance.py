#Single level Inheritance
'''
class Parent:
    def pdisplay(self):
        print("This is parent property")


class Child(Parent):
    def cdisplay(self):
        print("This is child property")
        
c = Child()
c.cdisplay()
c.pdisplay()

#Multi Level Inheritance

class GrandParent:
    def gpdisplay(self):
        print("Grand Parent propery")
        
class Parent(GrandParent):
    def pdisplay(self):
        print("Parent Property")
        
class Child(Parent):
    def cdisplay(self):
        print("Child Property")
        
c = Child()
c.cdisplay()
c.pdisplay()
c.gpdisplay()


#Multiple Inheritance
class Father:
    def fdisplay(self):
        print("This is father display")
        

class Mother:
    def mdisplay(self):
        print("This is mother display")
        

class Child(Father, Mother):
    def cdiplay(self):
        print("This is child property")
        
c = Child()
c.cdiplay()
c.fdisplay()
c.mdisplay()


'''


# Hierarchicle Inheritance
class Parent:
    def pdisplay(self):
        print("parent property")
    
class Child1(Parent):
    def c1display(self):
        print("This is child 1")
        
class Child2(Parent):
    def c2display(self):
        print("C2 Chilf ptoprtyy")
        
class Child3:
    def c3display(self):
        print("c3 display!!")
        
        
c1 = Child1()
c1.c1display()
c1.pdisplay()


c2 = Child2()
c2.c2display()
c2.pdisplay()