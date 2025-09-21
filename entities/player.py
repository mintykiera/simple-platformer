import pygame
from config import *

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.vel_x = 0
        self.vel_y = 0
        self.on_ground = False
        self.jump_cooldown = 0
        self.alive = True
        self.jumps_remaining = 2
        self.in_game_session = False
        self.touched_ground_after_jump = False
        self.scored_platforms = set()

    def update(self, platforms):
        self.vel_y += GRAVITY
        if self.vel_y > MAX_FALL_SPEED:
            self.vel_y = MAX_FALL_SPEED
        
        keys = pygame.key.get_pressed()
        self.vel_x = 0
        if keys[pygame.K_a]:
            self.vel_x = -PLAYER_SPEED
        if keys[pygame.K_d]:
            self.vel_x = PLAYER_SPEED
        
        new_platforms_scored = 0

        self.rect.x += self.vel_x

        self.rect.y += self.vel_y
        
        self.on_ground = False
        if self.in_game_session:
            for platform in platforms:
                if self.rect.colliderect(platform.rect) and self.vel_y > 0:
                    if abs(self.rect.bottom - platform.rect.top) < self.vel_y + 1:
                        self.rect.bottom = platform.rect.top
                        self.vel_y = 0
                        self.on_ground = True
                        self.jumps_remaining = 2

                        if platform.rect.y >= 500:
                            self.touched_ground_after_jump = True
                        
                        if platform.id not in self.scored_platforms:
                            self.scored_platforms.add(platform.id)
                            new_platforms_scored += 1

            if self.touched_ground_after_jump and self.on_ground and self.rect.y >= 500:
                self.alive = False

        else:
            if self.rect.bottom >= 560:
                self.rect.bottom = 560
                self.on_ground = True
                self.jumps_remaining = 2

        if self.jump_cooldown > 0:
            self.jump_cooldown -= 1

        if self.rect.y > 1000:
            self.alive = False
            
        return new_platforms_scored

    def jump(self):
        if self.jumps_remaining > 0 and self.jump_cooldown == 0:
            self.vel_y = JUMP_STRENGTH
            self.jumps_remaining -= 1
            self.jump_cooldown = 5
            self.touched_ground_after_jump = False

    def start_game_session(self):
        self.in_game_session = True
        self.scored_platforms.clear()
    def get_color(self):
        if self.touched_ground_after_jump and self.rect.y > 500:
            return RED
        elif self.jumps_remaining == 2:
            return PLAYER_COLOR
        elif self.jumps_remaining == 1:
            return (0, 150, 255)
        else:
            return (100, 100, 255)