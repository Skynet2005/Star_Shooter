# objects/bullet.py
import pygame
from utils.settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, speed):
        super().__init__()
        self.screen = screen
        self.level = 1
        self.image = pygame.image.load('assets/images/bullet.png')
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT

    def update(self):
        self._move_bullet()
        self._check_off_screen()

    def _move_bullet(self):
        # Move the bullet
        self.rect.y -= self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def _check_off_screen(self):
        # Remove the bullet if it's off-screen
        if self.rect.bottom < 0 or self.rect.top > self.screen_height or self.rect.left < 0 or self.rect.right > self.screen_width:
            self.kill()  

    def collide_with(self, sprite_group):
        # Check if bullet collides with any sprite in the group
        return pygame.sprite.spritecollide(self, sprite_group, False)