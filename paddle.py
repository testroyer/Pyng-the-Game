import pygame

class Paddle(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.Surface((16 , 112))
        self.image.fill("white")
        self.rect = self.image.get_rect(center = position)
        self.direction = pygame.math.Vector2(0 , 0)
        self.speed = 14
        print(f"pad:{self.rect.y}")

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

    def update(self):
        self.get_input()
        self.rect.y += self.direction.y * self.speed



class FirstPlayer(Paddle):
    def __init__(self):
        super().__init__((64 , 256))

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0


class SecondPlayer(Paddle):
    def __init__(self):
        super().__init__((960 ,256))

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0
