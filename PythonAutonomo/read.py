from fileinput import close


coun_file = open("path.txt","r")
print(coun_file.readable())
print(coun_file.readline())
print(coun_file.readline())
print(coun_file.readlines()[2])
for lines in coun_file.readlines():
    print(lines)

coun_file.close()