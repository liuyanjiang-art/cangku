# Frequency analysis is a method of breaking certain ciphers which involves counting the frequency of letters/symbols
# because English has quite a clear distribution of letters, with spikes on common letters such as 'e', 'i' and 's'

# Ask the user for a filename
# open and read the file 
# and count how many instances of each letter are in the program
# hint: use a dictionary!

# Additional hints:
# - Remember to handle the case where the file might not exist
# - You'll need to check each character to see if it's a letter
# - Dictionary pattern: if key exists, increment; if not, set to 1
# - Consider converting to lowercase for consistent counting

#this is a test
# 提示用户输入文件名
filename = input("请输入文件名（含路径，如 'test.txt'）：")

# 初始化字母统计字典（键为字母，值为出现次数）
letter_counts = {}

try:
    # 打开并读取文件（使用 'r' 模式，默认编码UTF-8）
    with open(filename, 'r', encoding='utf-8') as file:
        # 读取文件内容并转换为小写（统一统计大小写字母）
        content = file.read().lower()
        
        # 遍历每个字符，判断是否为字母并统计
        for char in content:
            if char.isalpha():  # 仅统计字母（忽略数字、符号、空格等）
                if char in letter_counts:
                    letter_counts[char] += 1  # 字母已存在，次数+1
                else:
                    letter_counts[char] = 1   # 字母首次出现，初始化为1

    # 输出统计结果
    print("\n文件中字母出现频率统计：")
    for letter, count in sorted(letter_counts.items()):  # 按字母顺序排序输出
        print(f"字母 '{letter}': {count} 次")

except FileNotFoundError:
    # 处理文件不存在的异常
    print(f"错误：找不到文件 '{filename}'，请检查文件名或路径是否正确。")
except Exception as e:
    # 处理其他可能的异常（如权限问题、编码错误等）
    print(f"读取文件时发生错误：{e}")
