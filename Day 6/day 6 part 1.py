
# day 6 part 1

with open("day 6 input.txt", "r") as fid:
    dataString = fid.read().strip("\n")


lastValueList = ["a", "a", "a", "a"]

iteration = 1
for char in dataString:
    lastValueList.append(char)
    del lastValueList[0]

    if (iteration > 3 and len(set(lastValueList)) == 4):

        letterString = ""
        for letter in lastValueList:
            letterString += str(letter)

        packetLoc = dataString.index(letterString) + 4
        break

    iteration += 1

print("Answer: " + str(packetLoc))
