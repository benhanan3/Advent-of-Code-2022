# day 9 part 2

with open("day 9 input.txt", "r") as fid:
    moveList = fid.readlines()


H = {"x": 0, "y": 0}
T = {"x": 0, "y": 0}
coords = {knot: [0, 0] for knot in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}

coordsRecord = []

for line in moveList:
    direction, amount = line.strip().split()
    amount = int(amount)

    for i in range(amount):
        # process new head position
        if (direction == "L"):
            coords[0][0] -= 1

        elif (direction == "R"):
            coords[0][0] += 1

        elif (direction == "U"):
            coords[0][1] += 1

        elif (direction == "D"):
            coords[0][1] -= 1

        # update rest of rope
        for knotSeg in range(1, 10):
            # process where tail moves
            deltaX = coords[knotSeg - 1][0] - coords[knotSeg][0]
            deltaY = coords[knotSeg - 1][1] - coords[knotSeg][1]

            # moves straight right
            if (deltaX == 2 and deltaY == 0):
                coords[knotSeg][0] += 1

            # moves straight left
            elif (deltaX == -2 and deltaY == 0):
                coords[knotSeg][0] -= 1

            # straight up
            elif (deltaX == 0 and deltaY == 2):
                coords[knotSeg][1] += 1

            # straight down
            elif (deltaX == 0 and deltaY == -2):
                coords[knotSeg][1] -= 1

            # ---------------------------

            # upper right corner
            elif ((deltaX >= 1 and deltaY == 2) or (deltaX == 2 and deltaY == 1)):
                coords[knotSeg][1] += 1
                coords[knotSeg][0] += 1

            # lower right corner
            elif ((deltaX >= 1 and deltaY == -2) or (deltaX == 2 and deltaY == -1)):
                coords[knotSeg][1] -= 1
                coords[knotSeg][0] += 1

            # lower left corner
            elif ((deltaX <= -1 and deltaY == -2) or (deltaX == -2 and deltaY == -1)):
                coords[knotSeg][1] -= 1
                coords[knotSeg][0] -= 1

            # upper left corner
            elif ((deltaX <= -1 and deltaY == 2) or (deltaX == -2 and deltaY == 1)):
                coords[knotSeg][1] += 1
                coords[knotSeg][0] -= 1

            # ---------------------------
            # ---------------------------

        # add coords to list
        currentCoords = [coords[9][0], coords[9][1]]
        coordsRecord.append(currentCoords)

allCoords = [tuple(x) for x in coordsRecord]
allCoords = set(allCoords)
allPositions = len(allCoords)

print("Answer is", allPositions)
