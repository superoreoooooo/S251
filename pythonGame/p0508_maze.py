import random

class mazeWorld :
    def __init__(self, gridSize, treasureCount, trapCount):
        self.grid = [['.' for _ in range(0, gridSize, 1)] for _ in range(0, gridSize, 1)]
        self.playerPos = (0, 0)
        
        self.setObj('X', trapCount)
        self.setObj('T', treasureCount)
        self.setObj('P', 1)
        
    def setObj(self, type, count) :
        genCnt = 0
        for _ in range(0, count, 1) :
            pick = random.randint(0, len(self.grid)**2 - 1)
            if (self.grid[pick//5][pick%5] == '.') :
                self.grid[pick//5][pick%5] = type
                if (type == 'P') :
                    self.playerPos = (pick//5, pick%5)
                genCnt += 1
            else :
                self.setObj(type, count - genCnt)
    
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
            print("미로를 이탈하였습니다! 사망하였습니다!")
            return 2
        
        if (self.grid[self.playerPos[0]][self.playerPos[1]] == 'T') :
            print("보물을 찾았습니다! 축하합니다!")
            return 1
        elif (self.grid[self.playerPos[0]][self.playerPos[1]] == 'X') :
            print("사망하였습니다!")
            return 2
        
        self.grid[tmp[0]][tmp[1]] = '.'
        self.grid[self.playerPos[0]][self.playerPos[1]] = 'P'
        return 0

if (__name__ == "__main__") :
    w = mazeWorld(5, 2, 3)

    while True :
        w.printGrid()
        mvmt = input("이동(동/서/남/북) : ")
        status = w.movePlayer(mvmt)
        
        if (status == 0) :
            continue
        if (status == 1) :
            break
        if (status == 2) :
            w = mazeWorld(5, 2, 3)
            continue