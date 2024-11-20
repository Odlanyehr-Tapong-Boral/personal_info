#Create a program that ask user for personal information.
# Minimum of 5 information per person, more info the better. eg. Fullname, Address, etc.
with open("./output.txt", "a") as file_info :
                (input("please input name "))
                (input("please input age "))
                (input("please input birthday "))
                (input("please input address "))
                (input("please input number "))
    
                print(file_info)
                
while True:
    var1 = (input("input another?"))
    if var1 == 'yes' or var1 == 'Yes' or var1 == 'Y' or var1 == 'y':
        try:
            with open("./output.txt", "a") as file_info :
                (input("please input name "))
                (input("please input age "))
                (input("please input birthday "))
                (input("please input address "))
                (input("please input number "))
    
                print(file_info)
                break
        except:
            print()
            
    else:
        print()
        break
# Write the collected information in a txt file.
# It's up to you on how you'd like to format the information in the file.
# The program should ask user if want to input another person or exit.