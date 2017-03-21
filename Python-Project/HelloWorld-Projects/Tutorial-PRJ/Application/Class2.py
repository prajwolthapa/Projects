# Creating Class
import string
import datetime

class Employee:
    number_employee = 0
    raise_amt =1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.number_employee +=1

    def fullname(self):
        return  self.first +' '+ self.last

    def pay_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        return  self.pay


# Class method and Decorator(Class method passes cls as the first argument)
    @ classmethod
    def setraise_amount (cls,amt):
        cls.raise_amt =  amt

    @ classmethod
    def breakString(cls,data):
        cls.first,cls.last ,cls.pay = data.split('-')
        return  cls.first,cls.last,cls.pay

# Static Method (they dont pass anything as the first argument (No instance or the class))
    @ staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday()==6:
            return False
        return True





# Python Inhertence and Subclassess

class developer(Employee):
    def __init__(self,first,last,pay,language):
        super().__init__(first,last,pay)
        self.language = language




#
# my_date = datetime.date(2016,7,11)
# print(Employee.is_workday(my_date))





emp1 = developer('Prajwol','Thapa',20000,'Python')
print (emp1.language)
# emp2 = Employee('RJK','TRK',25)
# emp2.raise_amt = 1.09
# print(Employee.number_employee)
# print(emp2.pay_raise())
# print(emp1.__dict__)
# emp_str1 ='Prajwol-Thapa-1000'
# emp_str2 = 'Ojashri-Thapa-2000'