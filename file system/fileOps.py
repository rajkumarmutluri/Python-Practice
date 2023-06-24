# with open("file1.txt", 'a') as file:
#     lines = file.readlines()
#     file.seek(0)
#     content = file.read()
#     print(content)
#     print('\n')
#     print(lines)
    
filenew = open("../fileName.txt",'w')
content = "Hello, I'm creating file in the parent directory using file path ../fileName.txt \n"
filenew.write(content)
filenew.close()