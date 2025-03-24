import pygame
import numpy as np

#mt관련 -> 출석일 + 참가 확인서??


##### TODO WRITE PHYSICS
class Vector2 :
    def __init__(self, x=0, y=0):
        self = (x, y)
        self.x = x
        self.y = y
        self.magnitude = np.sqrt(x**2 + y**2)
        self.normalized = (x, y) / self.magnitude

class Quaternion :
    pass

class GameObject :
    pass

def run() :
    pygame.init()
    mario = pygame.image.load("pythonGame/mario.webp")
    mario = pygame.transform.scale(mario, (40, 40))
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    gravity = -9.8
    yVel = 0
    dt = 0 #delta time

    player_pos = pygame.Vector2(screen.get_width() / 2, 0 )#screen.get_height() / 2)

    def Jump(velocity) :
        velocity += 100 * dt
        player_pos.y += velocity * dt

    def runPhysics(velocity) :
        velocity += gravity * dt
        player_pos.y += velocity * dt

    def onInput() :
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            #player_pos.y -= 300 * dt

            Jump(yVel)

            """
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
            """
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("white")

        runPhysics(yVel)
        if (player_pos.y < screen.get_height()) :
            player_pos.y = screen.get_height() - 100
            yVel = 0
        onInput()

        #pygame.draw.circle(screen, "blue", player_pos, 40)

        screen.blit(mario, player_pos)

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 120
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(120) / 1000

    pygame.quit()

if __name__ == "__main__" :
    run()