# day 3 part 1 find which lettr is in both first and second half of sring, add up priority


with open("day3inputdata.txt", "r") as fid:

    dataRead = fid.readlines()


prioritySum = 0

for line in dataRead:
    line = list(line)

    if (line[-1] == " "):
        del line[-1]

    halfLength = int(len(line) / 2)

    firstBag = line[:halfLength]
    secondBag = line[halfLength:]

    # set () gets rid of duplicates
    for i in set(firstBag):
        if (i in secondBag):
            # A is 65
            # Z is 90
            # a is 97
            # z is 122

            if (97 <= ord(i) <= 122):
                priority = ord(i) - 96

            elif (65 <= ord(i) <= 90):
                priority = ord(i) - 38

            prioritySum += priority

            # print(i)
            # print(priority)


print(prioritySum)
