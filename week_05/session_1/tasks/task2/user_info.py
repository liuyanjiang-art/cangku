# Step 1: Prompt the user for their name, age, and favorite color.

# Step 2: Open a file called 'user_info.txt'

# Step 3: Write each piece of information to the file, each on a new line.

# hint: think about what mode to open in!
# hint: remember to add \n for new lines when writing to files
# hint: if you want multiple people to add info without overwriting, consider append mode 'a'

# you could extend this by using a loop to allow multiple people to enter their info in a row
def collect_user_info():
    # 步骤1：获取用户信息
    print("\n===== 用户信息收集 =====")
    name = input("请输入您的姓名：").strip()
    age = input("请输入您的年龄：").strip()
    color = input("请输入您最喜欢的颜色：").strip()

    # 基础数据验证
    if not all([name, age, color]):
        print("⚠️ 所有信息均为必填项，请重新输入")
        return False

    # 步骤2：以追加模式打开文件
    try:
        with open('user_info.txt', 'a', encoding='utf-8') as f:
            # 步骤3：按行写入信息（添加分隔符增强可读性）
            f.write("="*30 + "\n")  # 分隔线
            f.write(f"姓名：{name}\n")
            f.write(f"年龄：{age}\n")
            f.write(f"最喜欢的颜色：{color}\n\n")  # 空行分隔不同用户
        print(f"✅ 信息已保存！感谢您的参与，{name}！")
        return True
    except Exception as e:
        print(f"❌ 保存失败：{str(e)}")
        return False

# 主程序循环（支持多人连续录入）
while True:
    collect_user_info()
    another = input("\n是否继续添加其他用户信息？(y/n)：").strip().lower()
    if another != 'y':
        print("程序结束，再见！👋")
        break
#哈哈哈