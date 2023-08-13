# Day 17 part 1

with open("input ex.txt", "r") as fid:
    data = list(fid.read().strip())

'''
####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##
'''

def get_piece(t, y): # set of (x,y) pairs
    if t==0:
        return set([(2,y), (3,y), (4,y), (5,y)])
    elif t == 1:
        return set([(3, y+2), (2, y+1), (3,y+1), (4,y+1), (3,y)])
    elif t == 2:
        return set([(2, y), (3,y), (4,y), (4,y+1), (4,y+2)])
    elif t==3:
        return set([(2,y),(2,y+1),(2,y+2),(2,y+3)])
    elif t==4:
        return set([(2,y+1),(2,y),(3,y+1),(3,y)])
    else:
        assert False

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def move_left(piece):
    if any([x==0 for (x,y) in piece]):
        return piece
    return set([(x-1,y) for (x,y) in piece])

def move_right(piece):
    if any([x==6 for (x,y) in piece]):
        return piece
    return set([(x+1,y) for (x,y) in piece])
def move_down(piece):
    return set([(x,y-1) for (x,y) in piece])
def move_up(piece):
    return set([(x,y+1) for (x,y) in piece])

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def illustrate():
    maxY = max([y for (x,y) in R])
    for y in range(maxY, 0, -1):
        row = ""
        for x in range(7):
            if (x,y) in R:
                row += "#"
            else:
                row += " "
        print(row)
    print()

R = set([(x,0) for x in range(7)])
top = 0

i = 0
for t in range(10000):
    piece = get_piece(t % 5, top + 4)

    while True:
        move = data[i]

        if move == ">":
            piece = move_right(piece)
            if piece & R:
                piece = move_left(piece)

        elif move == "<":
            piece = move_left(piece)
            if piece & R:
                piece = move_right(piece)

        else:
            print("ERROR")
            assert False

        i = (i+1) % len(data)
        piece = move_down(piece)
        if piece & R:
            piece = move_up(piece)
            R |= piece
            break
        
        top = max([y for (x,y) in R])
            
        
'''
print(top)

illustrate()

for t in range(10000):
    piece = get_piece(t%5, top+4)
    while True:
        # pushed -> down
        if data[i]=='<':
            piece = move_left(piece)
            if piece & R:
                piece = move_right(piece)
        else:
            piece = move_right(piece)
            if piece & R:
                piece = move_left(piece)
        i = (i+1)%len(data)
        piece = move_down(piece)
        if piece & R:
            piece = move_up(piece)
            R |= piece
            top = max([y for (x,y) in R])
            break
'''