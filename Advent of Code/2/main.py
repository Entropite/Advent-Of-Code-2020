file = open("passwords.txt", "r")
data = file.read()
file.close()
data = data.replace(":", "")
data = data.replace("-", " ")
data = data.split("\n")
for i in range(len(data)):
    data[i] = data[i].split(" ")

print(data)
validPasswords = 0
for i in data:
    if(len(i[3]) >= int(i[1])):
        if((i[3][int(i[0])-1] == i[2] or i[3][int(i[1])-1] == i[2]) and not (i[3][int(i[0])-1] == i[2] and i[3][int(i[1])-1] == i[2])):
            validPasswords += 1

print(validPasswords)