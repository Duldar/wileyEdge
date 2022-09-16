# 1. what are Data types in python?
# Numbers, String, List, Tuple, Dictionary
# 2.how to write append method in a program
u = [1, 2, 3, 4, 5, 6, 8, 7, 9]
o = [11, 12, 13, 14, 15, 16]
u.append(o)
print(u)
# 3. why lists are mutable?
# elements in the list can be changed and unordered with the help of append command they can be manipulated
# 4.difference between tuple and list?
# while the tuples are immutable objects the lists are mutable
# 5.how many methods are used in tuple?
# two built in methods that can be used on tuple
# 6.what's the difference in str and tuple?
# strings are made up of smaller strings, each containing one character
# whereas, tuples are made up of elements, which are values of any Python datatype
# 7.what's the use of pop() method?
# removes an item at the specified index from the list
# 8. what's the use of reverse()?
# reverses a list
# 9. how to reverse a list?
aaa = ["a", "b", "c", "d", "e"]
aaa.reverse()
print(aaa)
# 10.what is indexing?
# a way to refer the individual items within an iterable by its position
# 11. what is negative index and slicing?
# It returns the element that is numbered after the minus sign from the right-hand side of the list
# instead of the usual left-hand side
# in negative index the last element will not considered
# 12 : a = [1,2,3,4,5,6,7,8,9,10,11,1,2,12,15,20,21] out put for [:3]? [3:7] ? [:6]? [:]? [-8:-2]?
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1, 2, 12, 15, 20, 21]
print(list[:3])
print(list[3:7])
print(list[:4])
print(list[:6])
print(list[:])
print(list[::2])
print(list[-3:-8])
