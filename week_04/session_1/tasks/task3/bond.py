# Week 4, Session 1: Task 3

# You are given an incomplete function isBond with a docstring. Your task
# is to complete the function based on the details in the docstring.



    
def isBond(intList):
    """
    This function accepts a list of integers and returns True if the
    sequence 0, 0, 7 appears in the list, in that order. Return False
    otherwise. The numbers do not need to be consecutive, but must appear
    in the specified order.
    """
    targets = [0, 0, 7]  # 目标序列
    target_index = 0      # 当前需要匹配的目标索引
    
    for num in intList:
        if target_index < len(targets) and num == targets[target_index]:
            target_index += 1  # 匹配成功，移动到下一个目标
    
    return target_index == len(targets)  # 若所有目标都匹配，返回 True

    # pass is a Python keyword used as a placeholder for future code,
    # meaning you need to delete pass to write your code.
    # Nothing happens when pass is executed.

    pass     # delete pass to write your code

# Check if the following lines of code produce the correct output
print(isBond([1, 2, 4, 0, 0, 7, 5]))   # True
print(isBond([1, 0, 2, 4, 0, 5, 7]))   # True
print(isBond([1, 7, 2, 0, 4, 5, 0]))   # False
