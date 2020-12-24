data = open("geography.txt", "r")
geography = data.read()
width = len(geography.split("\n")[0])
geography = geography.replace("\n", "")
slopes = [(1,2)]
for slope in slopes:
    position = 0
    collisions = 0
    while(position < len(geography)):
        if(geography[position] == "#"):
            collisions+=1
            geography = list(geography)
            geography[position] = "X"
            geography = "".join(geography)
        elif(geography[position] == "."):
            geography = list(geography)
            geography[position] = "O"
            geography = "".join(geography)
        position += (slope[1]-1)*width
        if((position+slope[0]) % width > (position % width) or (position % width == 0)):
            position += (slope[1]-1 if (slope[1] > 1) else slope[1])*width 
        position += slope[0]

    print("%s:%s" % (slope, collisions))
for i in range(int(len(geography)/width)):
    print(geography[i*width:i*width+width])