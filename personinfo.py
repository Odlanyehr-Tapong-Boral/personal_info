#Create a program that ask user for personal information.
# Minimum of 5 information per person, more info the better. eg. Fullname, Address, etc.
with open("./output.txt", "a") as file_info :
    var1 = (input("please input name "))
    var2 = (input("please input age "))
    var3 = (input("please input birthday "))
    var4 = (input("please input address "))
    var5 = (input("please input number "))
    
    print(file_info)

# Write the collected information in a txt file.
# It's up to you on how you'd like to format the information in the file.
# The program should ask user if want to input another person or exit.
