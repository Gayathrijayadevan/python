import re

# a='wElcome123'
# print(re.sub('w','W',a))
# print(re.sub('welcome','python',a))
# print(re.sub("well",'python',a)

# print(re.split('e',a))
# print(re.split('e',a,1))

# print(re.findall('e',a))
# print(len(re.findall('e',a)))

# print(re.search('e',a))

# if re.search('z',a):
#     print("yes")
# else:
#     print('no')    

# print(re.search('[A-Z]',a))

# print(re.search('[0-9]',a))

# a='aBcD'
# print(re.search('a.',a))
# print(re.search('a..',a))

# print(re.search('d.*',a))
# print(re.search('a.*',a))

# print(re.search('a.+',a))

# print(re.search('c.?',a))
# print(re.search('a.?',a))

# print(re.search('[A-Z].',a))
# print(re.search('[A-Z].*',a))
# 

# 22/07/2024


# a='Abcde'
# print(re.search('[a-z][0-9]',a))
# print(re.search('[A-Z].*[a-z][0-9]',a))
# print(re.search('[0-9]$',a))
# print(re.search('e$',a))
# a='welcome'
# print(re.search('welcome$',a))

# a=input("Enter a phone number:")
# l=len(a)
# if l==10 and a.isdigit() and re.search('[6-9].{9}',a):
#     print("valid")
# else:
#     print("invalid")    


# email validation

# a=input("Enter a email:")
# if a.islower() and re.search('[a-z].*@gmail.com',a):
#     print("valid")
# else:
#     print("invalid")    

# password validation

a=input("Enter a password:")
pattern = r"^(?=.[a-z])(?=.[A-Z])(?=.\d)(?=.[!@#$%^&*()_+\-=\[\]{}|;:,.<>?]).{8,}$"
if re.search(pattern,a):
    print("valid")
else:
    print("invalid")    



