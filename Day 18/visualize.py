import matplotlib.pyplot as plt
import numpy as np

with open("input.txt", "r") as fid:
    data = fid.read().strip().split("\n")
    
    for i in range(len(data)):
        stringSplit = data[i].split(",")
        data[i] = (int(stringSplit[0]), int(stringSplit[1]), int(stringSplit[2]))


maxX = max([x for (x,y,z) in data])
maxY = max([y for (x,y,z) in data])
maxZ = max([z for (x,y,z) in data])
max = max((maxX, maxY, maxZ))
max = (max, max, max)

array = np.zeros(max)  # 0 based

for (x,y,z) in data:
    array[x-1,y-1,z-1] = 1


ax = plt.axes(projection='3d')
ax.voxels(array, edgecolor='k')

plt.show()



