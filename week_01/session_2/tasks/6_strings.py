# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}")#whole
print(f"Modified String 1: {user_string.lower()}")#converting the user string to all lowercase
print(f"Modified String 2: {user_string.upper()}")#converting the user string to all uppercase
print(f"Modified String 3: {user_string.strip()}")#delete the start and end 
print(f"Modified String 4: {user_string.replace('a', '@')}")#replace a with @
print(f"Modified String 5: {user_string.capitalize()}")#capitalize the first word and rest of it lowercase 
print(f"Modified String 6: {user_string[::-1]}")#back
print(f"Modified String 7: {user_string.title()}")#conver the first letter of each word into uppercase
print(f"Modified String 8: {len(user_string)}")#get the length of it
print(f"Modified String 9: {user_string.find('a')}")#find the first place where a exsits
print(f"Modified String 10: {user_string.count('a')}")#find the appearing times of 'a'
print(f"Modified String 11: {user_string.startswith('Hello')}")#add the 'hello' to the heading
print(f"Modified String 12: {user_string.endswith('!')}")#add '!' to the end
print(f"Modified String 13: {user_string.isalnum()}")#distingguish if only number and letter
print(f"Modified String 14: {user_string.isalpha()}")#distinguish if all letter 
print(f"Modified String 15: {user_string.isdigit()}")#distingush if all number



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!