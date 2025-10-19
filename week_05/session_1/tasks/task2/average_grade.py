# Step 1: Open a file called 'student_data.csv' to read each student's grades.
# hint: skip the header row with data[1:]
# hint: you could handle file errors with try/except

# Step 2: Read each student's grades and calculate their average grade
# hint: CSV data comes as strings, convert grade columns to int() for maths
# hint: student_data.csv has columns: ID, Name, Mathematics, Science, History
# hint: average = (maths + science + history) / 3

# Step 3: Sort the students by their average grade in descending order.
# hint: you might want to store each student as a dictionary with name and average
# hint: use the sorted() function with a key parameter, or list.sort()

# Step 4: Open a file called 'report.txt'
# Write each student's name and their average grade to the report in order
# hint: use 'w' mode to create a fresh report each time
# hint: format averages nicely, maybe to 2 decimal places with :.2f
import csv

# Step 1: 读取CSV文件并处理异常
students = []
try:
    with open('student_data.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # 跳过表头行（ID, Name, Mathematics, Science, History）
        
        # Step 2: 计算每个学生的平均分
        for row in reader:
            # 解析CSV行数据（确保有5列，避免索引错误）
            if len(row) != 5:
                print(f"警告：跳过格式错误的行 {row}")
                continue
            
            student_id, name, maths_str, science_str, history_str = row
            
            # 转换成绩为整数（处理可能的非数字值）
            try:
                maths = int(maths_str)
                science = int(science_str)
                history = int(history_str)
            except ValueError:
                print(f"警告：学生 {name} 的成绩包含非数字值，已跳过")
                continue
            
            # 计算平均分（保留2位小数）
            average = (maths + science + history) / 3
            students.append({"name": name, "average": round(average, 2)})  # 存储为字典

except FileNotFoundError:
    print("错误：找不到文件 'student_data.csv'，请确保文件存在。")
    exit()  # 文件不存在时终止程序
except Exception as e:
    print(f"读取CSV文件时发生错误: {e}")
    exit()

# Step 3: 按平均分降序排序
students_sorted = sorted(students, key=lambda x: x["average"], reverse=True)

# Step 4: 写入报告文件
try:
    with open('report.txt', 'w', encoding='utf-8') as report_file:
        report_file.write("学生成绩平均分报告（降序排列）\n")
        report_file.write("=" * 40 + "\n")  # 分隔线
        for student in students_sorted:
            # 格式化输出：姓名左对齐15字符，平均分保留2位小数
            line = f"{student['name']:15} 平均分: {student['average']:.2f}\n"
            report_file.write(line)
    print("报告生成成功！结果已保存至 'report.txt'")

except Exception as e:
    print(f"写入报告文件时发生错误: {e}")
