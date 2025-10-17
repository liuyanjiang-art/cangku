# To test that you can successfully download a file and upload it to gradescope

# You are going to write a very simple program:

# Ask a user to enter two numbers (one per input)

# multiply those numbers together

# print out the result

# There is an extra point available for validating that they entered numbers!
# Add to your code so that if they entered something other than an integer it prints
# 'That is not a number' and exits.

# Download your file, and upload it to the 'Week 1 Session 2 - Practice Upload' task on Minerva.
# You will get some feedback - ensure you are passing the tests!
# 提示用户输入两个数字
while True:
    try:
        num1 = int(input("请输入第一个整数："))
        num2 = int(input("请输入第二个整数："))
        break
    except ValueError:
        print("'That is not a number', and exits.")

# 计算并打印乘积
result = num1 * num2
print(f"两个数的乘积是：{result}")