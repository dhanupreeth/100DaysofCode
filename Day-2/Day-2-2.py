


# BMI Calculator
# wieght (kg)
# height (m)
# bmi = weight / height power of 2
# bmi = kg/m power of 2

print("Simple BMI Calcultor")
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
bmi = int(weight) / float(height) ** 2 # Converting the height into float type, in default it should be in string
result = int(bmi) # Converting the bmi into int to print the result as a rount number
print("Your Height is", height, "and your weight is", weight, "and your BMI is", result)



