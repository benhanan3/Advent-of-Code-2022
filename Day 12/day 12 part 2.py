# day 12 part 2

import collections

with open("day 12 input.txt", "r") as fid:
    data = fid.readlines()


letterList = [list(i.strip()) for i in data]


Q = []
for r in range(len(letterList)):
    for c in range(len(letterList[0])):

        if (letterList[r][c] == "S"):
            Q.append(((r, c), 0))
        if (letterList[r][c] == "a"):
            Q.append(((r, c), 0))

E = [[0 for j in i] for i in letterList]
for r in range(len(letterList)):
    for c in range(len(letterList[0])):

        if (letterList[r][c] == "S"):
            E[r][c] = 1
        elif (letterList[r][c] == "E"):
            E[r][c] = 26
        else:
            E[r][c] = ord(letterList[r][c]) - ord("a") + 1

S = set()
while Q:
    (r, c), d = Q.pop(0)

    print((r, c), d)

    if (r, c) in S:
        continue

    S.add((r, c))

    if (letterList[r][c] == "E"):
        print("Answer is ", d)
        assert False

    for (dr, dc) in [(1, 0), (0, -1), (0, 1), (-1, 0)]:
        rr = r + dr
        cc = c + dc
        if ((0 <= rr < len(letterList)) and (0 <= cc < len(letterList[0])) and ((E[rr][cc] - E[r][c]) <= 1)):
            Q.append(((rr, cc), d + 1))
