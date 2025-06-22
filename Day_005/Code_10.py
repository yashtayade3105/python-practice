# Take user input and check its type using eval()
data = input("Enter any value (e.g. 100,'Hello')")

try:
    evaluated = eval(data)
    print(f"You entered: {evaluated}")
    print(f"Type of the entered value: {type(evaluated)}")
except Exception as e:
    print(f"Error evaluating input: {e}")
    print("Please enter a valid Python expression.")    
