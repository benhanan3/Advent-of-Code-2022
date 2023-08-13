#day 18 part 1

def countSides(coord):
    # check +- y and +- z
    exposedSurface = 0
    x = coord[0]
    y = coord[1]
    z = coord[2]

    if (x, y + 1, z) not in data:
        exposedSurface += 1

    if (x, y - 1, z) not in data:
        exposedSurface += 1

    if (x, y, z + 1) not in data:
        exposedSurface += 1
    
    if (x, y, z - 1) not in data:
        exposedSurface += 1

    if (x + 1, y, z) not in data:
        exposedSurface += 1

    if (x - 1, y, z) not in data:
        exposedSurface += 1

    return(exposedSurface)


with open("input test.txt", "r") as fid:
    data = fid.read().strip().split("\n")
    
    for i in range(len(data)):
        stringSplit = data[i].split(",")
        data[i] = (int(stringSplit[0]), int(stringSplit[1]), int(stringSplit[2]))


# x from right to left.
# y into screen
# z up

surfaceArea = 0
counted = set()

for coord in data:

    if (coord not in counted):
        counted.add(coord)
        surfaceArea += countSides(coord)

print(surfaceArea)