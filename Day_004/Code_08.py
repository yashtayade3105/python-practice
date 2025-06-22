# bmi calculator

name  = input("Enter your name : ")
weight = float(input("Enter your weight in kg : "))
height = float(input("Enter your height in meters : "))
bmi = weight / (height ** 2)
print(f"Hello {name}, your BMI is : {round(bmi, 2)}")
