# day 8 part 2


with open("day 8 input.txt", "r") as fid:
    totalGrid = fid.readlines()

# setup horizontal list and vertical list
horizontal = [list(i.strip()) for i in totalGrid]
horizontal = [[int(x) for x in j] for j in horizontal]


vertical = []
for j in range(len(horizontal[0])):
    tempList = []
    for i in range(len(horizontal)):
        tempList.append(horizontal[i][j])

    vertical.append(tempList)


# for every tree, check: left & right, up & down

overallRecord = 0

for i in range(1, len(horizontal) - 1):
    for j in range(1, len(horizontal[i]) - 1):

        treeHeight = horizontal[i][j]

        rightCount = 0
        leftCount = 0
        upCount = 0
        downCount = 0

        # checking to the right
        for k in horizontal[i][j + 1:]:
            if (k < treeHeight):
                rightCount += 1
            else:
                rightCount += 1
                break

        # checking to the left
        for l in reversed(horizontal[i][:j]):
            if (l < treeHeight):
                leftCount += 1
            else:
                leftCount += 1
                break

        # checking down
        for m in vertical[j][i + 1:]:
            if (m < treeHeight):
                downCount += 1
            else:
                downCount += 1
                break

        # checking up
        for n in reversed(vertical[j][:i]):
            if (n < treeHeight):
                upCount += 1
            else:
                upCount += 1
                break

        # save the value if highest so far
        roundTotal = rightCount * leftCount * upCount * downCount
        if (roundTotal > overallRecord):
            overallRecord = roundTotal

print("Highest scenic score is", overallRecord)
