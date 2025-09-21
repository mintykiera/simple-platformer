import pygame
from config import *

class MovingPlatform:
    _id_counter = 0
    
    def __init__(self, x, y, width, height, move_range=100, speed=2):
        self.rect = pygame.Rect(x, y, width, height)
        self.start_x = x
        self.move_range = move_range
        self.speed = speed
        self.direction = 1
        self.id = MovingPlatform._id_counter
        MovingPlatform._id_counter += 1

    def update(self):
        self.rect.x += self.speed * self.direction
        
        if self.rect.x > self.start_x + self.move_range:
            self.direction = -1
        elif self.rect.x < self.start_x:
            self.direction = 1

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 165, 0), self.rect)