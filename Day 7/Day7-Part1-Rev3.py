import re


class Directory:
    def __init__(self, dirName):
        self.dirName = dirName
        self.totalSize = 0
        self.childDir = {}
        self.childFiles = {}


    def add_dir(self, dirName):
        newDir = Directory(dirName)
        newDir.parentDir = self
        self.childDir.update({dirName: newDir})

    
    def add_file(self, fileName, fileSize):
        self.childFiles.update({fileName: fileSize})


    def get_total_file_size(self):
        for key in self.childFiles:
            self.totalSize += self.childFiles[key]

        for key in self.childDir:
            self.totalSize += self.childDir[key].get_total_file_size()
        
        return self.totalSize
        

    def part1(self):
        deleteDir = 0

        if self.totalSize <= 100000:
            deleteDir += self.totalSize

        for key in self.childDir:
            deleteDir += self.childDir[key].part1()

        return deleteDir
            

    def part2(self, spaceNeeded, smallestDir):

        if ((self.totalSize >= spaceNeeded) and (self.totalSize < smallestDir)):
            smallestDir = self.totalSize

        for key in self.childDir:
            smallestDir = self.childDir[key].part2(spaceNeeded, smallestDir)

        return smallestDir


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

with open("input.txt", "r") as fid:
    input = fid.readlines()
    del input[0]


currentDir = Directory("/")
rootDir = currentDir

for i in range(len(input)):
    line = input[i].strip()

    regex_result_cd = re.match(r"\$\scd\s(.+)", line)
    regex_result_ls = re.match(r"\$\sls", line)
    regex_result_dir = re.match(r"dir\s(.+)", line)
    regex_result_file = re.match(r"(\d+)\s(.+)", line)

    #  $ cd ()
    if regex_result_cd:
        dirName = regex_result_cd.group(1)

        if dirName == "..":
            try:
                currentDir = currentDir.parentDir
            except:
                print("FATAL: parent directory not found")

        else:
            try:
                currentDir = currentDir.childDir[dirName]
            except:
                print("FATAL: child directory not found")


    #  $ ls ()
    elif regex_result_ls:
        continue

    #  dir ()
    elif regex_result_dir:
        childDir = regex_result_dir.group(1)
        currentDir.add_dir(childDir)
        
    #  file
    elif regex_result_file:
        fileSize = int(regex_result_file.group(1))
        newFile = regex_result_file.group(2)

        currentDir.add_file(newFile, fileSize)


rootDir.get_total_file_size()


ans1 = rootDir.part1()
print(ans1)


spaceNeeded = -40000000 + rootDir.totalSize
print("space required: ", spaceNeeded)

ans2 = rootDir.part2(spaceNeeded, 70000000)
print(ans2)

