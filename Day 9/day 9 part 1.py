# day 9 part 1


with open("day 9 input.txt", "r") as fid:
    moveList = fid.readlines()


H = {"x": 0, "y": 0}
T = {"x": 0, "y": 0}

coordsRecord = []

for line in moveList:
    direction, amount = line.strip().split()
    amount = int(amount)

    for i in range(amount):
        # process new head position
        if (direction == "L"):
            H["x"] -= 1

        elif (direction == "R"):
            H["x"] += 1

        if (direction == "U"):
            H["y"] += 1

        elif (direction == "D"):
            H["y"] -= 1

        # ---------------------------
        # process where tail moves
        deltaX = H["x"] - T["x"]
        deltaY = H["y"] - T["y"]

        # moves straight right
        if (deltaX == 2 and deltaY == 0):
            T["x"] += 1

        # moves straight left
        if (deltaX == -2 and deltaY == 0):
            T["x"] -= 1

        # straight up
        if (deltaX == 0 and deltaY == 2):
            T["y"] += 1

        # straight down
        if (deltaX == 0 and deltaY == -2):
            T["y"] -= 1

        # ---------------------------

        # upper left -> up
        if (deltaX == -1 and deltaY == 2):
            T["y"] += 1
            T["x"] -= 1

        # upper right -> up
        if (deltaX == 1 and deltaY == 2):
            T["y"] += 1
            T["x"] += 1

        # ---------------------------

        # lower left -> down
        if (deltaX == -1 and deltaY == -2):
            T["y"] -= 1
            T["x"] -= 1

        # lower right -> down
        if (deltaX == 1 and deltaY == -2):
            T["y"] -= 1
            T["x"] += 1

        # ---------------------------

        # left side high -> left
        if (deltaX == -2 and deltaY == 1):
            T["y"] += 1
            T["x"] -= 1

        # left side lower -> left
        if (deltaX == -2 and deltaY == -1):
            T["y"] -= 1
            T["x"] -= 1

        # ---------------------------

        # right side high -> right
        if (deltaX == 2 and deltaY == 1):
            T["y"] += 1
            T["x"] += 1

        # right side lower -> right
        if (deltaX == 2 and deltaY == -1):
            T["y"] -= 1
            T["x"] += 1

        # ---------------------------
        # ---------------------------

        # add coords to list
        currentCoords = [T["x"], T["y"]]
        coordsRecord.append(currentCoords)

allCoords = [tuple(x) for x in coordsRecord]
allCoords = set(allCoords)
allPositions = len(allCoords)

print("Answer is", allPositions)
