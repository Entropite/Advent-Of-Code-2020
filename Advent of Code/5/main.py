MIN_SEAT_ID = 6
MAX_SEAT_ID = 951 # from part one

data = open("input.txt", "r")

def processBoardingPass(boardingPass):
    row = 0
    for i in range(7):
        if boardingPass[i] == "B":
            row += 2**(6-i)

    column = 0
    for i in range(3):
        if boardingPass[7+i] == "R":
            column += 2**(2-i)

    return (row, column)

idSet = set(range(MIN_SEAT_ID, MAX_SEAT_ID+1))

highestSeatId = 0
for boardingPass in data.read().split("\n"):
    (row, column) = processBoardingPass(boardingPass)
    seatId = row * 8 + column
    idSet.remove(seatId)
    if seatId > highestSeatId:
        highestSeatId = seatId
    
print(highestSeatId)
print(idSet)



    