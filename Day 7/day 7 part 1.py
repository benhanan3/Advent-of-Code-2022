
# day 7 part 1

with open("day 7 input test.txt", "r") as fid:
    commandList = fid.readlines()


masterDir = {}
line = 0  # normal counting
for command in commandList:
    line += 1
    dirName = ""
    if ("$ cd" in command):
        # move out
        if (".." in command):

            # move in
        else:
            directoryName = command.split()[-1]

            if (directoryName not in masterDir.keys()):
                masterDir[directoryName] = []

    if ("$ ls" in command):
        lineFind = line + 1
        for j in commandList[line:]:
            if ("$" in command):
                lineFindEnd = lineFind
                break
            lineFind += 1

        for k in commandList[line:lineFindEnd]:
            if ("dir" in k):
