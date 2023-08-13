
def moveRight(startIndex, moveValue):    
    moveValue %= (length - 1)
    i = 0
    while i < moveValue + 1:
        next = startIndex + i + 1
        current = startIndex + i

        if ((next) > (length - 1)):
            next %= length
            current %= length
        
        if (current == (length - 1)):
            lastItem = orderedList.pop()
            orderedList.insert(0, lastItem)
            i += 1
            moveValue += 1
            displayOutput()
            continue

        temp = orderedList[next]
        orderedList[next] = orderedList[current]
        orderedList[current] = temp
        i += 1
        displayOutput()


def moveLeft(startIndex, moveValue):
    moveValue = abs(moveValue)
    moveValue %= (length - 1)
    i = 0
    while i < moveValue + 1:
        next = startIndex - i - 1
        current = startIndex - i

        if (next < 0):
            next = length - (abs(next) % length)
            current = (next + 1) % length

        if current == 0:
            firstItem = orderedList.pop(0)
            orderedList.append(firstItem)
            i += 1
            continue

        temp = orderedList[next]
        orderedList[next] = orderedList[current]
        orderedList[current] = temp
        i += 1

def displayOutput():
    ans = [x[1] for x in orderedList]
    print(ans)


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

startList = []

with open("input-test.txt", "r") as fid:
    data = fid.read().strip().split("\n")
    data = [int(x) for x in data]

    for index, value in enumerate(data):
        startList.append([index, value])  # index, value

orderedList = startList.copy()
length = len(startList)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

for i in range(length):
    item = startList[i]
    moveValue = item[1]

    startIndex = orderedList.index(item)

    if moveValue > 0:
        moveRight(startIndex, moveValue)
    
    elif moveValue < 0:
        moveLeft(startIndex, moveValue)

    if i % 100 == 0 and i != 0:
        print(i)

    print("layer done")
    displayOutput()


print("done\n\n")
displayOutput()

itemWith0 = [x for x in orderedList if x[1] == 0][0]
searchStartIndex = orderedList.index(itemWith0)

found = []

for find in [1000, 2000, 3000]:
    findIndex = (find % length + searchStartIndex) % length
    found.append(orderedList[findIndex][1])    

print(found)
ans = sum(found)
print(ans)
