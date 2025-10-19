# Week 4, Session 2: Task 1

# Write a function format_date that takes 4 arguments: day, month,
# year, separator. The separator is an optional argument with a default
# value to be "-". The function returns the formatted date as a string
# in the format day-month-year with the default separator.


def format_date(day, month, year, separator="-"):  # 为separator设置默认值"-"
    # 将日、月、年转换为字符串并拼接，使用separator分隔
    formatted_date = f"{day}{separator}{month}{separator}{year}"
    return formatted_date


# 测试函数：使用不同分隔符调用
print(format_date(15, 10, 2025))          # 默认分隔符 "-" → 15-10-2025
print(format_date(5, 3, 2023, "/"))       # 自定义分隔符 "/" → 5/3/2023
print(format_date(20, 12, 2024, ":"))     # 自定义分隔符 ":" → 20:12:2024
print(format_date(9, 9, 2022, "."))       # 自定义分隔符 "." → 9.9.2022



# Write code to call the function with other separators such as "/", ":", "."
