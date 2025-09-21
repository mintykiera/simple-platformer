import pygame
from config import *

class StartScene:
    def __init__(self, screen):
        self.screen = screen
        self.font_large = pygame.font.Font(None, 74)
        self.font_small = pygame.font.Font(None, 36)
        self.running = True
        self.start_game = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.start_game = True

    def update(self):
        pass

    def render(self):
        self.screen.fill(SKY_BLUE)
        
        title_text = self.font_large.render("INFINITE JUMPER", True, WHITE)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH//2, 200))
        self.screen.blit(title_text, title_rect)
        
        instruction_text = self.font_small.render("Press SPACE to Start", True, WHITE)
        instruction_rect = instruction_text.get_rect(center=(SCREEN_WIDTH//2, 300))
        self.screen.blit(instruction_text, instruction_rect)
        
        controls_text = self.font_small.render("A/D to move, W to jump", True, WHITE)
        controls_rect = controls_text.get_rect(center=(SCREEN_WIDTH//2, 350))
        self.screen.blit(controls_text, controls_rect)
        
        pygame.display.flip()

    def run(self):
        while self.running and not self.start_game:
            self.handle_events()
            self.update()
            self.render()
            pygame.time.Clock().tick(FPS)
        
        return self.start_game