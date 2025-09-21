import random
from entities.platform import Platform
from entities.moving_platform import MovingPlatform
from config import PLATFORM_WIDTH_MIN, PLATFORM_WIDTH_MAX, PLATFORM_HEIGHT

class PlatformManager:
    def __init__(self):
        self.platforms = []
        self.player_x_offset = 0
        self.last_platform_x = 0
        self.platforms_jumped = 0
        self.jumped_platform_ids = set()
        self.initialize_platforms()

    def initialize_platforms(self):
        for i in range(-10, 20):
            x = i * 800
            self.platforms.append(Platform(x, 560, 800, 40))
        
        for i in range(20):
            self.generate_platform_at_edge()

    def generate_platform_at_edge(self):
        next_x = self.last_platform_x + random.randint(150, 350)
        y = random.randint(350, 540)
        width = random.randint(PLATFORM_WIDTH_MIN, PLATFORM_WIDTH_MAX)
        
        if abs(next_x - 400) < 300 and abs(y - 300) < 200:
            next_x += 600
        
        if random.random() < 0.2:
            platform = MovingPlatform(next_x, y, width, PLATFORM_HEIGHT, move_range=100, speed=1)
        else:
            platform = Platform(next_x, y, width, PLATFORM_HEIGHT)
            
        self.platforms.append(platform)
        self.last_platform_x = next_x

    def update(self, player_x):
        self.player_x_offset = player_x
        
        for platform in self.platforms:
            if hasattr(platform, 'update'):
                platform.update()
        
        self.platforms = [p for p in self.platforms if p.rect.x > player_x - 2000 or p.rect.y == 560]
        
        while self.last_platform_x < player_x + 3000:
            self.generate_platform_at_edge()

    def get_platforms(self):
        return self.platforms

    def platform_jumped(self):
        self.platforms_jumped += 1

    def get_score(self):
        return self.platforms_jumped