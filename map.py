import random
rowNum = 10
colNum = 10
playerCol = random.randint(1, 5)
playerRow = random.randint(1, 5)
from time import sleep

def createMap():
    mapFinal = []
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
        print(rowList)

#def checkDir(direc):


while 1==1:
    createMap()
    #for debugging purposes
    #print(playerRow, playerCol)
    playerDir = input("please input a direction, or w, a, s, and d ")
    #checkDir(playerDir)
    if playerDir == "up" or playerDir == "w":
        playerRow -= 1
    elif playerDir == "down" or playerDir == "s":
        playerRow += 1
    elif playerDir == "left" or playerDir == "a":
        playerCol -= 1
    elif playerDir == "right" or playerDir == "d":
        playerCol += 1
    else:
        print("ERROR that was either not a direction or something else. try again.")
        sleep(1)   