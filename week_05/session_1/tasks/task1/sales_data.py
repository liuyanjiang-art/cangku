# You've been asked to analyse a set of sales data which you can find in sales.csv

# Open the file and read the data
# find the:
#   - largest sale day (highest sale amount)
#   - average sale amount
#   - the widget which has been sold the most
# and print these out in a nice, human-readable format

# for a challenge - add a menu so the user picks which piece of data to show

# Additional hints:
# - Remember to handle file errors
# - The first row contains headers: Date, Product, Sales_Amount, Units_Sold, Region
# - Sales amounts are stored as strings - you'll need to convert to int() for math
# - For finding the highest selling widget, use a dictionary to count units sold per product
# - For average, sum all sales amounts and divide by number of rows
import csv

def load_sales_data(filename):
    """加载销售数据并返回处理后的列表"""
    sales_data = []
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # 转换销售金额为整数
                try:
                    row['Sales_Amount'] = int(row['Sales_Amount'])
                    row['Units_Sold'] = int(row['Units_Sold'])
                    sales_data.append(row)
                except ValueError:
                    print(f"警告：跳过无效数据行 - {row}")
        return sales_data
    except FileNotFoundError:
        print(f"错误：文件 '{filename}' 不存在")
        return None
    except Exception as e:
        print(f"读取文件时发生错误：{str(e)}")
        return None

def find_largest_sale_day(sales_data):
    """找出销售额最高的日期"""
    if not sales_data:
        return None
    max_sale = max(sales_data, key=lambda x: x['Sales_Amount'])
    return {
        'date': max_sale['Date'],
        'amount': max_sale['Sales_Amount'],
        'product': max_sale['Product']
    }

def calculate_average_sale(sales_data):
    """计算平均销售额"""
    if not sales_data:
        return 0
    total = sum(row['Sales_Amount'] for row in sales_data)
    return round(total / len(sales_data), 2)

def find_top_selling_widget(sales_data):
    """找出销量最高的产品"""
    if not sales_data:
        return None
    product_counts = {}
    for row in sales_data:
        product = row['Product']
        product_counts[product] = product_counts.get(product, 0) + row['Units_Sold']
    # 找出销量最高的产品
    top_product = max(product_counts.items(), key=lambda x: x[1])
    return {
        'product': top_product[0],
        'units_sold': top_product[1]
    }

def display_menu():
    """显示用户菜单"""
    print("\n===== 销售数据分析工具 =====")
    print("1. 查看销售额最高的日期")
    print("2. 查看平均销售额")
    print("3. 查看销量最高的产品")
    print("4. 查看所有分析结果")
    print("5. 退出")
    return input("请选择操作 (1-5): ")

def main():
    sales_data = load_sales_data('sales.csv')
    if not sales_data:
        return

    while True:
        choice = display_menu()
        
        if choice == '1':
            largest_sale = find_largest_sale_day(sales_data)
            if largest_sale:
                print(f"\n📅 销售额最高的日期: {largest_sale['date']}")
                print(f"   产品: {largest_sale['product']}")
                print(f"   销售额: ¥{largest_sale['amount']}")
        
        elif choice == '2':
            avg_sale = calculate_average_sale(sales_data)
            print(f"\n📊 平均销售额: ¥{avg_sale}")
        
        elif choice == '3':
            top_widget = find_top_selling_widget(sales_data)
            if top_widget:
                print(f"\n🏆 销量最高的产品: {top_widget['product']}")
                print(f"   总销量: {top_widget['units_sold']} 件")
        
        elif choice == '4':
            print("\n===== 完整分析报告 =====")
            largest_sale = find_largest_sale_day(sales_data)
            avg_sale = calculate_average_sale(sales_data)
            top_widget = find_top_selling_widget(sales_data)
            
            print(f"1. 销售额最高日期: {largest_sale['date']} (¥{largest_sale['amount']})")
            print(f"2. 平均销售额: ¥{avg_sale}")
            print(f"3. 销量最高产品: {top_widget['product']} ({top_widget['units_sold']}件)")
        
        elif choice == '5':
            print("\n感谢使用！再见！👋")
            break
        
        else:
            print("\n❌ 无效选择，请输入 1-5 之间的数字")

if __name__ == "__main__":
    main()
