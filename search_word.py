file = open("sample.txt")

search = input("Please enter : ")

if(search in file.read()):
    print(search, "found")
else:
    print(search, "word not found")