class MyClass:
    def __init__(self, name, usn):
        self.name = name
        self.usn = usn 
        
    def display_student(self):
        print(f"The Name is : {self.name} and usn is {self.usn}")
        
        
s1 = MyClass("Shreya", "CS001")
s1.display_student()