# 1. write a print statement to execute Hello World
a = "hello world"
print(a)
# 2. write a print statement for Boolean Expression
b = ["pikachu", "weasel"]
c = ["gravy", "potatoes"]
d = b
print(c is b)
print(b is d)
print(c is d)
# 3. write a print statement with logical operators ?
x = int(input('Enter your age: '))
if x < 21:
    print('You are too young, go away!')
else:
    print('Welcome, you are of the right age!')
# 4. Write a print Statement for creating a pattern programming like square,rectangle?
side = int(input("Please Enter any Side of a Square  : "))

print("Hollow Square Star Pattern")
for i in range(side):
    for j in range(side):
        if (i == 0 or i == side - 1 or j == 0 or j == side - 1):
            print('*', end='  ')
        else:
            print(' ', end='  ')
    print()

# 5. write a program to execute all even numbers?
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

for num in range(start, end + 1):

    if num % 2 == 0:
        print(num, end=" ")

# 6.write a program to reverse a string?
z = "hello world im jarvis"[::-1]
print(z)
# 7. write a program to check the length of a string?
ghj = "carpe diem"
print(len(ghj))
# 8. write a program to convert lowercase to uppercase?
q = " there is a bank holiday on monday"
print(a.upper)
# 9.write a program to differentiate the python numbers?
f = 3
h = 67853
g = 445.32
u = 2 + 6j
print(type(f))
print(type(h))
print(type(g))
print(type(u))
# 10.how can you use comments in a program? we use them to help others who are reading the code follow the trail of
# thought of the person who made any changes in any collaborative effort, by either using // or a hashtag you can
# place comments that do not interfere with the code

# 11. what are indentation errors? The indentation error can occur
# when the spaces or tabs are not placed properly.

# 12.is it necessary to add a string in Quotes and why? Python
# strings are sequences of characters and numbers. A string is wrapped around a set of single quotes or double
# quotes. There is no difference in which you use. it is a requirement otherwise it will register as a different type
# of function or maybe an indentation error

# 13.write a program to show index number of particular string?
text = "magic is so fun harry potter could use it forever"
result = text.index('is')
print(result)
qwe = "we are in a python class for our training"
print(qwe[8])
# 14 how can we use join() in string?
vegetables = ("rocket", "letice", "onion")
d = "-------".join(vegetables)
print(d)
# 15. what's the diff between capitalize() and Upper()? capitalize only capitalizes the first letter of each string
# depending on the code whereas upper actually capitalizes the entire string
# 16.use input() to show how can one can enter the value from terminal?
character = input("enter character name:")
print(character)
# 17.write a program to convert int to float and float to int ?
eee = 12
rrr = float(eee)
ttt = 13.0
yyy = int(ttt)
print(eee)
print(rrr)
print(ttt)
print(yyy)

