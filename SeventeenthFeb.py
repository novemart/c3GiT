# num = 0
# while num != 5:
#     num = int(input("Give me a number: "))
#ordered but immutable
# my_tuple = 4, 6, 8, 3
# print(my_tuple[1])
#
# a = 5
# b = 6
# a, b = b, a
#
# val1, val2, val3 = (2, 3, 4)
# print(val1, val2, val3)
#
# #overloaded operator
# print(my_tuple*3)
#
# #trailing comma
# my_single_item = ("hello",)
# print(type(my_single_item))
#
# #!!error
# #my_tuple[1]= 7
#
# #ordered mutable
# my_list = [1, "hello", [1, 2, 3], ["apples", "oranges"]]
# print(my_list[3][1])
#
# my_tuple = (1, 2, 4, 7, 8)
# a, b, *c = my_tuple
# print(c)
# print(type(c))
#
# my_list = ['apples', 'oranges', 'bananas']
# #adding to the left hand side
# my_list[:0] =['milk', 'bread']
# print(my_list)
#
# #adding at the back
# my_list.append("bacon")
# print(my_list)
#
# my_list.extend(['cheese','biscuits'])
# print(my_list)
#
# my_list = my_list + ['chocolate', 'butter']
# # myvar += 1 <=> myvar = myvar+1
# my_list += ['fish', 'oil']
# print(my_list)
#
#
# my_list.insert(3, 'bird feed')
# print(my_list)
#
#
# #my_list[4]='juice'
# my_list[4:4] = ['juice']
# print(my_list)


# my_list.pop()
# print(my_list)
#
# popped_item = my_list.pop(3)
# print(my_list)
# print(popped_item)
#
# my_list.remove('milk')
# print(my_list)

# my_list.remove('milk')
# print(my_list)
# print("********************")
# my_new_list = sorted(my_list)
# print(my_new_list)
# print(my_list)
#
# #sort in place
# my_list.sort()
# print(my_list)

#unordered only unique elements
# my_set = {3, 6, 3, 7, 8, 2, 46, 8, 3, 9}
# print(my_set)
#
# my_set.add(18)
# print(my_set)
#
# my_set.add(3)
# print(my_set)
#
# my_set.remove(46)
# print(my_set)

# my_dict ={
#     'UK': ['London', 'Leeds', "Glasgow"],
#     'US': ['New York', 'Boston', 'Miami']
# }
#
# print(my_dict)
#
# my_dict['FR'] = ['Paris', 'Nice', 'Toulouse']
# print(my_dict)
#
# for country in my_dict.keys():
#     print(my_dict[country])
#
# for k,v in my_dict.items():
#     print(k)
#     print(v)

#x - create and open
opened_file = open('myFile.txt', 'r+')
# content = opened_file.read()
# print(content)

for line in opened_file:
    print(line, end="")

opened_file.write("hello from python")


opened_file.close()