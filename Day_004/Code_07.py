"""
# Convert temperature form c to f
# input
c = float(input("Enter the temeperature in celcius : "))
# calculation
f = (c * 9/5) + 32
print(f"THe temperature in fahrenheit is : {f}")
# another way
print(f"{c} 'c = {f} 'f")
"""

# conver temperature form f to c
# input
f = float(input("Enter the temperature in fahrenheit : "))
c = (f - 32) * 5/9
print(f"The temperature in celcius is : {c}")
# another way
print(f"{f} 'f = {c} 'c")

# program to  convert temperature form c to k
# inpt
c = float(input("Enter the temperature in celcius : "))
# calculation
k = c + 273.15
print(f"The temperature in kelvin is : {k}")
