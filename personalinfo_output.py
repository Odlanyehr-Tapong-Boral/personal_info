with open("./output.txt", "r") as file_info:
    lines = file_info.readlines()
    for line in lines :
        print(line.strip())