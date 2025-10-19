# Week 4, Session 1: Task 1

# To convert a temperature from Celsius to Fahrenheit. There were two
#  main tasks involved:
#   (1) validating the temperature and
#   (2) converting Celsius to Fahrenheit.

# These are now defined in a separate function.

# Given the two functions and the following code to get the temperature
# from user, complete the rest of the program to use these functions to
# print the temperature in Fahrenheit if the temperature from the user
# is within the range, otherwise print "The temperature is out of range."



def valid_temperature(temperature):
    if temperature >= -100 and temperature <= 100:
        return True
    else:
        return False


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit



def run():
    celsius = float(input("Enter temperature in Celsius: "))
    y=valid_temperature(celsius)
    if y:
        x=celsius_to_fahrenheit(celsius)
        print(f'fahrenhit{x}')
    else:
        print('input again please')
run()

# Complete the rest of the code here