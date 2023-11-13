# objects/health_pack.py
import pygame
from utils.settings import HEALTH_PACK_CHANCE, HEALTH_PACK_AMOUNT, SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_SPEED

class HealthPack(pygame.sprite.Sprite):
    def __init__(self, screen, start_pos):
        super().__init__()
        self.screen = screen
        self.level = 1
        self.image = pygame.image.load('assets/images/health_pack.png')
        self._initialize_health_pack(start_pos)
        self.rect = self.image.get_rect(center=start_pos)
        self.speed = ASTEROID_SPEED
        self.amount = HEALTH_PACK_AMOUNT
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT

    def _initialize_health_pack(self, start_pos):
        self.rect = self.image.get_rect(center=start_pos)

    def update(self):
        self._move_health_pack()
        self._check_off_screen()

    def _move_health_pack(self):
        # Move the health pack downwards
        self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def collide(self, player):
        if pygame.sprite.collide_rect(self, player):
            player.health += self.get_amount()
            self.kill()

    def get_amount(self):
        return self.amount

    def _check_off_screen(self):
        if self.rect.y > self.screen_height + 20:
            self.kill()


