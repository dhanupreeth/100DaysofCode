# Printing a string
print("devops")

# printing a string with concatenate, with multiple methods
print("dev " + "ops") # space in the firs string
print("dev" + " ops") # space in the second string
print("dev" + " " + "ops") # space btw the two string

# Getting the input from user and printing the value
user_name = input("Enter your name to be print:\n") # \n is used for second line, the cursor need to wait or blink
print(user_name) # without quotes because this is not string this is variable name for user input
print("Verify your name: ", user_name)

# length of your name
length = len(user_name)
print("Your Name length is: ", length)

#input function is the print statement
print("Hello " + input("Which Course your are contributing for 100 Ddays of Code:\n"))

# Generating a Band Name
print("Welcom to Band Name Generator\n") # greeting msg for band name generator
city = input("What's your city name?\n") # city variable 
course_name = input("Which langugae you're learing?\n") # course_name variable
print("Your Band Name is", city, course_name) # Concatenate method 1
print("Your Band Name is " + city + " " + course_name)  # Concatenate method 2
print("Yout Band Name is" + " " + city + " " + course_name)  # Concatenate method 3