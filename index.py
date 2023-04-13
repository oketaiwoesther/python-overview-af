name = "jane"
print(name)

age = 8
afloat = 7.9
#boolen
isTrue = True
print(name +" is " + str(age) +" years old")
print(age+afloat)

x =3
y = 78
z = 78
x += 4
print(x)
# comparison operators
print(x==y)
print(x>y)
print(z>y)
print(z >= y)

# logical operators and,or,not operators
print(z > x and y == z)
print(z < x and y == z)
print(z < x or y == z)  
print(z > x and y == z and x==y) # in and (any false retuen false values)
print(not(z < x and y == z))   #the not convert the values to opposite values

print(x is y) 

# myName = input("What is the name? ")
# myAge = input("How old are you? ")
# print(f'My name is {myName} and myAge is {myAge}')

#list
cars =['Mercedes','Honda','BMW','Range Rover','Acura','Audi']
designer = ['Gucci','Ysl','lv','D&G','Zara']
print(cars[2])
"""print(cars[2:])


'''
to change the value of the specific item refer to the index number
to change the values of item within a specific range def a list with the new values and refer to the range of index numbers 
where you want to insert the new values
if you insert more items than you replace, the new items will b inserted where you specified,and the remaining items will move accordingly.
insert a new list items without replacing any of the existing values we can use the insert method
'''

print(cars[2])
print(cars[2:])
print('=======answer============')
cars[3] ='polestar'
print(cars)
cars[4:5 ] = ['tesla','nore','nord']
print(cars)

cars.insert(5,'porche')
print(cars)

"""

#  function
def greet(name):
    print(f'Hello {name}')
greet('Darksied')

def hello(a,b):
    name = 'Hafeez'
    job =  'PM'
    me = f'{name} is the {job} for tSa'
    return f'{me} he has {a} years to experience in {b}'
print(hello(4,'Web Developer'))


# name = input('What is the name?')
# def intro():
#     name = input('Enter your name? ')
#     if name :
#         print(f'Hello, {name}')
#     else:
#         print('Hello unknown user')
# intro()

# Dicitonary
me = {
    'name': 'Oyin',
    'gender': 'them',
    'laptop': False
}
print(me)
print(me['name'])
print(me.get('gender'))
# using keys
a = me.keys()
print(a)

me['twitter'] = '@damola'
me.update({'weight': 40})
print(me)

if 'twitter ' in me:
    print('I have twitter account')
    
# create a rock, paper and scissor game using while loop,elief ,continue and break.
# import random

# while True:
#     dice = ['rock', 'paper', 'scissor']
#     computer = random.choice(dice)
#     playerU = input('Enter (rock, paper, scissor): ')
#     print(f'User : {playerU} vs computer : {computer}')
#     if playerU == 'quit':
#         print("BYE👋👋👋!")
#         break
#     if computer == playerU:
#         print(f'Both played {playerU} 😂!')
#         continue
#     elif playerU == 'rock' and computer == 'scissor':
#         print('Rock beats scissor.')
#         break
#     elif playerU == 'paper' and computer == 'rock':
#         print('Paper beats rock.')
#         break
#     elif playerU == 'scissor' and computer == 'paper':
#         print('Scissor beat paper.')
#         break
#     else:
#         print('You lose😢😜Try again.')


# import modules
# name = input('What is your name? ')
# modules.displayingMsg(name)


'''
from modules import add, subtract, divide, multiply,modulus

a = int(input('Enter the first number : '))
operator = input("Select an operator : '+', '-', '/','*','%': ")
b = int(input('Enter the second number : '))

# print('Answer: ', add(a,b))

if operator == '+':
    print('Answer: ', add(a,b))
elif operator == '-':
    print('Answer: ', subtract (a,b))
elif operator == '*':
    print('Answer: ', multiply (a,b))
elif operator == '/':
    print('Answer: ',divide(a,b))
elif operator== '%':
    print('Answer: ',modulus(a,b))
else:
    print('input valid operator')   
    
'''


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

'''1)create a quiz app,create an introdcutory message that says welcome to the quiz.
2)create an input that can ask you if you are interested the game or not
3)if you click on yes the game should proceed and ask the first qst
qsts-name of this bootcamp(ensure to be case sensitive)
-name of course offered 
-who created python
add two more qsts of your choice to make it 5
if answer is correct then add a point and  have a total score and also print the total scores  in % 
(3/5)*100'''   

score = 0
run = True
print("WELCOME!")
while run:
    answer = input("Would you like to play this challenge? (yes/no): ")
    if answer.lower() == "yes":
        question1 = input("1) What is the capital of Nigeria?: ")
        if question1.lower() == "abuja":
            score += 1
            print("Correct! Your score is:", score)
        else:
            print("Incorrect.")
        question2 = input("2) The capital of the Lagos is :")
        if question2.lower() == "ikeja":
            score += 1
            print("Correct! Your score is:", score)
        else:
            print("Incorrect.")
        question3 = input("3) Nigeria adopted what currency in 1973? :")
        if question3.lower() == "naira":
            score += 1
            print("Correct! Your score is:", score)
        else:
            print("Incorrect.")
        question4 = input("4)What is the official language in Nigeria?")
        if question4.lower() == "english":
            score += 1
            print("Correct! Your score is:", score)
        else:
            print("Incorrect.")
        question5 = input("5) How many colors are there in a rainbow?:")
        if question5.lower() == "12":
            score += 1  
        total = score
        print("Your score is:",total)
        print("Your total percentage is:",(total/5)*100)
        run = False      
    elif answer.lower() == "no":
        print("Bye for now.")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")