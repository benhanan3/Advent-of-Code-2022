
# day 13 part 2

with open("day 13 input.txt", "r") as fid:
    data = fid.read().strip()

data = data.split("\n\n")


def compare(p1, p2):

    if (isinstance(p1, int) and isinstance(p2, int)):
        if (p1 < p2):
            return 1

        elif (p1 == p2):
            return 0

        elif (p1 > p2):
            return -1

    elif (isinstance(p1, list) and isinstance(p2, list)):
        i = 0
        while (i < len(p1) and i < len(p2)):
            c = compare(p1[i], p2[i])
            if (c == -1):
                return -1

            elif (c == 1):
                return 1

            i += 1

        if ((i < len(p1)) and (i == len(p2))):
            return -1

        if ((i == len(p1)) and (i < len(p2))):
            return 1

        else:
            return 0

    elif (isinstance(p1, int) and isinstance(p2, list)):
        return compare([p1], p2)

    elif (isinstance(p1, list) and isinstance(p2, int)):
        return compare(p1, [p2])


'''
correctOrderedList = []
for groupNum in range(len(data)):
    p1, p2 = data[groupNum].split("\n")
    p1 = eval(p1)
    p2 = eval(p2)

    if (compare(p1, p2) == 1):
        correctOrderedList.append(groupNum + 1)


print("Answer is", sum(correctOrderedList))
'''


allP = []
for group in data:
    p1, p2 = group.split("\n")
    allP.append(eval(p1))
    allP.append(eval(p2))

allP.extend([[2], [6]])


# sorting algo
for i in range(len(allP)):
    for j in range(len(allP) - 1):
        if (compare(allP[j], allP[j + 1]) == -1):
            allP[j], allP[j + 1] = allP[j + 1], allP[j]

# find divider packets
index1 = allP.index([2]) + 1
index2 = allP.index([6]) + 1

print("Answer is", index1 * index2)
