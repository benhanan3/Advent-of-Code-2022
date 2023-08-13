

with open("day2inputdata.txt", "r") as fid:

    dataList = fid.readlines()


totalPoint = 0

for match in dataList:

    individualRound = match.split()

    if (individualRound[1] == "X"):
        shapePoint = 1
        myPlay = "X"

    if (individualRound[1] == "Y"):
        shapePoint = 2
        myPlay = "Y"

    if (individualRound[1] == "Z"):
        shapePoint = 3
        myPlay = "Z"

# -------------

    if (individualRound[0] == "A" and myPlay == "X"):
        outcomePoint = 3

    if (individualRound[0] == "A" and myPlay == "Y"):
        outcomePoint = 6

    if (individualRound[0] == "A" and myPlay == "Z"):
        outcomePoint = 0

# --------------

    if (individualRound[0] == "B" and myPlay == "X"):
        outcomePoint = 0

    if (individualRound[0] == "B" and myPlay == "Y"):
        outcomePoint = 3

    if (individualRound[0] == "B" and myPlay == "Z"):
        outcomePoint = 6

# --------------

    if (individualRound[0] == "C" and myPlay == "X"):
        outcomePoint = 6

    if (individualRound[0] == "C" and myPlay == "Y"):
        outcomePoint = 0

    if (individualRound[0] == "C" and myPlay == "Z"):
        outcomePoint = 3

    roundPoint = outcomePoint + shapePoint
    totalPoint += roundPoint


print(totalPoint)
