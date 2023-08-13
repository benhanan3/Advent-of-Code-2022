
# day 14 part 1

with open("day 14 input.txt", "r") as fid:
    data = fid.readlines()


# set up master list. list with list -> line with point
allLines = []
for line in data:
    line = line.split(" -> ")
    lineClean = []

    for point in line:
        x, y = point.split(",")
        x, y = int(x), int(y)

        lineClean.append((x, y))

    allLines.append(lineClean)


# find min/max x and y values for grid
allX = set()
allY = set()
allPointAbs = set()
for line in allLines:
    for point in line:
        x, y = point
        allPointAbs.add((x, y))
        allX.add(x)
        allY.add(y)

minX = min(allX)
maxX = max(allX)

minY = min(allY)
maxY = max(allY)


# create grid
gridSet = set()
grid = [["." for x in range(minX, maxX + 2)] for y in range(0, maxY + 2)]
for y in range(0, maxY + 2):
    for x in range(minX, maxX + 2):
        gridSet.add((x, y))


def displayGrid():
    for r in grid:
        for c in r:
            print(c, end="")
        print()
    print()


# graph lines
allPointRel = set()

for line in allLines:
    for pointNum in range(len(line) - 1):
        x, y = line[pointNum]
        c = x - minX
        r = y

        allPointRel.add((c, r))

        grid[r][c] = "#"

        dl = [line[pointNum + 1][0] - line[pointNum][0], line[pointNum + 1][1] - line[pointNum][1]]

        # draw change in x
        if (dl[0] != 0):
            if (dl[0] < 0):
                for dx in range(abs(dl[0])):
                    c -= 1
                    grid[r][c] = "#"
                    allPointRel.add((c, r))
            else:
                for dx in range(dl[0]):
                    c += 1
                    grid[r][c] = "#"
                    allPointRel.add((c, r))

        # draw change in y
        elif (dl[1] != 0):
            if (dl[1] < 0):
                for dy in range(abs(dl[1])):
                    r -= 1
                    grid[r][c] = "#"
                    allPointRel.add((c, r))

            else:
                for dy in range(dl[1]):
                    r += 1
                    grid[r][c] = "#"
                    allPointRel.add((c, r))


# --------------------------------------------

# sand filling
def sandDown(sandX, sandY):
    blockBelowAll = [[x, y] for [x, y] in allPointRel if x == sandX]

    if (blockBelowAll == []):
        print("Answer is", len(allSandLoc))

        assert False

    blockBelowAll.sort()
    for i in blockBelowAll:
        if (sandY < i[1]):
            sandC, sandR = i[0], i[1] - 1
            return [sandC, sandR]


# sand spawn
spawnPoint = [500, 0]
spawnC = spawnPoint[0] - minX
spawnR = spawnPoint[1]
grid[spawnR][spawnC] = "+"

sandC, sandR = spawnC, spawnR

allSandLoc = set()

iteration = 1

while True:
    [sandC, sandR] = sandDown(sandC, sandR)

    iteration = iteration + 1

    # check down left
    if ((sandC - 1, sandR + 1) not in allPointRel):
        sandC -= 1
        sandR += 1

    # check down right
    elif ((sandC + 1, sandR + 1) not in allPointRel):
        sandC += 1
        sandR += 1

    # fix sand. add to set and print "o"
    else:
        allSandLoc.add((sandC, sandR))
        allPointRel.add((sandC, sandR))
        grid[sandR][sandC] = "o"

        sandC, sandR = spawnC, spawnR


displayGrid()


# len(allSandLoc) at failure is 644
