# don't change any function name write you all code inside the function only for every question solution and return you output as mentioned in problem statement.

# question_first_solution
class Circle():
    def __init__(self,radius):
      self.radius = radius
      self.pi = 3.14159265359
      
    def getArea(self):
        self.area = self.pi * self.radius ** 2
        return round(self.area, 1)

    def getCircumference(self):
        self.circumference = 2 * self.pi * self.radius
        return round(self.circumference, 1)
    
    def Display(self):
        return [str(self.getArea()) + '0', str(self.getCircumference()) + '0']

# question_second_solution
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

# question_third_solution
class Temperature():
    def convertFahrenhiet(self,celsius):
        self.farenheit = str((celsius * 9/5) + 32) + '0'
        return self.farenheit

    def convertCelsius(self,farenhiet):
        self.celsius = str((farenhiet - 32) * 5/9) + '0'
        return self.celsius

# question_fourth_solution:
class Subset:
    def sub_sets(self, sset):
        return self.subsetsRecur([], sorted(sset))
    
    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]

# question_fifth_solution:
class Sum:    
    def twoSum(self, nums, target):
        temp = [val for val in nums if val <= target]
        indices = []

        for idx in range(len(temp)):
                for idy in range(idx, len(temp)):
                        tI = []
                        if temp[idx] + temp[idy] == target:
                                tI.extend([idx, idy])
                                indices.append(tuple(tI))

        indices = sorted(indices, key=lambda x: x[1])
        return indices

# question_sixth_solution:
class SumEqualsZero:
    def threeSum(self, nums):
        # Write you code here
        pass

# question_seventh_solution:
class RomanToInt:
    def roman_to_int(self, s):
        # Write you code here
        pass

# # question_eighth_solution:
class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        # Write you code here
        pass

    # question ninth Solution:
    def withdraw(self, amount):
        # Write you code here
        pass

# question tenth solution:
class MinimumBalanceAccount(BankAccount):
    def __init__(self):
        BankAccount.__init__(self)
        self.minimum_balance = 5000

    def withdraw(self, amount):
        # Write you code here
        pass
