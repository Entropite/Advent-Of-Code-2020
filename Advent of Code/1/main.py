data = open("data.txt", "r")

intArray = []
for i in data:
    # print(i)
    intArray.append(int(i))

for i in range(len(intArray)):
    for j in range(len(intArray)-i):
        for k in range(len(intArray)):
            if(intArray[i] + intArray[i+j] + intArray[k] == 2020):
                print(intArray[i] * intArray[i+j] * intArray[k])