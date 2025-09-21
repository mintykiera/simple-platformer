import pygame
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from scenes.start_scene import StartScene
from scenes.game_scene import GameScene
from scenes.game_over_scene import GameOverScene
from config import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Platformer (template?)")

    running = True
    while running:
        start_scene = StartScene(screen)
        if not start_scene.run():
            break
        
        game_scene = GameScene(screen)
        final_score = game_scene.run()
        
        game_over_scene = GameOverScene(screen, final_score)
        if not game_over_scene.run():
            break

    pygame.quit()

if __name__ == "__main__":
    main()