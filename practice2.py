# import modules
# name = input('What is your name? ')
# modules.displayingMsg(name)

# import modules
# name = input('What is your name? ')
# modules.cfo_name(name)

# from practice import add,subtract,multiply,divide,modulus

# a = int(input('Enter the first number : '))
# operator = input(" Select an operator : +,-,/,%,* ")
# b = int(input('Enter the second number : '))

# # print("Answer: ", add(a,b))

# if operator == '+':
#     print("Answer: ", add(a,b))
# elif operator == '-':
#     print("Answer: ", subtract(a,b))
# elif operator == '*':
#     print("Answer: ", multiply(a,b))
# elif operator == '/':
#     print("Answer: ", divide(a,b))
# elif operator == '%':
#     print("Answer: ", modulus(a,b))
# else:
#     print('input vaild operator')


# class Animal:
#     kind = 'mammal'
#     tail = 'yes'
# a = Animal().kind
# print(a)
# print(Animal().tail)
# print(type(a))

# class Person:
#     Person_props = {
#         "name": "Blard",
#         "job": "senior dev",
#     },
#     edu = ['ssce','bsc','msc']
#     def this_is_a_method(self):
#         return self.edu

# person1 = Person()
# print(person1.Person_props , type(person1.Person_props))
# print(person1.edu, type(person1.edu))

# print(person1.this_is_a_method())

# class Animal:
#     def __init__(self,kind,color):
#         self.kind = kind
#         self.color = color
# dog = Animal('Dog','white')
# print(dog.kind)
# print(dog.color)


# class programming:
#     def __init__(self,a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c

# lang = programming('javascript','python','java')
# print(lang.c)
# #class is a parent class that implements and shares all available info to other functions
class Animal:
    def __init__(self,kind,color):
        self.kind = kind
        self.color = color
    def printAnimal(self):
        x  = f"{self.kind} is a domestic animal with {self.color} fur"
        print(x)
    def action(self) :
        return f"{self.kind} is running"  
     
dog = Animal('Dog','white')
dog.printAnimal()
print(dog.action())

rat = Animal('Rat','black')
print(rat.kind)
rat.printAnimal()
print(rat.action())

# # super class inheritance all parent classes e.g below

class Mammal(Animal):
    def __init__(self,kind,color,tail):
        super().__init__(kind, color)
        self.tail = tail
    def farm(self):
        x = f"{self.kind} is a domestic animal with {self.color} fur, with a {self.tail}"
        print(x)
cow = Mammal('cow','black',"long")
cow.farm()

# clear up d person class to look like d animal class, you can retain name nd job
# the child classs (individual) should be d superclass .. should hav 2 parameters ..... namely language 1 and lang 2
#create a function .. that says blard is a senior developer and he write jVscript and python.
#name , languages , job should be a parameter


class Persons:
    def __init__(self,name,job):
        self.name = name
        self.job = job
        
    def info(self):
        print(f"{self.name} {self.job}")
        
x = Persons("oyin","ibee")
x.info()

class individual(Persons):
    def __init__(self, name, job,lang,lang2):
        super().__init__(name, job)
        self.lang = lang
        self.lang2 = lang2
    def info(self):
        return f"{self.name} is a {self.job} and  he write {self.lang} and {self.lang2}"
    
personinfo = individual('Blard','senior dev','python',"java")
print(personinfo.info())


# arbituary argument. you don't need to specify the number of arguments
# a function that take more than 1 argument and return it 
def addnos(*args):
    print(args)
addnos(1,2,3,4,5)

def addnos(*args):
    print(type(args))
    total = 0
    for num in args:
        total += num
    return total
add_num= addnos(1,2,3,4,5)
print(add_num)
