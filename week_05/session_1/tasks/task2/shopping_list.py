# Step 1: Create an empty list for the shopping list.
# optional: see if there is an existing shopping list file and load that
# hint: use try/except to check if the file exists, or import os and use os.path.exists()

# Step 2: Define a function to add an item to the list.
# Prompt the user for the item name and add it to the list.

# Step 3: Define a function to remove an item from the list.
# Prompt the user for the item name to remove and delete it from the list if it exists.
# hint: use list.remove() or check if item is in list first

# Step 4: Define a function to write the current shopping list to a file called 'shopping_list.txt'.
# hint: use 'w' mode to overwrite the file each time with the current list
# hint: don't forget \n for new lines

# Step 5: create the main program loop with a small menu system which lets the user:
# - Call the functions to add or remove items.
# - After each action, write the updated shopping list to 'shopping_list.txt'.
# - Add a way of exiting the program
# hint: use a while loop with a menu and user choice
# 步骤1：初始化购物清单（支持从文件加载）
shopping_list = []
try:
    with open('shopping_list.txt', 'r', encoding='utf-8') as f:
        shopping_list = [line.strip() for line in f if line.strip()]
    print("已加载现有购物清单 ✅")
except FileNotFoundError:
    print("未找到现有清单，创建新清单 🆕")

# 步骤2：定义添加项目函数
def add_item():
    item = input("请输入要添加的商品名称：").strip()
    if item:
        shopping_list.append(item)
        print(f"✅ 已添加：{item}")
    else:
        print("⚠️ 商品名称不能为空")

# 步骤3：定义删除项目函数
def remove_item():
    item = input("请输入要删除的商品名称：").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"❌ 已删除：{item}")
    else:
        print(f"❓ 未找到商品：{item}")

# 步骤4：定义保存清单函数
def save_list():
    with open('shopping_list.txt', 'w', encoding='utf-8') as f:
        for item in shopping_list:
            f.write(f"{item}\n")
    print("📄 购物清单已保存")

# 步骤5：主程序循环（菜单系统）
while True:
    print("\n===== 购物清单管理器 =====")
    print(f"当前清单 ({len(shopping_list)}项)：")
    for i, item in enumerate(shopping_list, 1):
        print(f"{i}. {item}")
    
    print("\n请选择操作：")
    print("1. 添加商品")
    print("2. 删除商品")
    print("3. 退出程序")
    
    choice = input("输入选项 (1-3)：").strip()
    if choice == '1':
        add_item()
        save_list()
    elif choice == '2':
        remove_item()
        save_list()
    elif choice == '3':
        print("感谢使用，再见！👋")
        break
    else:
        print("⚠️ 请输入有效的选项 (1-3)")
