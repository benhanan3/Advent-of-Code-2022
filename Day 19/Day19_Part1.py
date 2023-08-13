import itertools

def build_ore(ore, oreBot, buildOre):
    ore -= buildOre
    oreBot += 1
    return ore, oreBot

def build_clay(ore, clayBot, buildClay):
    ore -= buildClay
    clayBot += 1
    return clay, clayBot

def build_obs(ore, clay, obsBot, buildObs):
    ore -= buildObs[0]
    clay -= buildObs[1]
    obsBot += 1
    return ore, clay, obsBot

def build_geode(ore, obs, geodeBot, buildGeode):
    ore -= buildGeode[0]
    obs -= buildGeode[1]
    geodeBot += 1
    return ore, obs, geodeBot

def create_turn_structure():
    return {"ore": ore, "clay": clay, "obs": obs, "geode": geode, "buildOre": buildOre, "buildClay": buildClay, "buildObs": buildObs, "buildGeode": buildGeode, "oreBot": oreBot, "clayBot": clayBot, "obsBot": obsBot, "geodeBot": geodeBot, "turn": turnNum}

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

with open("input-test.txt", "r") as fid:
    data = fid.readlines()

BPList = []

#Segregates into Blueprint blocks. Does not include BP line
for i in range(len(data)):
    string = data[i]
    if "Blueprint" in string:
        BPList.append(data[i+1:i+5])

# separated by blueprint blocks
for BPnum in range(len(BPList)):
    stringList = BPList[BPnum]  # list of all BP sublines

    buildOre = [int(s) for s in stringList[0].split() if s.isdigit()]  # ore
    buildClay = [int(s) for s in stringList[1].split() if s.isdigit()] # ore
    buildObsidian = [int(s) for s in stringList[2].split() if s.isdigit()] # ore, clay
    buildGeode = [int(s) for s in stringList[3].split() if s.isdigit()] # ore, obsidian

    # -=-=-=-=-=- LIST FORMAT -=-=-=-=-=-
    BPList[BPnum] = [buildOre[0], buildClay[0], buildObsidian, buildGeode]

geodeStore = {}  # stores best geode count for every BP
allGeodeBP = []  # stores all geode counts for every BP

# iterates through every BP
for BPnum in range(len(BPList)):
    
    # -=-=-=-=-=- UNPACK BP DATA, CREATE DICT -=-=-=-=-=-
    BP = BPList[BPnum]  # stores individual BP's data
    
    buildOre = BP[0]
    buildClay = BP[1]
    buildObs = BP[2]
    buildGeode = BP[3]

    # initial conditions
    ore = 0
    clay = 0
    obs = 0
    geode = 0

    oreBot = 1
    clayBot = 0
    obsBot = 0
    geodeBot = 0

    turnNum = 1

    # -=-=-=-=-=- DATA STRUCTURE -=-=-=-=-=-
    # copied the value into the dictionary. Not a pointer
    turn0 = {"ore": ore, "clay": clay, "obs": obs, "geode": geode, "buildOre": buildOre, "buildClay": buildClay, "buildObs": buildObs, "buildGeode": buildGeode, "oreBot": oreBot, "clayBot": clayBot, "obsBot": obsBot, "geodeBot": geodeBot, "turn": turnNum}

    Q = [turn0]

    #DFS through this BP configuration
    while Q:
        # -=-=-=-=-=- UNPACK TURN DATA -=-=-=-=-=-
        turn = Q.pop()

        ore = turn["ore"]
        clay = turn["clay"]
        obs = turn["obs"]
        geode = turn["geode"]

        buildClay = turn["buildClay"]
        buildOre = turn["buildOre"]
        buildObs = turn["buildObs"]
        buildGeode = turn["buildGeode"]

        oreBot = turn["oreBot"]
        clayBot = turn["clayBot"]
        obsBot = turn["obsBot"]
        geodeBot = turn["geodeBot"]

        turnNum = turn["turn"]
        
        if (turnNum == 24):
            allGeodeBP.append(geode)
            continue
            
        # -=-=-=-=-=- INCREMENT RESOURCES -=-=-=-=-=-
        ore += oreBot
        clay += clayBot
        obs += obsBot
        geode += geodeBot

        turnNum += 1

        turn = create_turn_structure()

        # can build ore robot? default no.
        canBuildOre = False
        canBuildClay = False
        canBuildObs = False
        canBuildGeode = False

        # -=-=-=-=-=- CAN BUILD? -=-=-=-=-=-
        if (ore >= buildOre):
            canBuildOre = True

        if (ore >= buildClay):
            canBuildClay = True

        if (ore >= buildObs[0]) and (clay > buildObs[1]):
            canBuildObs = True

        if (ore >= buildGeode[0]) and (obs >= buildGeode[1]):
            canBuildGeode = True


        # -=-=-=-=-=- CREATE ALL OPTIONS -=-=-=-=-=-
        binaryOptions = list(itertools.product([0, 1], repeat=4))

        if (canBuildOre == False):
            binaryOptions = [x for x in binaryOptions if x[0] == 0]
        
        if (canBuildClay == False):
            binaryOptions = [x for x in binaryOptions if x[1] == 0]

        if (canBuildObs == False):
            binaryOptions = [x for x in binaryOptions if x[2] == 0]

        if (canBuildGeode == False):
            binaryOptions = [x for x in binaryOptions if x[3] == 0]

        altTurn = turn.copy()
        for option in binaryOptions:
            if option[0] == 1:
                altTurn["ore"], altTurn["oreBot"] = build_ore(ore, oreBot, buildOre)
                
            if option[1] == 1:
                altTurn["ore"], altTurn["clayBot"] = build_clay(ore, clayBot, buildClay)

            if option[2] == 1:
                altTurn["ore"], altTurn["clay"], altTurn["obsBot"] = build_obs(ore, clay, obsBot, buildObs)

            if option[3] == 1:
                altTurn["ore"], altTurn["obs"], altTurn["geodeBot"] = build_geode(ore, obs, geodeBot, buildGeode)
        
            Q.append(altTurn.copy())


    geodeStore["BP" + str(BPnum)] = max(allGeodeBP)

print(geodeStore)

            

