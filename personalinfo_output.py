with open("./output.txt", "r") as file_info:
    lines = file_info.readlines()
    for line in lines :
        print(line.strip())
        
while True:
        find = (input("Do you want to search for any information?  : "))
        if find == 'yes' or find == 'Yes' or find == 'Y' or find == 'y':
            find_info = (input("Enter the info you want: "))
            
        else:
            print()
            break
        