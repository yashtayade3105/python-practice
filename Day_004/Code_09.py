# program to calculate the age
# input
name = input("Enter your name : ")
print(f"Hello {name}, welcome to the age calculator program!")
print(f"{name} your interested to calculate your age if yes press \'y\' or if no press \'n\'")
choice = input("Enter your choice : ")
if(choice=='y'):
    year_of_birth = int(input("Enter your year of birth : "))
    current_year = int(input("Enter the current year : "))
    age = current_year - year_of_birth
    print(f"{name} your age is : {age}")
else:
    print(f"{name} you are not innterested to calculate your age.")
    print("Thank you have a nice day!")
        

