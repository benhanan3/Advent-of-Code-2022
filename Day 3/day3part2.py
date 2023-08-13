# day 3 part 1 find which lettr is in both first and second half of sring, add up priority


with open("day3inputdata.txt", "r") as fid:

    dataRead = fid.readlines()


cleanDataRead = []

for line in dataRead:
    line = list(line)
    if (line[-1] == "\n"):
        del line[-1]
    cleanDataRead.append(line)


numGroups = range((int(len(cleanDataRead) / 3)))

prioritySum = 0

for i in numGroups:
    group = cleanDataRead[(3 * i):((3 * (i + 1)))]

    for i in set(group[0]):
        if (i in group[1] and i in group[2]):
            if (97 <= ord(i) <= 122):
                priority = ord(i) - 96

            elif (65 <= ord(i) <= 90):
                priority = ord(i) - 38

            prioritySum += priority

            print(i)
            print(priority)

print(prioritySum)
