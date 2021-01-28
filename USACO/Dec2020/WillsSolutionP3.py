def sortCoorinateListByX(elements):
    sortedList = []
    while(len(elements) > 0):
        minx = float('inf')
        for i in range(len(elements)):
            minx = min(minx, elements[i][0])

        for i in range(len(elements)-1, -1, -1):
            if(elements[i][0] == minx):
                sortedList.append(elements[i])
                elements.remove(elements[i])
    return sortedList

def sortCoorinateListByY(elements):
    sortedList = []
    while(len(elements) > 0):
        miny = float('inf')
        for i in range(len(elements)):
            miny = min(miny, elements[i][1])

        for i in range(len(elements)-1, -1, -1):
            if(elements[i][1] == miny):
                sortedList.append(elements[i])
                elements.remove(elements[i])
    return sortedList




N = int(input())

cowDistances = dict()

cows = []
eastCows = []
northCows = []

for i in range(N):
    cowDistances[i] = "Infinity"

    cowData = input().split()
    cowData[1] = int(cowData[1])
    cowData[2] = int(cowData[2])
    cows.append(cowData)
    if(cowData[0] == "E"):
        eastCows.append([cowData[1], cowData[2], i])
    else:
        northCows.append([cowData[1], cowData[2], i])

eastCows = sortCoorinateListByY(eastCows)
northCows = sortCoorinateListByX(northCows)

intersections = []
intersectionPairs = dict()

for i in range(len(northCows)):
    for t in range(len(eastCows)):
        if(northCows[i][0] >= eastCows[t][0] and northCows[i][1] <= eastCows[t][1]):
            intersections.append([northCows[i][0], eastCows[t][1]])
            key = str(northCows[i][0]) + " " + str(eastCows[t][1])
            if(key not in intersectionPairs):     
                intersectionPairs[key] = set()
            intersectionPairs[key].add(northCows[i][2])
            intersectionPairs[key].add(eastCows[t][2])

eastMaxes = dict()
for i in range(len(eastCows)-1):
    if(eastCows[i][0] == eastCows[i+1][0]):
        if(eastCows[i][1] > eastCows[i+1][1]):
            if(eastCows[i+1][2] not in eastMaxes):
                eastMaxes[eastCows[i+1][2]] = eastCows[i][1] - eastCows[i+1][1]
            else:
                 eastMaxes[eastCows[i+1][2]] = min(eastMaxes[i+1], eastCows[i][1] - eastCows[i+1][1])
        else:
            if(i not in eastMaxes):
                eastMaxes[eastCows[i][2]] = eastCows[i+1][1] - eastCows[i][1]
            else:
                 eastMaxes[eastCows[i][2]] = min(eastMaxes[i], eastCows[i+1][1] - eastCows[i][1])

northMaxes = dict()
for i in range(len(northCows)-1):
    if(northCows[i][0] == northCows[i+1][0]):
        if(northCows[i][1] > northCows[i+1][1]):
            if(northCows[i+1][2] not in northMaxes):
                northMaxes[northCows[i+1][2]] = northCows[i][1] - northCows[i+1][1]
            else:
                 northMaxes[northCows[i+1][2]] = min(northMaxes[i+1], northCows[i][1] - northCows[i+1][1])
        else:
            if(i not in northMaxes):
                northMaxes[northCows[i][2]] = northCows[i+1][1] - northCows[i][1]
            else:
                 northMaxes[northCows[i][2]] = min(northMaxes[i], northCows[i+1][1] - northCows[i][1])

maxes = dict()
maxes.update(eastMaxes)
maxes.update(northMaxes)

for i in range(len(intersections)):
    key = str(intersections[i][0]) + " " + str(intersections[i][1])
    collidingCows = list(intersectionPairs[key])

    if (len(collidingCows) > 2):
        minXDist = float('inf')
        minYDist = float('inf')
        northCow = 0
        eastCow = 0
        for c in range(len(collidingCows)):
            if(cows[collidingCows[c]][0] == "N"):
                if(minYDist > intersections[i][1] - cows[collidingCows[c]][2]):
                    minYDist = intersections[i][1] - cows[collidingCows[c]][2]
                    northCow = collidingCows[c]
            else:
                if(minXDist > intersections[i][0] - cows[collidingCows[c]][1]):
                    minXDist = intersections[i][0] - cows[collidingCows[c]][1]
                    eastCow = collidingCows[c]
        collidingCows = [northCow, eastCow]

    if(cowDistances[collidingCows[0]] == "Infinity" and cowDistances[collidingCows[1]] == "Infinity"):
        northCow = []
        eastCow = []
        northCowIndex = 0
        eastCowIndex = 0
        if(cows[collidingCows[0]][0] == "N"):
            northCow = cows[collidingCows[0]]
            eastCow = cows[collidingCows[1]]
            northCowIndex = collidingCows[0]
            eastCowIndex = collidingCows[1]
        else:
            northCow = cows[collidingCows[1]]
            eastCow = cows[collidingCows[0]]
            northCowIndex = collidingCows[1]
            eastCowIndex = collidingCows[0]

        xDist = intersections[i][0] - eastCow[1]
        yDist = intersections[i][1] - northCow[2]

        if(xDist > yDist):
            cowDistances[eastCowIndex] = xDist
        elif(yDist > xDist):
            cowDistances[northCowIndex] = yDist

for i in range(N):
    if(i in maxes):
        if(cowDistances[i] == "Infinity"):
            cowDistances[i] = maxes[i]
        else:
            cowDistances[i] = min(cowDistances[i], maxes[i])

for i in range(N):
    print(cowDistances[i])


