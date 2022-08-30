import pygame
from level import Level

pygame.init()

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 512
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH ,SCREEN_HEIGHT))
pygame.display.set_caption("Pyng")
pygame.display.set_icon(pygame.image.load("./resources/Sports-Ping-Pong-icon.png"))


level = Level(screen)

running = True
while running:
    screen.fill("black")
    pygame.draw.rect(screen, "white" ,pygame.Rect(511 ,0 ,8 ,512))
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False
        if events.type == pygame.KEYDOWN:
            pass
            if events.key == pygame.K_ESCAPE:
                level.pause()
            elif events.key == pygame.K_h:
                print("toggled")
                level.toggle_hitboxes()

    level.run()

    pygame.display.update()
    clock.tick(60)