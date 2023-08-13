
# day 7 part 1

with open("day 7 input test.txt", "r") as fid:
    commandList = fid.readlines()


class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.dirs = []
        self.files = []

    def __str__(self):
        # return self.name + " " + str(len(self.dirs)) + " " + str(len(self.files))
        return F"{self.name} {len(self.dirs)} {len(self.files)} {self.getTotalSize()}"

    def addDirectory(self, newDirName):
        newDir = Directory(newDirName, self)
        self.dirs.append(newDir)

    def addFile(self, newFileName, fileSize):
        newFile = File(newFileName, fileSize)
        self.files.append(newFile)

    def getTotalSize(self):
        fileTotal = 0
        for file in self.files:
            fileTotal += file.size

        dirTotal = 0
        for item in self.dirs:
            dirTotal += item.getTotalSize()

        return (fileTotal + dirTotal)


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


root = Directory("root", None)

root.addDirectory("a")

root.addFile(newFileName="b", fileSize=12345)

root.addFile("c", 3456)

print(root)
