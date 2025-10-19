# Your aim is to read in a text file, and calculate how many words are in it.
# You should:
#    - ask the user to enter the file name
#    - read the file in
#    - count how many words are in the file - there are multiple ways of doing this.

# You can use any of the .txt files to test this - or even make your own.

# get the file name

# open and read the file
# hint: remember to handle the case where the file might not exist

# calculate the number of words
# hint: you could use .split() to break up by spaces
# hint: watch out for empty lines that might give you empty strings

# display the wordcount

# Here are the word counts you should get:
# story.txt - 290
# story2.txt - 326
# glasses.txt - 215
file_name = input("请输入文件名（含.txt后缀）: ")

try:
    # 打开文件并读取内容
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 计算单词数：使用split()默认按任意空白字符分割（空格、换行、制表符等），过滤空字符串
    words = content.split()  # split()无参数时，会自动忽略连续空格和空行
    word_count = len(words)  # 直接统计非空单词的数量
    
    # 输出结果
    print(f"文件 '{file_name}' 中的单词数为: {word_count}")

except FileNotFoundError:
    # 处理文件不存在的情况
    print(f"错误：找不到文件 '{file_name}'，请检查文件名是否正确。")
except Exception as e:
    # 处理其他可能的异常（如权限问题等）
    print(f"读取文件时发生错误: {e}")
