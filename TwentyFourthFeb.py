# def addition(num1, num2):
#     print(num1)
#     print(num2)
#     return num1+num2
#
#
# def print_menu():
#     print('Welcome to The calculator')
#     print('Hope you\'ll have fun')
#
#
# def subtraction(num1, num2):
#     return num1-num2
#
# result = addition(3, 4)
# print('The result is', result)
#
# print_menu()
# result = addition(7, 8)
# print('The result is', result)
#
#
# print_menu()
# val1 = int(input('Type in the first number: '))
# val2 = int(input('Type in the second number: '))
# result = addition(val1, val2)
# print('The result is', result)
#
#
# choice =''
# while choice != 'X':
#     val1 = int(input('Type in the first number: '))
#     val2 = int(input('Type in the second number: '))
#     result = subtraction(val1, val2)
#     print('The result is', result)
#     choice = input('Again?')

#global scope
# var1 = 'Martina'
#
#
# def print_greeting(name):
#     #local scope
#     myLocalVar = 'Hey'
#     print(myLocalVar, name)
#
# #print(myLocalVar) this is a local variable not available outside of the function
# print_greeting('John')


# def change_list(myList):
#     myList[0] = 'Martina'
#
# listOfNames = ['John', 'Joe', 'Jim']
# print(listOfNames)
# change_list(listOfNames)
# print(listOfNames)
#default parameter
# def calculateVat(price, tax=0.195):
#     return price*tax
#
#
# table = 20
# print(calculateVat(table))
#
# wine = 5
# print(calculateVat(price=wine, tax=0.25))
#
# chair = 15
# print(calculateVat(tax=0.20, price=chair))

#the star enforces naming of the parameters when calling the function

# def division(param1, *, num1, num2):
#     print(param1)
#     return num1/num2
#
# print(division(4, num1=5, num2=7))
#
# print('Hello', 'World', 'How', 'Are', 'You', sep='?')
# def my_func(a, b, c):
#     print(a)
#     print(b)
#     print(c)
#
#
# def my_func2(a, *b):
#     print(a)
#     print(b)
#
#
# myTuple = (1, 2, 3)
# # a, *b = myTuple
# # print(a)
# # print(b)
# my_func(*myTuple)
#
# my_func2(1, 2)
# my_func2(2, 3, 4, 5, 67, 8, 8, 9, 6)

# def my_func3(**kwargs):
#     for k, v in kwargs.items():
#         print(k)
#         print(v)
#
# my_func3(name='Martina',surname='Yusuf')

# def multiplication(num1, num2):
#     return num1*num2
#
# def my_func4():
#     myDictionary ={'name': 'Martina', 'surname':'Yusuf'}
#     return myDictionary
#
#
# def add(num1, num2):
#     ans = str(round(float(num1) + num2, 2))
#     num1s = str(num1)
#     num2s = str(num2)
#     calc = [num1s, '+', num2s, '=', ans]
#     return ans, calc
#
#
# result, myList = add(3,6)
# print('Result', result)
# print('MyList', myList)
#global variable
# var1 = 'Martina'
#
#
# def print_greeting(name):
#     #local variable
#     greeting = 'Hey'
#     #local variable
#     global var1
#     var1 = 'Santa'
#     print(greeting, name, 'from', var1)
#
# print_greeting('John')
# print(var1)

def addition(num1, num2):
    return num1+num2


def addOne(x):
    return x+1

#lambda num1,num2 : num1+ num2

myList=[1, 2, 3, 4, 5, 6]

myNewList = list(map(addOne, myList))
#myNewList = list(map(lambda x:x+1, myList))
print(myNewList)