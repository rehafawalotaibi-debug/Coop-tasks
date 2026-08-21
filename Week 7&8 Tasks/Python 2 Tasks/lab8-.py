# Try and Except
try:
    print(x)
except:
    print("Something went wrong")

print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

# Function
def my_function():
    print("hello python")

my_function()

print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

# Function with Parameter
def my_function(name):
    print("My name is " + name)

my_function("hadeel")

print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

# Function with List
def my_function(lang):
    for x in lang:
        print(x)

pro_lang = ["python", "c++", "c"]
my_function(pro_lang)

print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

# Function with Dictionary
def my_function(mon):
    months = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }
    print(months[mon])

my_function("May")

print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

# Function with Different Data Types
def my_function(my_collection):
    for x in my_collection:
        print(x)

dic = {1: "Admin", 2: "Editor", 3: "Reader"}
tup = ("a", "b", "c")
str1 = "hadeel"
lis = [23, 64, 12]

my_function(dic)
my_function(tup)
my_function(str1)
my_function(lis)

print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

# Return
def my_function(x):
    return 10 * x

print(my_function(2))
print(my_function(4))
print(my_function(6))

print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

# Built-in Function
print(abs(-1))
print(abs(2))
print(abs(-3))

print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

# User-defined Function
def my_abs(x):
    if x >= 0:
        print(x)
    else:
        print(-x)

my_abs(-1)
my_abs(2)
my_abs(-3)

print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

# Function with pass
def myfunction():
    pass

myfunction()

print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

# Recursion - Factorial
def my_fact(n):
    if n == 1:
        return 1
    else:
        return n * my_fact(n - 1)

x = 6
print("The factorial of", x, "is:", my_fact(x))

print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

# Recursion - Sum
def sumofn(n):
    if n == 1:
        return 1
    else:
        return n + sumofn(n - 1)

print(sumofn(2))
print(sumofn(6))
print(sumofn(10))

print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

# Lambda
b = lambda a: a + 10
print(b(6))

print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

# Lambda with Two Arguments
x = lambda a, b: a + b
print(x(5, 5))

print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

# Lambda inside Function
def my_function(b):
    return lambda a: a * b

x = my_function(10)
print(x(20))
