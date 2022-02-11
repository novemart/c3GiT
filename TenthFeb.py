
# operator = '?'
#
# if (operator == '*') or (operator == '/') or (operator == '+'):
#     print("its star or slash")
#
# if '/':
#     print('yes')

#[0,1,2,3,4,5,6,7,8,9]
# for i in range(0, 10):
#     print("This is iteration number " + str(i+1))
#     print(i)
#
# a = 5
# b = 7
#
# c = a if a > b else b
#
# if a > b:
#     c = a
# else:
#     c = b
#
# print(c)
# age = 18
# print("I am " + str(age) + "years old", end='\n')
#
# print("I am", age, "years old", sep=' ')
#
# name = 'Martina'
# lastName = "O'Donnell"
#
# greeting = 'It\'s raining \t too bad'
# print(greeting)

#print("\U0001F600")
#print("\N{winking face}")
#import emoji
#print(emoji.emojize("Hello from :robot:"))

#name = "Martina"
# lastName = "Yusuf"
# name3 = name + lastName
# name3 = name3 + "?"
# print(name + " " + lastName)
#
# name2 = 'Martina' 'Yusuf'
# print(name2)

# print(name[3])
#
# for character in name:
#     print(character)

#strings are immutable
#name[3] = 'x'

# longString = """ This is going to be
# a super \t long string
# across multiple lines
# """
# print(longString)

greet = 'hello world'
# print(len(greet))
# print(greet.upper())
# print(greet*5)

# if 'a' in greet:
#     print("Contains letter 'a'")
# else:
#     print("Does not contain letter 'a'")
#

print(greet[1:4])
print(greet[-3:-1])
print(greet[0:12:2])
print(greet[:6])
print(greet[7:])
#creates a copy
print(greet[:])


number_input = "1,34,7,98,345"
number_list = number_input.split(",")
print(number_list)
weird_string = '-'.join(number_list)
print(weird_string)


# url = "localhost:8080/user/id"
# url_list = url.split("/")


