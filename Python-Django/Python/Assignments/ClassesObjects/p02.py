class Student():
    def __init__(self,name,roll):
        self.name = name
        self.roll= roll
    def display(self):
        return (self.name, self.roll)

    def setAge(self,age):
        self.age = age
        return self.age

    def setMarks(self,marks):
        self.marks = marks
        return self.marks

s1 = Student('abc', 123)
print(s1.display())