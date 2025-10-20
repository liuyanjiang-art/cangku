# Step 1: Create an empty list to hold quiz questions.

# Step 2: Define a function to add a new quiz question.
# This function should prompt the user for the question, options, and the correct answer.
# Store each question as a dictionary in the list.
# hint: dictionary could have keys like 'question', 'options', 'correct_answer'
# hint: options could be stored as a list of strings

# Step 3: Define a function to write the quiz questions to a file called 'quiz_questions.txt'.
# Format the questions nicely for readability, including the question text and possible answers.
# hint: loop through your list of dictionaries
# hint: use \n for formatting and spacing between questions

# Step 4: Define a function to display all current quiz questions in the console.
# hint: similar to step 3, but use print() instead of file writing

# Step 5: In the main part of the program:
# - Call the function to add questions in a loop until the user decides to stop.
# - After finishing, call the function to write all questions to 'quiz_questions.txt' in a nice, human-readable format
# - Optionally, display the questions on the console before writing them to the file.
# hint: use a while loop and you could ask user if they want to continue after each question
# Step 1: Create an empty list to hold quiz questions.

# Step 2: Define a function to add a new quiz question.
# This function should prompt the user for the question, options, and the correct answer.
# Store each question as a dictionary in the list.
# hint: dictionary could have keys like 'question', 'options', 'correct_answer'
# hint: options could be stored as a list of strings

# Step 3: Define a function to write the quiz questions to a file called 'quiz_questions.txt'.
# Format the questions nicely for readability, including the question text and possible answers.
# hint: loop through your list of dictionaries
# hint: use \n for formatting and spacing between questions

# Step 4: Define a function to display all current quiz questions in the console.
# hint: similar to step 3, but use print() instead of file writing

# Step 5: In the main part of the program:
# - Call the function to add questions in a loop until the user decides to stop.
# - After finishing, call the function to write all questions to 'quiz_questions.txt' in a nice, human-readable format
# - Optionally, display the questions on the console before writing them to the file.
# hint: use a while loop and you could ask user if they want to continue after each question


# Step 1: 创建空列表存储题库
quiz_questions = []

# Step 2: 定义添加问题的函数
def add_question():
    """向题库添加新问题"""
    question = input("请输入问题内容: ")
    
    # 获取选项（支持自定义数量）
    options = []
    print("\n请输入选项（输入空值结束）")
    while True:
        option = input(f"选项 {len(options)+1}: ").strip()
        if not option:  # 空输入时停止添加选项
            if len(options) < 2:
                print("至少需要2个选项！")
                continue
            break
        options.append(option)
    
    # 获取正确答案（验证输入合法性）
    while True:
        correct_input = input(f"\n请输入正确选项序号(1-{len(options)}): ").strip()
        if correct_input.isdigit():
            correct_idx = int(correct_input) - 1  # 转换为索引
            if 0 <= correct_idx < len(options):
                correct_answer = options[correct_idx]
                break
        print(f"输入无效，请输入1到{len(options)}之间的数字")
    
    # 将问题添加到列表
    quiz_questions.append({
        'question': question,
        'options': options,
        'correct_answer': correct_answer
    })
    print("问题添加成功！\n" + "-"*50)

# Step 3: 定义写入文件的函数
def write_to_file(filename='quiz_questions.txt'):
    """将题库写入文件"""
    with open(filename, 'w', encoding='utf-8') as f:
        for i, q in enumerate(quiz_questions, 1):
            # 写入问题编号和内容
            f.write(f"问题 {i}: {q['question']}\n")
            
            # 写入选项
            f.write("选项:\n")
            for idx, option in enumerate(q['options'], 1):
                f.write(f"  {idx}. {option}\n")
            
            # 写入正确答案
            f.write(f"正确答案: {q['correct_answer']}\n")
            f.write("\n" + "="*60 + "\n\n")  # 分隔线
    print(f"\n题库已保存至 {filename}")

# Step 4: 定义显示问题的函数
def display_questions():
    """在控制台显示所有问题"""
    if not quiz_questions:
        print("题库为空！")
        return
    
    print("\n" + "当前题库内容".center(50, "=") + "\n")
    for i, q in enumerate(quiz_questions, 1):
        print(f"问题 {i}: {q['question']}")
        print("选项:")
        for idx, option in enumerate(q['options'], 1):
            print(f"  {idx}. {option}")
        print(f"正确答案: {q['correct_answer']}\n" + "-"*50)

# Step 5: 主程序逻辑
if __name__ == "__main__":
    print("===== 测验题库生成器 =====")
    
    # 循环添加问题
    while True:
        add_question()
        while True:
            choice = input("是否继续添加问题? (y/n): ").strip().lower()
            if choice in ['y', 'n']:
                break
            print("请输入 'y' 或 'n'")
        if choice == 'n':
            break
    
    # 可选：显示所有问题
    if input("\n是否显示所有问题? (y/n): ").strip().lower() == 'y':
        display_questions()
    
    # 写入文件
    write_to_file()
    print("程序结束！")
