task1
#find the frequency
file_name = input('请输入文件名: ')
with open(file_name, 'r', encoding='utf-8') as file:  # 注意：原代码中'file_name'加了引号，会导致读取固定字符串而非变量，已修正
    content = file.read()

letter_count = {}
for char in content:
    if char.isalpha():  # 仅统计字母
        char_lower = char.lower()  # 不区分大小写（统一转为小写）
        letter_count[char_lower] = letter_count.get(char_lower, 0) + 1  # 简化计数逻辑

# 按字母顺序输出频率
for letter in sorted(letter_count.keys()):
    print(f'{letter}: {letter_count[letter]}')

# 修正：获取出现频率最高的字母（按值排序，取第一个）
max_letter = max(letter_count, key=lambda k: letter_count[k])
print(f'\n出现频率最高的字母: {max_letter}，次数: {letter_count[max_letter]}')
