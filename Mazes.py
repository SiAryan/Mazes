import pygame
import random

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (241, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (203, 0, 255)
RED = (255, 0, 0)
BLACK = (0,0,0)

screenSize = (1000, 600)
screen = pygame.display.set_mode(screenSize)

bgOrigin = (-460, 0)
FPS = 60

def updateScreen():
    pygame.display.flip()






class Maze(object):
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.x = 20
        self.y = 20
        self.width = 40
        self.grid = []
    def gridGen(self):
        w = self.width
        for i in range(self.y, screenSize[1]-self.width, self.width):
            for j in range(self.x, screenSize[0]-self.width, self.width):
                pygame.draw.line(screen, BLACK, [j, i], [j+w, i])
                pygame.draw.line(screen, BLACK, [j+w, i], [j+w, i+w])
                pygame.draw.line(screen, BLACK, [j+w, i+w], [j, i+w])
                pygame.draw.line(screen, BLACK, [j, i+w], [j, i])

                if [j,i] not in self.grid:
                    self.grid.append([j, i])

    def pushUp(self, x, y):
        pygame.draw.rect(screen, YELLOW, (x + 1, y - self.width + 1, self.width - 1, self.width), 0)

    def pushDown(self, x, y):
        pygame.draw.rect(screen, YELLOW, (x + 1, y + self.width, self.width - 1, self.width), 0)

    def pushRight(self, x, y):
        pygame.draw.rect(screen, YELLOW, (x + self.width, y + 1, self.width, self.width - 1), 0)

    def pushLeft(self, x, y):
        pygame.draw.rect(screen, YELLOW, (x - self.width + 1, y + 1, self.width, self.width - 1), 0)

    def colorCell(self, x, y):
        pygame.draw.rect(screen, YELLOW, (x + 1, y + 1, self.width - 1, self.width - 1))

    def trackCell(self, x, y):
        pygame.draw.rect(screen, GREEN, (x + 1, y + 1, self.width - 1, self.width - 1))


    def buildMaze(self):
        run = True
        algorithm = Algorithms()
        maze.gridGen()
        builtmaze = False
        playmaze = False
        while run:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            if not builtmaze:
                builtmaze = algorithm.rec_Backtracker(20, 20, self.width, self)

            #player.drawPlayer()
            #if builtmaze and not playmaze:


            updateScreen()





class Algorithms(object):
    def __init__(self):
        self.visited = []
        self.stack = []
        self.direction = []

    def rec_Backtracker(self, x, y, w, maze):
        self.stack.append([x, y])
        self.visited.append([x, y])
        maze.colorCell(x, y)
        while len(self.stack) > 0:
            self.direction = []
            x = self.stack[-1][0]
            y = self.stack[-1][1]
            maze.clock.tick(FPS)
            if [x + w, y] not in self.visited and [x + w, y] in maze.grid:
                self.direction.append("right")
            if [x - w, y] not in self.visited and [x - w, y] in maze.grid:
                self.direction.append("left")
            if [x, y + w] not in self.visited and [x, y + w] in maze.grid:
                self.direction.append("down")
            if [x, y - w] not in self.visited and [x, y - w] in maze.grid:
                self.direction.append("up")

            # reached a dead end or end of the grid
            if len(self.direction) > 0:
                direction = random.choice(self.direction)

                if direction == "right":
                    maze.pushRight(x, y)
                    x = x + w
                    self.visited.append([x, y])
                    self.stack.append([x, y])
                    updateScreen()

                elif direction == "left":
                    maze.pushLeft(x, y)
                    x = x - w
                    self.visited.append([x, y])
                    self.stack.append([x, y])
                    updateScreen()

                elif direction == "up":
                    maze.pushUp(x, y)
                    y = y - w
                    self.visited.append([x, y])
                    self.stack.append([x, y])
                    updateScreen()

                elif direction == "down":
                    maze.pushDown(x, y)
                    y = y + w
                    self.visited.append([x, y])
                    self.stack.append([x, y])
                    updateScreen()
            else:
                #maze.trackCell(x, y)
                #pygame.display.flip()
                #time.sleep(0.05)
                #maze.colorCell(x, y)
                #pygame.display.flip()
                self.stack.remove([x, y])
        return True



if __name__ == '__main__':
    maze = Maze()
    maze.buildMaze()

