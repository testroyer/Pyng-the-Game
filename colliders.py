import pygame

class ScoreCollider(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((2, 512), pygame.SRCALPHA)
        self.image.fill("black")
        self.image.set_colorkey("black")
        self.rect = self.image.get_rect(topleft = pos)


class EdgeCollider(pygame.sprite.Sprite):
    def __init__(self , pos):
        super().__init__()
        self.image = pygame.Surface((1024 , 2))
        self.image.fill("black")
        self.rect = self.image.get_rect(topleft = pos)
