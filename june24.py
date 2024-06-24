# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.
# salary=float(input("Enter your current salary"))
# yof=float(input("Enter your year of service"))
# if yof>5:
#       bonus=(salary*0.05)+salary
#       print("your new salary is:",bonus)
# elif yof<5:
#      print("sorry you are not eligible for bonus")      

# Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
#              Unit                                                     Price  
# First 100 units                                               no charge
# Next 100 units                                              Rs 5 per unit
# After 200 units                                             Rs 10 per unit
# (For example if input unit is 350 than total bill amount is Rs2000

# units=int(input("enter the number of units you have consumed"))
# if units==100:
#     print("your electricity bill is : Rs0")
# elif units<=200:
#     bill=(units-100)*5
#     print("your electricity bill is:",bill)    
# else:
#   bill=(units-200)*10+500
#   print("your electricity bill is:",bill)

#     # Write a program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday , 2 for Monday and so on.
        
# days=int(input("enter any number between 1 to 7"))
# if days==1:
#     print("Today is Sunday")
# elif days==2:    
#     print("Today is Monday")
# elif days==3:
#     print("Today is Tuesday")    
# elif days==4:
#     print("Today is Wednesday")    
# elif days==5:
#     print("Today is Thursday")    
# elif days==6:
#     print("Today is Friday")    
# else:
#     print("Today is Saturday")    

# Accept any city from the user and display monument of that city.
#                   City                                 Monument
#                   Delhi                               Red Fort
#                   Agra                                Taj Mahal
#                   Jaipur                              Jal Mahal

# city=input("Enter the name of any city")
# if city=='Delhi':
#     print("Monument: Red Fort")
# elif city=='Agra':
#     print("Monument:Taj Mahal")
# elif city=='Jaipur':
#     print("Monument:Jal Mahal")
# else:
#     print("Invalid city")    