import random
from time import sleep
rowNum = 11
colNum = 20
playerCol = random.randint(1, 5)
playerRow = random.randint(1, 5)
playerDir = ""
inputList = [
    "up",
    "w",
    "down",
    "s",
    "left",
    "a",
    "right",
    "d"
]


def createMap():
    mapFinal = []
    grassList = [".", "_", "-"]
    for row in range(0,rowNum):
        rowList = []
        for column in range(0,colNum):
            if column == playerCol-1 and row == playerRow-1:
                rowList.append("@")
            else:
                rowList.append(".")
        mapFinal.append(rowList)
    printMap(mapFinal)

def printMap(mapFinal):
    for rowList in mapFinal:
        #print(rowList)
        print(" ".join(rowList))

#def checkDir(direc):


while playerDir != "exit":
    createMap()
    #for debugging purposes
    #print(playerRow, playerCol)
    playerDir = input("please input a direction, or w, a, s, and d ")
    #checkDir(playerDir)
    if playerDir == inputList[0] or playerDir == inputList[1]:
        playerRow -= 1
    elif playerDir == inputList[2] or playerDir == inputList[3]:
        playerRow += 1
    elif playerDir == inputList[4] or playerDir == inputList[5]:
        playerCol -= 1
    elif playerDir == inputList[6] or playerDir == inputList[7]:
        playerCol += 1
    elif playerDir == "exit":
        pass
    else:
        print("ERROR that was either not a direction or something else. try again.")
        sleep(1)