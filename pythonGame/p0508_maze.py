import random

class world :
    def __init__(self, gridSize, treasureCount, trapCount):
        self.grid = [['.' for _ in range(0, gridSize, 1)] for _ in range(0, gridSize, 1)]
        self.playerPos = (0, 0)
        
        for _ in range(0, trapCount, 1) :
            self.setObj('trap')
            
        for _ in range(0, treasureCount, 1) :
            self.setObj('treasure')
        
        self.setObj('player')
        
    def setObj(self, type) :
        pick = random.randint(0, len(self.grid)**2 - 1)
        if (self.grid[pick//5][pick%5] == '.') :
            if (type == 'trap') :
                self.grid[pick//5][pick%5] = 'X'
            elif (type == 'treasure') :
                self.grid[pick//5][pick%5] = 'T'
            elif (type == 'player') :
                self.grid[pick//5][pick%5] = 'P'
                self.playerPos = (pick//5, pick%5)
        else :
            self.setObj(type)
    
    def printGrid(self) :
        for i in range(0, len(self.grid), 1) :
            for j in range(0, len(self.grid[i]), 1) :
                print(f"{self.grid[i][j]} ", end='')
            print('')
            
    def movePlayer(self, way) :
        tmp = self.playerPos
        if (way == "동") :
            self.playerPos = (self.playerPos[0], self.playerPos[1] + 1)
        elif (way == "서") :
            self.playerPos = (self.playerPos[0], self.playerPos[1] - 1)
        elif (way == "남") :
            self.playerPos = (self.playerPos[0] + 1, self.playerPos[1])
        elif (way == "북") :
            self.playerPos = (self.playerPos[0] - 1, self.playerPos[1])
            
        if (self.playerPos[0] not in range(0, len(self.grid), 1) or self.playerPos[1] not in range(0, len(self.grid), 1)) :
            print("경로를 이탈하였습니다! 사망하였습니다!")
            return 2
        
        if (self.grid[self.playerPos[0]][self.playerPos[1]] == 'T') :
            print("보물을 찾았습니다! 축하합니다!")
            return 1
        elif (self.grid[self.playerPos[0]][self.playerPos[1]] == 'X') :
            print("사망하였습니다!")
            return 2
        
        #print(tmp, self.playerPos)
        self.grid[tmp[0]][tmp[1]] = '.'
        self.grid[self.playerPos[0]][self.playerPos[1]] = 'P'
        return 0
            
w = world(5, 2, 3)

while True :
    w.printGrid()
    mvmt = input("이동(동/서/남/북) : ")
    reward = w.movePlayer(mvmt)
    
    if (reward == 0) :
        continue
    if (reward == 1) :
        break
    if (reward == 2) :
        w = world(5, 2, 3)
        continue