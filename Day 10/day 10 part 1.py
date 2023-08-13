# day 10 part 1


with open("day 10 input.txt", "r") as fid:
    commands = fid.readlines()


x = 1
cycle = 1
checkList = [20, 60, 100, 140, 180, 220]
requestedValues = []

for i in range(len(commands)):

    if ("noop" in commands[i]):
        cycle += 1

    elif ("addx" in commands[i]):
        v = int(commands[i].split()[1])

        cycle += 1
        if (cycle in checkList):
            requestedValues.append(x)

        x += v
        cycle += 1

    if (cycle in checkList):
        requestedValues.append(x)


signalStrength = [checkList[x] * requestedValues[x] for x in range(len(checkList))]

total = sum(signalStrength)

print("Answer is", total)
