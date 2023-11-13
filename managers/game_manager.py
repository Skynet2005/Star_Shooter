# managers/game_manager.py
import pygame
import random
from objects.player import Player
from objects.asteroid import Asteroid
from objects.health_pack import HealthPack
from objects.helper_item import HelperItem
from objects.helper_ship import HelperShip
from utils.settings import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_FREQUENCY, HEALTH_PACK_CHANCE, HELPER_ITEM_CHANCE, MAX_ASTEROIDS

class GameManager:
    def __init__(self, screen, font, sound_manager):
        self.screen = screen
        self.font = font
        self.sound_manager = sound_manager
        self.sound_manager.load_explosion_sound('assets/sounds/collide.wav')
        self.player = Player(screen)
        self.asteroids = pygame.sprite.Group()
        self.health_packs = pygame.sprite.Group()
        self.helper_items = pygame.sprite.Group()
        self.helper_ships = pygame.sprite.Group()
        self.player.update()
        self.handle_collisions()
        pygame.time.set_timer(pygame.USEREVENT + 1, ASTEROID_FREQUENCY)

    def run(self, events):
        # Check events for spawning asteroids
        for event in events:
            if event.type == pygame.USEREVENT + 1:
                self.spawn_asteroid()
                self.spawn_health_pack()
                self.spawn_helper_item()

        # Update the player, asteroids, health packs, and helper items
        self.player.update()
        self.asteroids.update() 
        self.health_packs.update()  
        self.helper_items.update()

        # Update helper ships
        if len(self.asteroids) > 0:
            for helper_ship in self.helper_ships:
                helper_ship.update(self.asteroids)
        # Pass the asteroid group if there are asteroids, otherwise don't pass it
        else:
            for helper_ship in self.helper_ships:
                helper_ship.update()

        # Handle any collisions that have occurred
        self.handle_collisions()


    def spawn_asteroid(self):
        if Asteroid.ASTEROID_COUNT < MAX_ASTEROIDS:
            x_pos = random.randrange(0, SCREEN_WIDTH)
            y_pos = 0  
            asteroid = Asteroid((x_pos, y_pos))
            self.asteroids.add(asteroid)

    def spawn_health_pack(self):
        if random.random() < HEALTH_PACK_CHANCE:
            x_pos = random.randrange(0, SCREEN_WIDTH)
            y_pos = random.randrange(0, SCREEN_HEIGHT)
            health_pack = HealthPack(self.screen, (x_pos, y_pos))
            self.health_packs.add(health_pack)

    def spawn_helper_item(self):
        if random.random() < HELPER_ITEM_CHANCE:
            x_pos = random.randrange(0, SCREEN_WIDTH)
            y_pos = random.randrange(0, SCREEN_HEIGHT)
            helper_item = HelperItem(self.screen, (x_pos, y_pos))
            self.helper_items.add(helper_item)

    def handle_collisions(self):
        # Handle bullet-asteroid collisions
        for bullet in self.player.bullets:
            hit_asteroids = pygame.sprite.spritecollide(bullet, self.asteroids, False)
            for asteroid in hit_asteroids:
                bullet.kill()
                asteroid.take_damage(1, bullet)
                if not asteroid.alive():
                    self.sound_manager.play_explosion_sound('assets/sounds/collide.wav')
                    self.player.score += 10

        # Handle player-asteroid collisions
        asteroids_collided = pygame.sprite.spritecollide(self.player, self.asteroids, False)
        if asteroids_collided:
            asteroid = asteroids_collided[0]
            asteroid.take_damage(1, self.player) 
            if self.player.can_take_damage():
                self.player.take_damage(1)
                self.player.trigger_invulnerability()

        # Handle player-health pack collisions
        health_packs_collided = pygame.sprite.spritecollide(self.player, self.health_packs, True)
        for health_pack in health_packs_collided:
            self.player.health += health_pack.get_amount()
            health_pack.kill()

        # Handle player-helper item collisions
        helper_items_collided = pygame.sprite.spritecollide(self.player, self.helper_items, True)
        for helper_item in helper_items_collided:
            # The collide method of HelperItem has been updated to accept the GameManager instance
            helper_item.collide(self.player, self)  # Pass the GameManager instance to the collide method

        # Check if the player is no longer alive
        if not self.player.alive():
            self.end_game()

    def get_closest_asteroid(self, position):
        # Find the closest asteroid to the given position
        closest_asteroid = None
        min_distance = float('inf')
        for asteroid in self.asteroids:
            distance = (position[0] - asteroid.rect.centerx) ** 2 + (position[1] - asteroid.rect.centery) ** 2
            if distance < min_distance:
                min_distance = distance
                closest_asteroid = asteroid
        return closest_asteroid

    def draw(self, screen):
        self.player.draw(screen)  
        self.player.bullets.draw(screen)
        self.asteroids.draw(screen) 
        self.health_packs.draw(screen)
        self.helper_items.draw(screen)  
        self.helper_ships.draw(screen)

    def end_game(self):
        pass
