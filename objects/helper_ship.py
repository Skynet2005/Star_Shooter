# objects/helper_ship.py
import pygame
import time
from objects.bullet import Bullet
from objects.particle_effect import ParticleEffect
from utils.settings import HELPER_SHIP_SPACING, HELPER_SPEED, HELPER_SHOOTING_COOLDOWN, SCREEN_WIDTH, SCREEN_HEIGHT, HELPER_BULLET_SPEED, HELPER_SHOOTING_RANGE

# The HelperShip class represents the helper ships in the game.
class HelperShip(pygame.sprite.Sprite):
    # Initialize the helper ship with its screen, starting position, and target asteroid.
    def __init__(self, screen, start_pos, target_asteroid):
        super().__init__()
        self.screen = screen
        self.level = 1
        self.initial_health = 1
        self.spacing = HELPER_SHIP_SPACING
        self.image = pygame.image.load('assets/images/helper_ship.png')
        self.rect = self.image.get_rect(center=start_pos)
        self.target_asteroid = target_asteroid
        self.speed = HELPER_SPEED
        self.bullet_speed = HELPER_BULLET_SPEED
        self.shooting_cooldown = HELPER_SHOOTING_COOLDOWN
        self.last_shot_time = time.time()
        self.score = 0
        self.bullets = pygame.sprite.Group()
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT
        self._initialize_helper_ship(start_pos)

    # Initialize the helper ship with its starting position.
    def _initialize_helper_ship(self, start_pos):
        # Setup the initial state of the helper ship
        self.rect = self.image.get_rect(center=start_pos)
        self.speed = HELPER_SPEED
        self.bullet_speed = HELPER_BULLET_SPEED
        self.shooting_cooldown = HELPER_SHOOTING_COOLDOWN
        self.last_shot_time = time.time()
        self.score = 0
        self.bullets = pygame.sprite.Group()
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT
        
    # Update the state of the helper ship.
    def update(self, asteroids):
        # If there is no target asteroid or it is no longer alive, find a new target
        if self.target_asteroid is None or not self.target_asteroid.alive():
            self.target_asteroid = self._get_new_target(asteroids)
            if self.target_asteroid is None:
                return  
        # Move towards the target asteroid
        self._chase_target()
        # Check if we're close enough to shoot
        if self._is_in_shooting_range(self.target_asteroid):
            self._shoot()
        self.bullets.update()
        self._check_collision(asteroids)
        self._enforce_screen_boundaries()
        self._check_off_screen()

    # Get a new target asteroid.
    def _get_new_target(self, asteroids):
        # Find the closest asteroid that is not already targeted by another helper ship
        closest_asteroid = None
        min_distance = float('inf')
        for asteroid in asteroids:
            if not asteroid.is_targeted:
                distance = self._get_distance_to_asteroid(asteroid)
                if distance < min_distance:
                    min_distance = distance
                    closest_asteroid = asteroid
        if closest_asteroid:
            closest_asteroid.is_targeted = True
        return closest_asteroid

    # Chase the target asteroid.
    def _chase_target(self):
        # Adjust the logic to stop at a distance before the asteroid
        target_x_position = self.target_asteroid.rect.centerx
        target_y_position = self.target_asteroid.rect.centery - self.spacing  # Stop above the asteroid

        # Horizontal movement towards the target
        if self.rect.centerx < target_x_position:
            self.rect.x += min(self.speed, target_x_position - self.rect.centerx)
        elif self.rect.centerx > target_x_position:
            self.rect.x -= min(self.speed, self.rect.centerx - target_x_position)

        # Vertical movement towards the target (stopping at a distance before the asteroid)
        if self.rect.centery < target_y_position:
            self.rect.y += min(self.speed, target_y_position - self.rect.centery)

    # Check if the helper ship is in shooting range of the target.
    def _is_in_shooting_range(self, target):
        # Define what it means to be in shooting range
        # For example, within a certain distance horizontally and slightly above the asteroid
        horizontal_distance = abs(self.rect.centerx - target.rect.centerx)
        vertical_distance = target.rect.centery - self.rect.centery
        return horizontal_distance < HELPER_SHOOTING_RANGE and vertical_distance > 0

    # Get the distance to an asteroid.
    def _get_distance_to_asteroid(self, asteroid):
        # Simple Pythagorean distance calculation
        dx = self.rect.centerx - asteroid.rect.centerx
        dy = self.rect.centery - asteroid.rect.centery
        return (dx ** 2 + dy ** 2) ** 0.5
    
    # Shoot a bullet towards the target.
    def _shoot(self):
        # Shoot a bullet towards the target
        current_time = time.time()
        if current_time - self.last_shot_time >= self.shooting_cooldown:
            self.last_shot_time = current_time
            # Adjust bullet's speed and direction if necessary
            bullet_speed_x = 0  # No horizontal movement
            bullet_speed_y = -self.bullet_speed  # Negative because it moves up
            bullet = Bullet(self.rect.centerx, self.rect.centery, bullet_speed_x, bullet_speed_y)
            self.bullets.add(bullet)
            
    # Check for collisions between the helper ship's bullets and asteroids.
    def _check_collision(self, asteroids):
        # Check for collisions between the helper ship's bullets and asteroids
        for bullet in self.bullets:
            # Check if a bullet hits any asteroid
            hit_asteroids = pygame.sprite.spritecollide(bullet, asteroids, True)
            for asteroid in hit_asteroids:
                # Handle the bullet-asteroid collision
                bullet.kill()
                # Increment the score when an asteroid is hit
                self.score += 1
                asteroid.is_targeted = False 
                # Create a particle effect when an asteroid is hit
                particle_effect = ParticleEffect(asteroid.rect.center)
                particle_effect.start()

    # Enforce the screen boundaries for the helper ship.
    def _enforce_screen_boundaries(self):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.screen_height:
            self.rect.bottom = self.screen_height

    # Check if the helper ship is off the screen.
    def _check_off_screen(self):
        if self.rect.y > self.screen_height + 20:
            self.kill()
    
    # Reduce the health of the helper ship by a certain amount.
    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self._die()

    # Kill the helper ship.
    def _die(self):
        self.kill()

    # Draw the helper ship and its bullets on the screen.
    def draw(self, screen):
        self.bullets.draw(screen)
        screen.blit(self.image, self.rect)
