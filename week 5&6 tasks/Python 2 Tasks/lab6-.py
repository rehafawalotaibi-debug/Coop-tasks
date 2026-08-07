x, y = 6, 4
print("Addition (x + y):", x + y)
print("Subtraction (x - y):", x - y)
print("Multiplication (x * y):", x * y)
print("Division (x / y):", x / y)
print("Exponentiation (x ** y):", x ** y)
print("Floor Division (x // y):", x // y)
print("Modulus (x % y):", x % y)
print("\n#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

a = True
b = False
print("x > 4 and x < 10:", x > 4 and x < 10)
print("x > 3 or x < 3:", x > 3 or x < 3)
print("not (x > 3 or x < 3):", not (x > 3 or x < 3))
print("\n#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

val = 4
val += 3
val *= 3
print("Assignment result after += and *=:", val)
print("\n#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

list1 = ["python", "c++"]
list2 = ["python", "c++"]
ref_list = list1
print("list1 is ref_list:", list1 is ref_list)
print("list1 is list2 (different memory objects):", list1 is list2)
print("\n#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

num1 = 60
num2 = 13

res_and = num1 & num2
res_or = num1 | num2
res_xor = num1 ^ num2

print("Bitwise AND (60 & 13):", res_and)
print("Bitwise OR (60 | 13):", res_or)
print("Bitwise XOR (60 ^ 13):", res_xor)
print("Bitwise NOT (~60):", ~num1)
print("Left Shift (60 << 2):", num1 << 2)
print("Right Shift (60 >> 2):", num1 >> 2)
