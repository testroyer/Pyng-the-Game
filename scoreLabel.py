import pygame

class ScoreLabel():
    def __init__(self, font ,x,y,screen) -> None:
        self.value = 0
        self.display = screen
        self.font = font
        self.x = x
        self.y = y 

    def render(self):
        score = self.font.render(str(self.value) , True ,"white")
        self.display.blit(score , (self.x , self.y))

