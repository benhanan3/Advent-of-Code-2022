# day 8 part 1


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


# iterate through the row, checking if visible from one direction
# check horizontal, for trees not visible, add index to list
# for trees that are visible, add to count

indexFromHorizontal = []
visibleTreesCount = 0


# only checks middle trees
for i in range(1, len(horizontal) - 1):
    for j in range(1, len(horizontal[i]) - 1):
        left = set(horizontal[i][:j])
        right = set(horizontal[i][j + 1:])

        if (horizontal[i][j] > max(left) or horizontal[i][j] > max(right)):
            visibleTreesCount += 1
        else:
            indexFromHorizontal.append([j, i])


# check vertical visibility for trees with no previous visibility
for i in range(len(indexFromHorizontal)):
    xCoord = indexFromHorizontal[i][0]
    yCoord = indexFromHorizontal[i][1]

    above = set(vertical[xCoord][:yCoord])
    below = set(vertical[xCoord][yCoord + 1:])

    if (vertical[xCoord][yCoord] > max(above) or vertical[xCoord][yCoord] > max(below)):
        visibleTreesCount += 1

# add perimeter tree count
perimeter = (2 * len(vertical)) + (2 * (len(horizontal) - 2))
visibleTreesCount += perimeter

print("There are", visibleTreesCount, "visible trees")
