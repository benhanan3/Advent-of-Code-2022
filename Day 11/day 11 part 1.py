# day 11 part 1
import math

with open("day 11 input.txt", "r") as fid:
    data = fid.read().strip()


monkeys = data.split("\n\n")
monkeys = [i.split("\n") for i in monkeys]

monkDict = {int(monkeys[i][0].split()[1].replace(":", "")):
            [monkeys[i][1].split(":")[1].strip().split(", "),
             monkeys[i][2].split("= ")[1].strip(),
             int(monkeys[i][3].split()[3].strip()),
             int(monkeys[i][4].split()[5].strip()),
             int(monkeys[i][5].split()[5].strip()), 0] for i in range(len(monkeys))}


for roundNum in range(20):
    for turn in range(len(monkDict)):

        monkDict[turn][5] += len(monkDict[turn][0])

        for item in range(len(monkDict[turn][0])):

            operation = monkDict[turn][1]
            divBy = monkDict[turn][2]

            old = int(monkDict[turn][0][0])
            new = math.floor(eval(operation) / 3)

            tossedItem = new
            del monkDict[turn][0][0]
            ifTrueMonkey = monkDict[turn][3]
            ifFalseMonkey = monkDict[turn][4]

            if (new % divBy == 0):
                monkDict[ifTrueMonkey][0].append(tossedItem)
            else:
                monkDict[ifFalseMonkey][0].append(tossedItem)


inspectCount = [monkDict[monkey][5] for monkey in monkDict]

greatest = max(inspectCount)
inspectCount.remove(greatest)
great2 = max(inspectCount)

monkBusiness = greatest * great2

print("Monkey Business is: ", monkBusiness)
