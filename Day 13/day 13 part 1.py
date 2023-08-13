
# day 13 part 1

with open("day 13 input.txt", "r") as fid:
    data = fid.read().strip()

data = data.split("\n\n")

I = []
for groupNum in range(len(data)):
    p1, p2 = data[groupNum].split("\n")
    p1 = eval(p1)
    p2 = eval(p2)

    order = True
    for i in range(len(p1)):
        try:
            p2[i]
            if (type(p1[i]) == int):
                if (type(p2[i]) == int):
                    if (p1[i] > p2[i]):
                        order = False

                else:
                    if (p1[i] > p2[i][0]):
                        order = False

                if (p1[i] > int(p2[i])):
                    order = False

            elif (type(p1[i]) == list):
                if(type(p2[i]) == list):
                    for j in range(len(p1[i])):
                        try:
                            p2[i][j]
                            if (p1[i][j] > p2[i][j]):
                                order = False
                        except:
                            order = False
                else:
                    if (p1[i][0] > p2[i]):
                        order = False

                    if ((p1[i][0] == p2[i]) and (len(p1[i]) > 1)):
                        order = False

        except IndexError:
            order = False

    if (order and (len(p1) <= len(p2))):
        I.append(groupNum + 1)

print("Answer is", sum(I))
