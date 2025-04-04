from circleshape import *
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOT_SPEED
from shot import *
import pygame

class Player(CircleShape):    
    def __init__(self,x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0

        # in the player class:
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        
        return [a, b, c]

    def draw(self,display):
        return pygame.draw.polygon(surface= display, color = "white", points = self.triangle(), width = 2)

    def rotate(self, dt):
        self.rotation = self.rotation + (PLAYER_TURN_SPEED*dt)
    
    def update(self, dt):
           keys = pygame.key.get_pressed()
           if keys[pygame.K_a]:
               self.rotate(-dt)
           if keys[pygame.K_d]:
               self.rotate(dt)
           if keys[pygame.K_w]:
               self.move(dt)
           if keys[pygame.K_s]:
               self.move(-dt)
           if keys[pygame.K_SPACE]:
               self.shoot(dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, dt):
        if self.shot_timer <= 0:
            self.shot_timer = 0.4
            a_shot = Shot(self.position[0],self.position[1], SHOT_RADIUS)
            a_shot.velocity = pygame.Vector2(0,1) * PLAYER_SHOT_SPEED
            a_shot.velocity = a_shot.velocity.rotate(self.rotation)

        self.shot_timer -= dt

