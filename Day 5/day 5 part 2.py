# day 5 part 1

with open("day 5 input.txt", "r") as fid:
    stackStrings, instructions = (i.splitlines() for i in fid.read().strip("\n").split("\n\n"))


stacks = {int(digit): [] for digit in stackStrings[-1].replace(" ", "")}
#indexes = [index for index, char in enumerate(stackStrings[-1]) if char != " "]

# my index solution
indexes = []
for i in range(len(stackStrings[-1])):
    if (stackStrings[-1][i] != " "):
        indexes.append(i)

# sort crates into dictionary
# top boxes at end of list

for row in stackStrings[:-1]:
    column = 1
    for index in indexes:
        if (row[index] != " "):
            stacks[column].insert(0, row[index])

        column += 1


# interpret move request
for line in instructions:
    quantity = int(line.split()[1])
    fromLoc = int(line.split()[3])
    toLoc = int(line.split()[5])

    # execute all moves
    # find box value wit "from location"
    moveBox = stacks[fromLoc][-quantity:]

    del stacks[fromLoc][-quantity:]
    # insert "box value" at start of list with "to location" key
    stacks[toLoc].extend(moveBox)


# count final configuration
finalConfig = ""
for stack in stacks:
    finalConfig += str(stacks[stack][-1])

print("Answer: " + finalConfig)
