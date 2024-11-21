with open("./output.txt", "r") as file_info:
    lines = file_info.readlines()
    for line in lines :
        print(line.strip())
        
while True:
        find = (input("Do you want to search for any information?  : "))
        if find == 'yes' or find == 'Yes' or find == 'Y' or find == 'y':
            find_info = (input("Enter the info you want: "))
            
            try:
                with open("./output.txt", "r") as file_info:
                    lines = file_info.readlines()
                    
                    print("\n--- Search Results ---")
                    for line in lines:
                       if find_info in line:
                          print(line.strip())
                          
                       else:
                        print("No results found for your search.")
            except FileNotFoundError:
                            print("The file 'output.txt' does not exist. Please collect information first.")

            
        else:
            print()
            break
        