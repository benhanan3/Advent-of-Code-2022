# day 10 part 1
import math

with open("day 10 input.txt", "r") as fid:
    commands = fid.readlines()


x = 1
cycle = 1

crt = [["." for j in range(40)] for i in range(6)]


def render():
    for k in crt:
        for l in k:
            print(l, end="")
        print()


def draw():
    rowNum = math.floor((cycle - 1) / 40)
    posNum = cycle - (rowNum * 40) - 1
    if (abs(x - posNum) <= 1):
        crt[rowNum][posNum] = "#"


for i in range(len(commands)):

    draw()

    if ("noop" in commands[i]):
        cycle += 1

    elif ("addx" in commands[i]):
        v = int(commands[i].split()[1])

        cycle += 1

        draw()

        x += v
        cycle += 1


render()
