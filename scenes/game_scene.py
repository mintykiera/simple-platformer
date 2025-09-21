import pygame
from config import *
from entities.player import Player
from managers.platform_manager import PlatformManager

class GameScene:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.Font(None, 36)

        self.player = Player(400, 300)
        self.platform_manager = PlatformManager()
        self.platforms = 0
        self.camera_x = 0
        self.game_started = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not self.game_started and self.player.on_ground:
                        self.player.start_game_session()
                        self.game_started = True
                    self.player.jump()

    def update(self):
        newly_scored_platforms = self.player.update(self.platform_manager.get_platforms())
        self.platforms += newly_scored_platforms

        self.platform_manager.update(self.player.rect.x)
        self.camera_x = self.player.rect.x - SCREEN_WIDTH // 2
        
        if self.game_started and not self.player.alive:
            self.running = False

    def render(self):
        self.screen.fill(SKY_BLUE)
        
        for platform in self.platform_manager.get_platforms():
            draw_rect = pygame.Rect(
                platform.rect.x - self.camera_x,
                platform.rect.y,
                platform.rect.width,
                platform.rect.height
            )
            if hasattr(platform, 'direction'):
                pygame.draw.rect(self.screen, MOVING_PLATFORM_COLOR, draw_rect)
            else:
                pygame.draw.rect(self.screen, PLATFORM_COLOR, draw_rect)
        
        player_draw_rect = pygame.Rect(
            self.player.rect.x - self.camera_x,
            self.player.rect.y,
            self.player.rect.width,
            self.player.rect.height
        )
        pygame.draw.rect(self.screen, self.player.get_color(), player_draw_rect)
        
        pygame.draw.circle(self.screen, WHITE, (player_draw_rect.x + 8, player_draw_rect.y + 15), 4)
        pygame.draw.circle(self.screen, WHITE, (player_draw_rect.x + 22, player_draw_rect.y + 15), 4)
        pygame.draw.line(self.screen, WHITE, (player_draw_rect.x + 10, player_draw_rect.y + 30), 
                        (player_draw_rect.x + 20, player_draw_rect.y + 30), 2)
        
        platforms_text = self.font.render(f"Platforms: {self.platforms}", True, WHITE)
        self.screen.blit(platforms_text, (10, 10))
        
        if not self.game_started:
            start_text = self.font.render("Press SPACE to start jumping!", True, WHITE)
            start_rect = start_text.get_rect(center=(SCREEN_WIDTH//2, 100))
            self.screen.blit(start_text, start_rect)
        
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(FPS)
        
        return self.platforms