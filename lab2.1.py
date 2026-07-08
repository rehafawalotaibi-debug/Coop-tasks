#String Indexing & Slicing. 
text = "python"
print(text[0])      
print(text[2:5])    
print(text[-3:-1])  
print(text[:3])     
print(text[-2:])
print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
#String Length.
print(len(text))
print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

#str Manipulation.
s = "Hello Python"
print(s.lower())      
print(s.upper())      
print(s.swapcase())   
print(s.title())      
print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
#Search & Replace.
print(s.find("my"))   
print(s.replace("Python", "World"))

print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
#Splitting & Partitioning.
text2 = "hello python!"
print(text2.split())  
print("I could eat eggs all day".partition("eg"))

print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
#Checking Content.
print("12345".isdigit()) 
print("hadeel".islower())
print("MY NAME".isupper())
print("MY NAME".startswith("MY"))

print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
#Formatting & Joining.
words = ["name", "age", "country"]
print(":".join(words))
print("My name is {}".format("Hadeel"))
print("66".zfill(10))
print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
#More Formatting Types.
print("I have {:,}".format(3000555666)) 
print("Binary of 5 is {:b}".format(5))  
