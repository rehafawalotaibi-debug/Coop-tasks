cars = {}
print("Type of cars:", type(cars))
print("\n#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

cars = {"brand": "BMW", "year": "1964"}
print("Cars Dictionary:", cars)
print("Length of cars:", len(cars))
print("\n#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

nums = {1: "one", 2: "two", 3: "three"}
print("Value of key 1 (indexing):", nums[1])
print("Value of key 2 (get):", nums.get(2))
print("Keys:", nums.keys())
print("Values:", nums.values())
print("\n#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

nums[1] = "ten"
nums[4] = "four"
print("After update and add:", nums)

removed_val = nums.pop(2)
print("Popped value (key 2):", removed_val)

random_item = nums.popitem()
print("Popped item:", random_item)

del nums[3]
print("After deleting key 3:", nums)
print("\n#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

print("Is 1 in nums?", 1 in nums)
print("Is 5 in nums?", 5 in nums)
print("\n#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

nested_nums = {
    "intnum": {1: "one", 2: "two"},
    "floatnum": {1: "1.0", 2: "2.0"}
}
print("Nested Dictionary:", nested_nums)
print("\n#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

user = dict(name="ahmed", age="25")
print("Dict Constructor result:", user)
