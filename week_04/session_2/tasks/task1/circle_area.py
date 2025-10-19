# Week 4, Session 2: Task 1

# Define a function circle_area that takes 2 arguments:
#   (1) radius and
#   (2) pi_value 
#   
#   The function returns the area of a circle. The argument pi_value
#   is optional. The formula for the area of a circle is
#   area = pi * radius * radius.

# Your task is to complete the definition of the function, and set a
# default value to the optional argument pi_value. You can set it to
# either (1) 3.14, (2) 3.142, (4) 3.1428, or (4) 3.142857 and observed
# the output produced the the function is used.


def circle_area(radius, pi_value=3.1416):  # assign a default value to pi_value
    # complete the code here
    area = pi_value * radius * radius
    return area


# Check if correct output is produced
print(circle_area(2))
print(circle_area(5))
print(circle_area(22.5))

# For those knowing how to import a module, you could import the math module
# and then use math.pi as the default value for pi_value.
import math

def circle_area(radius, pi_value=math.pi):  # 使用math.pi作为默认值
    return pi_value * radius ** 2  # 等价于 pi_value * radius * radius

print(circle_area(2))  # 输出：12.566370614359172（更精确的结果）

