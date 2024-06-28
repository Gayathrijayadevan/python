# 26/06/2024

# 1. find oddsum evensum and sum of numbers upto a limit

 # a=int(input("enter starting number"))
 # b=int(input("enter ending number"))
 # oddsum=0
 # evensum=0
 # sum=0
 # for i in range(a,b+1):
 #     sum+=i
 #     if i%2==0:
 #         evensum+=i
 #     else:
 #         oddsum+=i
 # print("even sum is:",evensum)    
 # print("odd sum:",oddsum)
 # print("sum of all numbers:",sum)

# 2. factorial of a number
 # a=int(input("enter a number"))
 # fact=1
 # for i in range(1,a+1):
 #     fact=fact*i
 # print("factorial=",fact)  
 # 

# 3.multiplication table  

 # a=int(input("enter a number:"))
 # for i in range(1,11):
 #    print(i,'*',a,'=',i*a)

# 27/6/2024

# 1. print a string and reverse it
# a='welcome'
# s=''
# for i in a:
#     s=i+s
# print(s)

# 2.print the pattern
# * * *
# * * *
# * * *
# for i in range(3):
#     for j in range(3):
#         print('*',end='\t')
#     print()        

# 3.print the pattern
# 0 0 0
# 1 1 1
# 2 2 2
# for i in range(3):
#     for j in range(3):
#         print(i,end='\t')
        
#     print()
        

# 4.print the pattern
#   0 1 2
#   0 1 2      
#   0 1 2

# for i in range(3):
#     for j in range(3):
#         print(j,end='\t')
        
#     print()

# 5. print the pattern
    #  0 1 2
    #  3 4 5
    #  6 7 8

# a=0
# for i in range(3):
#     for j in range(3):
#         print(a,end='\t')
#         a+=1
#     print()

# 28/06/2024

#1. 0
#   1 1
#   2 2 2

# for i in range(3):
#     for j in range(i+1):
    #     print(i,end='\t')
    # print()    

# 2.0
#   0 1
#   0 1 2

# for i in range(3):
#     for j in range(i+1):
    #     print(j,end='\t')
    # print()    

# 3.0
#   1 2
#   3 4 5

# a=0
# for i in range(3):
#     for j in range(i+1):
    #       print(a,end='\t')
    #       a+=1
    # print()  

# 4.0
#   1 0
#   2 1 0

# for i in range(3):
#     for j in range(i+1):
        # print(i-j,end='\t')
    # print()    

# 5.A A A
#   B B B
#   C C C

# a=65
# for i in range(3):
#     for j in range(3):
#         print(chr(a),end='\t')
#     print()    
#     a+=1

# 6. A B C
#    A B C
#    A B C
   
# a=65
# for i in range(3):
    # for j in range(3):
        #  print(chr(a),end='\t')
        #  
    # print()    

# 7. A B C   
#    D E F 
#    G H I

# a=65
# for i in range(3):
#     for j in range(3):
#         print(chr(a),end='\t')
    #     a+=1
    # print()    
# 8.A
#   B C
#   D E F
# a=65
# for i in range(3):
    # for j in range(i+1):
        # print(chr(a),end='\t')
        # a+=1
    # print()    