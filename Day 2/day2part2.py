

with open("day2inputdata.txt", "r") as fid:

    dataList = fid.readlines()


totalPoint = 0

for match in dataList:

    individualRound = match.split()

    # rock
    if (individualRound[0] == "A" and individualRound[1] == "X"):
        # scissors
        roundPoint = 3

    if (individualRound[0] == "A" and individualRound[1] == "Y"):
        # rock
        roundPoint = 4

    if (individualRound[0] == "A" and individualRound[1] == "Z"):
        # paper
        roundPoint = 8

# ----------------------

    # paper
    if (individualRound[0] == "B" and individualRound[1] == "X"):  # lose
        # rock
        roundPoint = 1

    if (individualRound[0] == "B" and individualRound[1] == "Y"):  # draw
        # paper
        roundPoint = 5

    if (individualRound[0] == "B" and individualRound[1] == "Z"):  # win
        # scissors
        roundPoint = 9

# ----------------------

    # scissors
    if (individualRound[0] == "C" and individualRound[1] == "X"):  # lose
        # paper
        roundPoint = 2

    if (individualRound[0] == "C" and individualRound[1] == "Y"):  # draw
        # scissors
        roundPoint = 6

    if (individualRound[0] == "C" and individualRound[1] == "Z"):  # win
        # rock
        roundPoint = 7

    totalPoint += roundPoint

print(totalPoint)
