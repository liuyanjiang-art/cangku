# Week 2, Session 2: Task 2
# Simple Number Comparer

# Prompt the user to enter the numbers

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Use an if statement to compare the two numbers

if num1>num2: 
    print("The first number is bigger.")
elif num2>num1:  
    print("The second number is bigger.")
else:
    print("Both numbers are Equal.")
