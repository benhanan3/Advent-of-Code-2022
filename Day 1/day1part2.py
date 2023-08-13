# find the total calories carried by top three elves

with open("day1input.txt", "r") as fid:
    dataList = fid.readlines()

splitList = [[]]


# split the list into lists of list per elf
for value in dataList:
    if ((len(value)) > 1):
        splitList[-1].append(int(value))
    else:
        splitList.append([])


topThreeCal = [0, 0, 0]


# sum each list of calories, add to list of three by deleting min if greater than min
for elfLoad in splitList:
    calTotal = sum(elfLoad)

    if calTotal > min(topThreeCal):
        minValue = topThreeCal.index(min(topThreeCal))

        del topThreeCal[minValue]

        topThreeCal.append(calTotal)

sum(topThreeCal)

print(sum(topThreeCal))
