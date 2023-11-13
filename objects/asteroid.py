# objects/asteroid.py
import pygame
import random
from utils.settings import ASTEROID_SPEED, ASTEROID_HEALTH, SCREEN_WIDTH, SCREEN_HEIGHT
from objects.player import Player
from objects.helper_ship import HelperShip
from objects.bullet import Bullet

class Asteroid(pygame.sprite.Sprite):
    ASTEROID_COUNT = 0
    def __init__(self, start_pos):
        super().__init__()
        self.image = pygame.image.load('assets/images/asteroid.png')
        self.rect = self.image.get_rect(center=start_pos)
        self.speed = ASTEROID_SPEED
        self.health = ASTEROID_HEALTH
        self.angle = 0
        self.is_targeted = False
        Asteroid.ASTEROID_COUNT += 1

    def update(self):
        self._move_asteroid()
        self._check_off_screen()

    def _move_asteroid(self):
        # Move the asteroid downwards
        self.rect.y += self.speed

    def _check_off_screen(self):
        # Check if the asteroid has moved off-screen
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()  # Remove the asteroid from all sprite groups

    def destroy(self):
        # Add any additional destruction logic here
        self.is_targeted = False  # Reset the targeted flag
        self.kill() 

    def draw(self, screen):
        # Draw the asteroid on the screen
        screen.blit(self.image, self.rect)

    def take_damage(self, amount, collider):
        # Assuming collider can be a Bullet as well
        if isinstance(collider, (Player, HelperShip, Bullet)):
            self._reduce_health(amount)
            self._check_health_depleted()

    def _reduce_health(self, amount):
        # Reduce the asteroid's health by the damage amount
        self.health -= amount

    def _check_health_depleted(self):
        # Check if the asteroid's health has been depleted
        if self.health <= 0:
            self.kill()  # Remove the asteroid from all sprite groups

    def kill(self):
        super().kill()
        Asteroid.ASTEROID_COUNT -= 1
        if Asteroid.ASTEROID_COUNT < 0:
            Asteroid.ASTEROID_COUNT = 0