name = "Yash"            # str
age = 20                 # int
height = 5.9             # float
is_student = True        # bool
demo = None              # NoneType
com = 1 + 2j            # complex

# list
fruits = input("Enter the list of fruits separated by commas : ")
fruits = fruits.split(",")
print("Fruits list:", fruits)

# Tuple
# Tuple is immutable
fruits_tuple = tuple(fruits)
print("Fruits tuple : ", fruits_tuple)

# Dictionary
fruits_Dict = {fruit: len(fruit) for fruit in fruits}
print("Fruits dictionary:", fruits_Dict)
# Re-assigning with different type (dynamic typing)
# name = 100

print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of height", type(height))
print("Type of is_student:", type(is_student))
print("Type of demo:", type(demo))
print("Type of com:", type(com))
print("Value of name:", name)
print("Value of age:", age)
print("Value of height:", height)
