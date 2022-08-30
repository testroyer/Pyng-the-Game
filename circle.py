import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, pos, radius):
        super().__init__()
        self.image = pygame.Surface(((radius*2) , (radius*2)))
        self.image.fill("green")
        self.image.set_colorkey("green")
        pygame.draw.circle(self.image ,"white" ,(radius , radius)  , radius)
        self.rect = self.image.get_rect(center = pos)
        self.direction = pygame.math.Vector2(-1,0)
        self.speed = 14
        self.radius = radius
        print(self.rect.y)

    def redraw(self):
        pygame.draw.circle(self.image ,"white" ,(self.radius , self.radius)  , self.radius)



