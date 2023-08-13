# Import Data
import numpy as np
fid = open("input.txt", "r")
fileAll = fid.readlines()
fid.close()

inputLine = 2000000  # where to check (y-level)

# 10 used for test case
# 2000000 used for part 1

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# put together list of sensor and beacon locations, stored together
# ((sensorX, sensorY),(beaconX, beaconY), dist)
# dist denotes the "radius" between the beacon and signal

sensorBeaconList = []  # holds sensor tuple and beacon tuple
sensorBeaconDistList = []  # holds tuple with tuple of sensor, tuple of beacon, and int of distance

entireMapX = []  # stores the coordinates of all sensor & beacons, used to find maxes and mins
maxDist = 0  # used to find the max distance in order to add to the max and min values

for line in fileAll:
    sensor, beacon = line.split(": ")
    sensorX, sensorY = sensor.removeprefix("Sensor at x=").split(", y=")
    beaconX, beaconY = beacon.removeprefix("closest beacon is at x=").split(", y=")

    relativeVectorSB = (abs(int(beaconX) - int(sensorX)), abs(int(beaconY) - int(sensorY)))
    dist = relativeVectorSB[0] + relativeVectorSB[1]

    if (dist > maxDist):
        maxDist = dist

    entireMapX.append(int(sensorX))
    entireMapX.append(int(beaconX))
    sensorBeaconDistList.append(((int(sensorX), int(sensorY)), (int(beaconX), int(beaconY)), dist))

    sensorBeaconList.append((int(sensorX), int(sensorY)))
    sensorBeaconList.append((int(beaconX), int(beaconY)))

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# creates matrix of entire map

xMax = max(entireMapX) + maxDist
xMin = min(entireMapX) - maxDist

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# For all points at a given line, find all squares where

invalidSquare = 0  # tracks how many places the signal cannot be
invalidSquareList = []

for x in range(xMin, xMax + 1):
    squareCoord = (x, inputLine)

    if (squareCoord in sensorBeaconList):
        continue  # next cycle of above for loop. doesnt count as an invalid square

    # for every square, we check every sensor's range
    for pair in sensorBeaconDistList:
        relativeVector = (squareCoord[0] - pair[0][0], squareCoord[1] - pair[0][1])
        distSquareSensor = abs(relativeVector[0]) + abs(relativeVector[1])

        if (distSquareSensor <= pair[2]):
            invalidSquare += 1
            invalidSquareList.append(squareCoord)
            break  # won't need to check any other sensors because the square is already searched

print("There are {} invalid squares at y level {}".format(invalidSquare, inputLine))

# Answer is 5125700
