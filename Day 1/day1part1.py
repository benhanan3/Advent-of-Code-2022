

with open("day1input.txt", "r") as fid:
    dataList = fid.readlines()

splitList = [[]]


# split the list into lists of list per elf
for value in dataList:
    if ((len(value)) > 1):
        splitList[-1].append(int(value))
    else:
        splitList.append([])


mostCal = 0


# sum each list of calories, only hold if its the greatest
for elfLoad in splitList:
    calTotal = sum(elfLoad)

    if calTotal > mostCal:
        mostCal = calTotal

print(mostCal)
