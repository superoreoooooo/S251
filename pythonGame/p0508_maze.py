import random

class world :
    def __init__(self, gridSize, treasureCount, trapCount):
        self.grid = {{_ for x in range(0, gridSize, 1)} for _ in range(0, gridSize, 1)}
        
        print(self.grid)
        


w = world(5, 2, 3)
