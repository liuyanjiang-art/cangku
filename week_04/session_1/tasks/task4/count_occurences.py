# Week 4, Session 1: Task 4

# You are given an incomplete function count_occurences with docstring.
# Your task is to complete the function that takes two arguments:
#   (1) a list of string
#   (2) a string to search.

# This function returns the number of times a string appears in the list.
# This function is restricted to only accept positional arguments.
# Test the function with different list of strings and string to search

def count_occurences(l_strings, target, /):
    """
    Count how many times target appears in the list l_strings.

    Returns:
        int: number of occurences of target in l_strings.
    """
    count = 0
    for string in l_strings:
        if string == target:
            count += 1
    return count
# 测试用例1：目标存在多次
test_list1 = ["apple", "banana", "apple", "orange", "apple"]
target1 = "apple"
print(f"Test 1: {count_occurences(test_list1, target1)} → 预期输出：3")  # 实际输出：3

# 测试用例2：目标不存在
test_list2 = ["cat", "dog", "bird"]
target2 = "fish"
print(f"Test 2: {count_occurences(test_list2, target2)} → 预期输出：0")  # 实际输出：0

# 测试用例3：空列表
test_list3 = []
target3 = "test"
print(f"Test 3: {count_occurences(test_list3, target3)} → 预期输出：0")  # 实际输出：0

# 测试用例4：列表包含不同类型（不会匹配字符串目标）
test_list4 = [123, "apple", True, "apple"]
target4 = "apple"
print(f"Test 4: {count_occurences(test_list4, target4)} → 预期输出：2")  # 实际输出：2


# Write code to call the function and check if 
# correct output is produced