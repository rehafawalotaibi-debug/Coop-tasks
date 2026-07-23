
#Tuple definition (with or without parentheses).
mytuple = ("python", "c++", "c", "java")
print(mytuple)

mytuple2 = "python", "c++", "c", "java"
print(mytuple2)
print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

# Accessing elements via indexing.
x = ("python", "c++", "c", "java")
print(x[1])
print(x[-1])
print(x[1:3])
print(x[-4:-1])
print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

#Checking type using type() function and difference between string and tuple.
x_type = ("python", "c++", "c", "java")
print(type(x_type))

x_str = ("python")
y_tuple = ("python",)
print(type(x_str))
print(type(y_tuple))
print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

#Tuple containing a list and converting a tuple to a list.
x_list_inside = ("python", "c++", [1, 2, 3])
print(type(x_list_inside))
print(x_list_inside)

x_to_convert = ("python", "c++")
y = list(x_to_convert)
print(y)
print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

#Finding the length of a tuple using the len() function
x_len = ("python", "c++")
print(len(x_len))
print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
# 6. Attempting modification or deletion (generating errors to prove that tuples are immutable)
# x = ("python", "c++")
# x[1] = "c"  # TypeError: Occurs when trying to modify an element inside a tuple because tuples are immutable
# del x
# print(x)    # NameError: Occurs when trying to print a variable that has been completely deleted

#Joining tuples
tuple1 = ("python", "c++")
tuple2 = ("c", "java")
tuple3 = tuple1 + tuple2
print(tuple3)
print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

#Using the constructor (tuple())
x_constructor = tuple(("python", "c++", "c", "java"))
print(x_constructor)
print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

#Sets (curly brackets {})
x_set = {"python", "c++", "c", "java"}
print(x_set)
print(type(x_set))
print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

#Set content and avoiding duplicates
x_mixed = {"hello", 604, (1, 2, 3)}
print(type(x_mixed))
print(x_mixed)

# x_err = {["python", "c++"], 604, (1, 2, 3)}  # TypeError: Occurs because set elements must be hashable and do not accept lists

x_duplicates = {"python", "c++", "c", "java", "c++", "c"}
print(x_duplicates)
print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

#Checking for the existence of an element using (in)
x_check = {"python", "c++", "c", "java"}
print("java" in x_check)
print("SQL" in x_check)
print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

#Set functions (add, len, remove, pop, clear, del)
x_func = {"python", "c++", "c"}
x_func.add("java")
print(x_func)
print(len(x_func))

x_func.remove("c")
print(x_func)

x_pop_example = {"python", "c++", "c", "java"}
print(x_pop_example.pop())
print(x_pop_example)

x_func.clear()
print(x_func)

# del x_func
# print(x_func)  # NameError: Occurs when trying to access a set that has been deleted from memory
print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

#Set union and update
set1 = {"python", "c++"}
set2 = {"c", "java"}
set3 = set1.union(set2)
print(set3)

set_x = {"python", "c++"}
set_y = {"c", "java", "c++"}
set_x.update(set_y)
print(set_x)
print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

#Frozen sets (frozenset)
x_frozen = frozenset({"python", "c++"})
print(type(x_frozen))
# x_frozen.remove("c++")  # AttributeError: Occurs when trying to use a method that is not available or not allowed on this data type (such as modifying a frozenset)




