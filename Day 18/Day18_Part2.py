# day 18 part 2
# exterior surface area only

def check_flood_fill(coord):
    SEEN = set()
    Q = [coord]

    while Q:
        (x, y, z) = Q.pop(0)
        coord = (x, y, z)

        if (len(SEEN) > 5000) or (coord in OUTSIDE):
            OUTSIDE.update(SEEN)
            return 1
        
        if (coord in INSIDE):
            return 0
        
        if coord in data:
            continue
        if coord in SEEN:
            continue
        
        SEEN.add(coord)
        
        for d in range(1,-2,-2):
            Q.append((x + d, y, z))
            Q.append((x, y + d, z))
            Q.append((x, y, z + d))

    INSIDE.update(SEEN)
    return 0


with open("input.txt", "r") as fid:
    data = fid.read().strip().split("\n")
    
    for i in range(len(data)):
        stringSplit = data[i].split(",")
        data[i] = (int(stringSplit[0]), int(stringSplit[1]), int(stringSplit[2]))
    
    data = set(data)


SA = 0

INSIDE = set()
OUTSIDE = set()

for blockCoord in data:
    (x, y, z) = blockCoord
    
    for d in range(1,-2,-2):
        SA += check_flood_fill((x + d, y, z))
        SA += check_flood_fill((x, y + d, z))
        SA += check_flood_fill((x, y, z + d))

print(SA)