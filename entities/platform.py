import pygame
from config import *

class Platform:
    _id_counter = 0
    
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.id = Platform._id_counter
        Platform._id_counter += 1

    def update(self):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, PLATFORM_COLOR, self.rect)