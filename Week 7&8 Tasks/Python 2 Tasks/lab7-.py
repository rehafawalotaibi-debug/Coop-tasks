# Making Choices and Decisions
# If Statement
a = 60
b = 40
if a > b:
    print("a is bigger than b")
print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

# If - Else Statement
a = 40
b = 60
if b > a:
    print("b is greater than a")
else:
    print("a is greater than b")
print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

# If - Elif - Else Statement
a = 60
b = 40
if b > a:
    print("b is greater than a")
elif b < a:
    print("b is smaller than a")
else:
    print("a and b are equal")
print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

# Nested If
n = 10
if n >= 0:
    if n == 0:
        print("zero")
    else:
        print("Positive number")
else:
    print("Negative number")
print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

# Logical Operator: and
a = 60
b = 40
c = 20
if a > b and a > c:
    print("a is greater than other num")
print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

# Logical Operator: or
a = 60
b = 40
c = 20
if b > a or b > c:
    print("At least one of the conditions is True")
print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

# Logical Operator: not
a = 60
b = 40
c = 20
if not (b > a):
    print("a is greater than b")
print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

# For Loop with List
x = [1, 2, 3, 4, 5, 6]
for i in x:
    print(i)
print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

# For Loop with String
x = "python"
for i in x:
    print(i)
print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

# For Loop with range()
for i in range(5):
    print(i)
print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

# range() with Start and End
for i in range(2, 8):
    print(i)
print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

# range() with Start, End and Step
for i in range(2, 20, 4):
    print(i)
print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

# Nested For Loop
x = ["python", "c++"]
for i in range(2, 10, 4):
    for n in x:
        print(i, n)
print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

# Another Nested For Loop
m = [1, 2, 3]
n = [1, 2, 3]
for i in m:
    for j in n:
        print("(", i, j, ")")
print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

# If Statement inside For Loop
m = [1, -2, 3, 0, -4]
for i in m:
    if i > 0:
        print(i, "is a positive")
    elif i == 0:
        print(i, "is a zero")
    else:
        print(i, "is a negative")
print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

# While Loop
x = 2
while x <= 10:
    print(x)
    x += 2
print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

# While Loop with Else
x = 2
while x < 10:
    print(x)
    x += 2
else:
    print("x is no longer less than 10")
print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

# Break inside For Loop
num = [1, 2, 3]
for x in num:
    if x == 2:
        break
    print(x)
print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

# Break inside While Loop
x = 2
while x < 10:
    print(x)
    if x == 4:
        break
    x += 2
print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

# Continue inside For Loop
num = [1, 2, 3]
for x in num:
    if x == 2:
        continue
    print(x)
print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

# Continue inside While Loop
x = 2
while x < 10:
    x += 2
    if x == 8:
        continue
    print(x)
print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

# Pass inside For Loop
x = {"p", "a", "y", "t", "h", "o", "n"}
for i in x:
    pass
print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

# Pass inside If Statement
x = 10
y = 20
if y > x:
    pass
