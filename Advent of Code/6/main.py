data = open("input.txt", "r")

groups = data.read().split("\n\n") # divide into groups

def getTotalDeclarationsFromGroup(group):
    declarations = [0] * 26
    for char in group:
        order = ord(char)
        
        if(order > 96 and order < 123 and declarations[order-97] == 0):
            declarations[order-97] = 1
    return sum(declarations)

def getUbiquitousDeclarationsFromGroup(group):
    declarations = [0] * 26
    groupSize = group.count("\n") + 1

    for i in range(97, 123):
        if(group.count(chr(i)) == groupSize):
            declarations[i-97] = 1
    return sum(declarations)

totalDeclarations = 0
totalUbiquitousDeclarations = 0 # where all members in a group answer yes

for group in groups:
    totalDeclarations += getTotalDeclarationsFromGroup(group)
    totalUbiquitousDeclarations += getUbiquitousDeclarationsFromGroup(group)
print("Total Declarations: %s"  % totalDeclarations) # Part 1
print("Total Ubiquitous Declarations: %s" % totalUbiquitousDeclarations) # Part 2