data = open("input.txt", "r")

bagData = {}

def initializeBags(bagDescriptions):
    removeSuffix = lambda str, suff: str[:-1] if str.endswith(suff) else str
    getBagQuantity = lambda str: int(str.split(" ")[0]) if str[0] != "n" else 0 # distinguish between regular bag quantities and "no other bag"
    for bag in bagDescriptions:
        bags = list([removeSuffix(removeSuffix(i.replace(".", ""), " "), "s") for i in bag.replace("contain", ",").split(", ")])
        # describe bag types and quantities
        subBags, subBagNums = zip(*list([(i[2:], getBagQuantity(i)) for i in bags[1:]]))
        
        bagData[bags[0]] = [list(subBags), list(subBagNums)]


def hasShinyGoldBag(bag):
    for subBag in bagData[bag][0]:
        if(subBag == "shiny gold bag"):
            return True
        elif(subBag == " other bag"):
            return False
        else:
            if(hasShinyGoldBag(subBag)):
                return True
    return False

def getNumberOfRequiredBags(bag):
    requiredBags = 0
    subBagData = list(zip(*bagData[bag]))
    print(subBagData)
    for subBag, subBagNum  in subBagData:
        if(subBagNum > 0):
            requiredBags += subBagNum + subBagNum * getNumberOfRequiredBags(subBag)
    return requiredBags
            

bagDescriptions = data.read().split("\n")
initializeBags(bagDescriptions)
print(bagData)

bagsWithShinyGoldBags = 0
requiredBags = getNumberOfRequiredBags("shiny gold bag")

for bag in bagData:
    if(hasShinyGoldBag(bag)):
        bagsWithShinyGoldBags += 1

print("Bags with at least one shiny gold bag: %s" % bagsWithShinyGoldBags)
print(requiredBags)
