# objects/helper_item.py
import pygame
from objects.helper_ship import HelperShip
from utils.settings import HELPER_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT, HELPER_ITEM_AMOUNT

class HelperItem(pygame.sprite.Sprite):
    def __init__(self, screen, start_pos):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('assets/images/helper_item.png')
        self.rect = self.image.get_rect(center=start_pos)
        self.speed = HELPER_SPEED
        self.amount = HELPER_ITEM_AMOUNT
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT

    def update(self):
        self._move_helper_item()
        self._check_off_screen()

    def _move_helper_item(self):
        self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def collide(self, player, game_manager):
        # If the HelperItem is collected, spawn a HelperShip
        if pygame.sprite.collide_rect(self, player):
            # Find a target asteroid for the helper ship
            target_asteroid = game_manager.get_closest_asteroid(self.rect.center)
            # Create a helper ship at the current position of the helper item
            helper_ship = HelperShip(self.screen, self.rect.center, target_asteroid)
            # Add the helper ship to the game manager's helper ships group
            game_manager.helper_ships.add(helper_ship)
            # Kill the helper item
            self.kill()
            
    def get_amount(self):
        return self.amount

    def _check_off_screen(self):
        if self.rect.y > self.screen_height + 20:
            self.kill()