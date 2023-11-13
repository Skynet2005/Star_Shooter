# managers/screen_manager.py
import pygame
from utils.settings import BACKGROUND_IMAGE_PATH

class ScreenManager:
    def __init__(self, screen, font, background_color=(0, 0, 0)): 
        self.screen = screen
        self.font = font 
        self.background_color = background_color
        self.background_image = pygame.image.load(BACKGROUND_IMAGE_PATH).convert()

    def draw_background(self):
        # Draw the game background
        self.screen.blit(self.background_image, (0, 0))

    def draw(self, game_manager):
        self.draw_background()
        self.draw_score(game_manager.player.score)
        self.draw_lives(game_manager.player.health)
        self.draw_level(game_manager.player.level)

    def draw_score(self, score):
        score_text = self.font.render(f"Current Score: {score} points", True, (255, 255, 0))
        self.screen.blit(score_text, (10, 10))

    def draw_lives(self, lives):
        lives_text = self.font.render(f"Remaining Lives: {lives} health", True, (255, 0, 0))
        self.screen.blit(lives_text, (10, 30))

    def draw_level(self, level):
        level_text = self.font.render(f"Current Level: {level} stage", True, (0, 255, 255))
        self.screen.blit(level_text, (10, 50))