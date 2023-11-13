import pygame
from utils.settings import PLAYER_SPEED, PLAYER_BULLET_SPEED, PLAYER_HEALTH, PLAYER_SHOOTING_COOLDOWN, SCREEN_WIDTH, SCREEN_HEIGHT
from objects.bullet import Bullet
import time

class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.level = 1 
        self.image = pygame.image.load('assets/images/player_ship.png')
        self.rect = self.image.get_rect(center=self.screen.get_rect().center)
        self.speed = PLAYER_SPEED
        self.bullets = pygame.sprite.Group()
        self.bullet_speed = PLAYER_BULLET_SPEED
        self.shooting_cooldown = PLAYER_SHOOTING_COOLDOWN
        self.last_shot_time = time.time()
        self.score = 0
        self.health = PLAYER_HEALTH
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT
        self.invulnerable = False
        self.invulnerability_duration = 1.0
        self.last_damage_time = None

    def can_take_damage(self):
        if self.invulnerable and time.time() - self.last_damage_time < self.invulnerability_duration:
            return False
        return True

    def take_damage(self, amount):
        if self.can_take_damage():
            self.health -= amount
            self.trigger_invulnerability()
            if self.health <= 0:
                self._die()

    def trigger_invulnerability(self):
        self.invulnerable = True
        self.last_damage_time = time.time()

    def move_left(self):
        self.move(-1, 0)

    def move_right(self):
        self.move(1, 0)

    def move_up(self):
        self.move(0, -1)

    def move_down(self):
        self.move(0, 1)

    def move(self, dx, dy):
        self.rect.move_ip(dx * self.speed, dy * self.speed)
        self._enforce_screen_boundaries()

    def update(self):
        self._enforce_screen_boundaries()
        self.bullets.update()
        if self.invulnerable and time.time() - self.last_damage_time > self.invulnerability_duration:
            self.invulnerable = False

        # Automatic shooting logic
        current_time = time.time()
        if current_time - self.last_shot_time >= self.shooting_cooldown:
            self.shoot()

    def shoot(self):
        bullet = Bullet(self.screen, self.rect.centerx, self.rect.top, self.bullet_speed)
        self.bullets.add(bullet)
        self.last_shot_time = time.time()

    def draw(self, screen):
        self.screen.blit(self.image, self.rect)
        for bullet in self.bullets:
            bullet.draw(screen)

    def _enforce_screen_boundaries(self):
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
        elif self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > self.screen_height:
            self.rect.bottom = self.screen_height

    def _die(self):
        self.kill()
