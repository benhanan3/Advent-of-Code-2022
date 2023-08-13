
# day 13 part 1

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


I = []
for groupNum in range(len(data)):
    p1, p2 = data[groupNum].split("\n")
    p1 = eval(p1)
    p2 = eval(p2)

    if (compare(p1, p2) == 1):
        I.append(groupNum + 1)


print("Answer is", sum(I))
