#Create a program that ask user for personal information.
# Minimum of 5 information per person, more info the better. eg. Fullname, Address, etc.
with open("./output.txt", "a") as file_info :
                file_info.write(input("please input name ") + "\n")
                file_info.write(input("please input age ") + "\n")
                file_info.write(input("please input birthday ") + "\n")
                file_info.write(input("please input address ") + "\n")
                file_info.write(input("please input number ") + "\n")
    
                print(file_info)
                
while True:
    var1 = (input("input another? "))
    if var1 == 'yes' or var1 == 'Yes' or var1 == 'Y' or var1 == 'y':
        try:
            with open("./output.txt", "a") as file_info :
                file_info.write(input("please input name ") + "\n")
                file_info.write(input("please input age ") + "\n")
                file_info.write(input("please input birthday ") + "\n")
                file_info.write(input("please input address ") + "\n")
                file_info.write(input("please input number ") + "\n")
    
                print(file_info)
                break
        except:
            print()
            
    else:
        print()
        break
#natagalan po ako kase kalako mali... yun pala kulang lng ng "file_info.write" sa unahan