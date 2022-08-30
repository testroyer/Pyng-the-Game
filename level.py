import pygame
from paddle import FirstPlayer ,SecondPlayer
from colliders import EdgeCollider, ScoreCollider
from circle import Ball
from scoreLabel import ScoreLabel

class Level:
    def __init__(self, screen):
        self.display = screen
        self.frameCount = 0
        self.ballStoppedFrame = 0
        self.ballStopped = True
        self.paused = False
        self.hitboxesShown = False
        self.setup()

    def setup(self):

        self.font = pygame.font.Font("./resources/bit5x3.ttf" , 64)
        self.label1 = ScoreLabel(self.font , 256 , 128 , self.display)
        self.label2 = ScoreLabel(self.font , 768 , 128 , self.display)
        self.pausedLabel = ScoreLabel(self.font , 0 , 0 , self.display)
        self.pausedLabel.value = "Paused"

        self.paddle_group = pygame.sprite.Group()
        self.score_group = pygame.sprite.Group()
        self.ball_group = pygame.sprite.GroupSingle()
        self.edge_group = pygame.sprite.Group()

        self.paddle1 = FirstPlayer()
        self.paddle2 = SecondPlayer()
        self.paddle_group.add(self.paddle1)
        self.paddle_group.add(self.paddle2)

        self.score1 = ScoreCollider((0,0))
        self.score2 = ScoreCollider((1022,0))
        self.score_group.add(self.score1)
        self.score_group.add(self.score2)

        self.edge1 = EdgeCollider((0 ,1))
        self.edge2 = EdgeCollider((0 , 510))
        self.edge_group.add(self.edge1)
        self.edge_group.add(self.edge2)

        self.ball = Ball((256 ,256) ,10)
        self.ball_group.add(self.ball)

    def toggle_hitboxes(self):
        if self.hitboxesShown == False:
            self.score1.image.fill("green")
            self.score2.image.fill("green")
            self.edge1.image.fill("red")
            self.edge2.image.fill("red")
            self.ball.image.fill("blue")
            self.paddle1.image.fill("yellow")
            self.paddle2.image.fill("yellow")
            self.hitboxesShown = True

        elif self.hitboxesShown == True:
            self.score1.image.fill("black")
            self.score2.image.fill("black")
            self.edge1.image.fill("black")
            self.edge2.image.fill("black")
            self.ball.image.fill("green")
            self.paddle1.image.fill("white")
            self.paddle2.image.fill("white")
            self.ball.redraw()
            self.hitboxesShown = False


    def ballMove(self):
        self.ballStopped = False
        self.frameCount = 0
        self.ballStoppedFrame = 0

    def ballStop(self):
        self.ballStopped = True
        self.frameCount = 0
        self.ballStoppedFrame = 0
    
    def reset(self):
        self.label1.value = 0
        self.label2.value = 0
        self.paddle1.rect.y = 200
        self.paddle2.rect.y = 200
        self.ball.rect.centery = 256 
        self.ball.rect.centerx = 256
        self.ball.direction.y = 0
        self.ball.direction.x = -1
        self.ballStop()

    def pause(self):
        if self.paused == False:
            self.paused = True
        elif self.paused == True:
            self.paused = False

    def ball_collide(self):
        ball = self.ball
        if not self.ballStopped:
            ball.rect.x += ball.direction.x * ball.speed
            ball.rect.y += ball.direction.y * ball.speed
        elif self.ballStopped:
            self.frameCount += 1
            if self.frameCount >= self.ballStoppedFrame + 60:
                self.ballMove()

        if ball.rect.y < -20 or ball.rect.y > 532:
            ball.rect.y = 256
            ball.rect.x = 256
            self.ballStop()

        for paddles in self.paddle_group.sprites():
            if paddles.rect.colliderect(ball):
                if paddles == self.paddle1:
                    ball.direction.x = 1
                    ball.direction.y = ((((paddles.rect.centery) - (ball.rect.centery)) / (paddles.rect.x - 64)) / 8.125) 
                elif paddles == self.paddle2:
                    ball.direction.x = -1
                    ball.direction.y = ((((paddles.rect.centery) - (ball.rect.centery)) /  (paddles.rect.x - 960)) / 8.125) 
                print(f"{ball.direction.x} , {ball.direction.y}")

            """
            ((((191) - (256)) / - (56 - 60)) / 10)
            2.0
            """

        for colliders in self.score_group.sprites():
            if colliders.rect.colliderect(ball):
                ball.rect.centery = 256
                if colliders == self.score1:
                    self.label2.value += 1
                    ball.rect.centerx = 256
                    ball.direction.y = 0
                    ball.direction.x = -1
                    self.ballStop()
                elif colliders == self.score2:
                    self.label1.value += 1
                    ball.rect.centerx = 756
                    ball.direction.y = 0
                    ball.direction.x = 1
                    self.ballStop()
                    

        for edges in self.edge_group.sprites():
            if edges.rect.colliderect(ball):
                   ball.direction.y = -ball.direction.y 

    def run(self):

        #Reset
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            self.reset()

        #Updates
        if self.paused == False:
            self.ball_collide()
            self.ball_group.update()
            self.paddle_group.update()
        else:
            self.pausedLabel.render()



        #Label renders
        self.label1.render()
        self.label2.render()

        #Ball
        self.ball_group.draw(self.display)

        #Score 
        self.score_group.draw(self.display)

        #Edge
        self.edge_group.draw(self.display)

        #Paddle
        self.paddle_group.draw(self.display)


