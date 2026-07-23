#Define variables (int, float, complex).
x = 5
y = 4.5
z = 4 + 6j

#Check the variable type using the type() function.
print(type(x)) 
print(type(y)) 
print(type(z))
print("\n#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

#Arithmetic operations.
x = 5 + 6
y = 4.0 + 5.0
z = 4 + 6j + 1 + 4j
print(x)  
print(y)  
print(z) 
print("\n#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

#Type Conversion.
x = 5
y = 4.5
x = float(x)  
y = complex(y)
print(x)  
print(y)
print("\n#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

#Generate random numbers using the random.
import random
print(random.randrange(1, 10))
print(random.randrange(1, 10))
print("\n#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

#Simple comparisons returning True or False.
print(10 > 9)   
print(10 == 9) 
print(10 < 9)  
print("\n#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

#Evaluate values using the bool() function.
print(bool("python"))  
print(bool(10))        
print("\n#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

#Special cases that evaluate to False in the bool() function.
print(bool(()))   
print(bool([]))    
print(bool({}))    
print(bool(0))     
print(bool(""))    
print(bool(False)) 
print(bool(None))
print("\n#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

#Define a list.
mylist = ["python", "c++", "c", "java"]
print(mylist)
print(mylist[0])  
print(mylist[1])  
print("\n#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

#Clear all elements and make the list empty using clear().
mylist.clear()
print(mylist)
print("\n#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

#Concatenate two lists using the (+) operator.
list1 = ["python", "c++"]
list2 = ["c", "java"]
list3 = list1 + list2
print(list3)  
print("\n#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

#Merge and extend a list with another using the extend() method.
list1 = ["python", "c++"]
list2 = ["c", "java"]
list1.extend(list2)
print(list1) 
