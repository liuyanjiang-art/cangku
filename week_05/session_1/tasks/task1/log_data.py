# log files are provided by websites to track different http requests and where they come from
# this is useful for blocking disruptive IP addresses, tracking failed login attempts, and handling DDOS attacks
# site.log is an example of a log file - you can see it is not very human-readable

# open and read the file
# find all failed login attempts (POST /login with the response 401)
# and print these out in a human-readable format such as:
# IP address 192.168.1.17 failed to login at 10:42:12 on 2024-10-20

# Additional hints:
# - Remember to handle file errors
# - The first row is headers - you'll need to skip it
# - Each row has: Date, Time, IP_Address, User_Agent, Request, Status_Code
# - You need to find rows where Request = "POST /login" AND Status_Code = "401"
# - Use list comprehension or loops to filter the data

log_filename = input("请输入日志文件名（如 'site.log'）：")

try:
    # 打开日志文件并读取内容
    with open(log_filename, 'r', encoding='utf-8') as file:
        # 读取所有行，跳过第一行标题行
        lines = file.readlines()[1:]  # [1:] 切片操作，从第二行开始读取
        
        # 初始化失败登录记录列表
        failed_logins = []
        
        # 遍历每一行日志，提取关键信息
        for line in lines:
            # 移除行尾换行符，按逗号分隔字段（假设日志以逗号分隔，需根据实际分隔符调整）
            # 注意：若日志使用其他分隔符（如空格、Tab），需修改为 line.split('分隔符')
            fields = line.strip().split(',')
            
            # 确保每行有足够的字段（避免格式错误导致索引越界）
            if len(fields) < 6:
                continue  # 跳过格式异常的行
            
            # 提取字段（根据题目提示的列顺序：Date, Time, IP_Address, User_Agent, Request, Status_Code）
            date = fields[0]
            time = fields[1]
            ip = fields[2]
            request = fields[4].strip()  # 移除可能的空格
            status_code = fields[5].strip()
            
            # 筛选条件：POST /login 请求且状态码 401
            if request == "POST /login" and status_code == "401":
                failed_logins.append(f"IP地址 {ip} failed to login at {time} on {date}")
        
        # 输出结果
        if failed_logins:
            print("\n检测到以下失败登录尝试：")
            for record in failed_logins:
                print(record)
        else:
            print("\n未检测到失败的登录尝试（POST /login 401）。")

except FileNotFoundError:
    print(f"错误：文件 '{log_filename}' 不存在，请检查文件名或路径是否正确。")
except Exception as e:
    print(f"处理日志文件时发生错误：{e}")
