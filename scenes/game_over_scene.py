import pygame
from config import *

class GameOverScene:
    def __init__(self, screen, score):
        self.screen = screen
        self.score = score
        self.font_large = pygame.font.Font(None, 74)
        self.font_small = pygame.font.Font(None, 36)
        self.running = True
        self.restart = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.restart = True
                elif event.key == pygame.K_ESCAPE:
                    self.running = False

    def update(self):
        pass

    def render(self):
        self.screen.fill((0, 0, 50))

        game_over_text = self.font_large.render("GAME OVER", True, RED)
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH//2, 200))
        self.screen.blit(game_over_text, game_over_rect)
        
        score_text = self.font_small.render(f"Score: {self.score}", True, WHITE)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH//2, 280))
        self.screen.blit(score_text, score_rect)
        
        restart_text = self.font_small.render("Press SPACE to Restart", True, WHITE)
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH//2, 350))
        self.screen.blit(restart_text, restart_rect)
        
        quit_text = self.font_small.render("Press ESC to Quit", True, WHITE)
        quit_rect = quit_text.get_rect(center=(SCREEN_WIDTH//2, 390))
        self.screen.blit(quit_text, quit_rect)
        
        pygame.display.flip()

    def run(self):
        while self.running and not self.restart:
            self.handle_events()
            self.update()
            self.render()
            pygame.time.Clock().tick(FPS)
        
        return self.restart