# day 4 part 1

#read in data
with open("day 4 input.txt", "r") as fid:
    dataList = fid.readlines()


count = 0

for row in dataList:
    row = row.split(",")

    elf1 = row[0].split("-")

    elf2 = row[1].split("-")

    # create list of each elf's IDs
    elf1Range = set(range(int(elf1[0]), int(elf1[1]) + 1))

    elf2Range = set(range(int(elf2[0]), int(elf2[1]) + 1))

    # compare IDs
    intersection = elf1Range.intersection(elf2Range)
    if (intersection == elf2Range or intersection == elf1Range):
        count += 1
