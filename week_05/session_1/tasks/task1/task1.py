task1
#find the frequency
file_name=input('put the filename')
with open('file_name','r',encoding='utf-8') as file:
    content=file.read()
letter_count={}
for i in content:
    if i.isalpha():
        i_letter=i.lower()
        if i_letter in letter_count:
            letter_count[i_letter]+=1
        else:
            letter_count[i_letter]=1
for letter in sorted(letter_count.keys()):
    print(f'{letter}:{letter_count[letter]}')
max=max(letter_count,key=)