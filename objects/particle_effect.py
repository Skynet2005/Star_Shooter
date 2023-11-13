import pygame
import random

class Particle:
    def __init__(self, position, direction, speed, radius, color, lifespan):
        self.position = list(position)
        self.direction = direction
        self.speed = speed
        self.radius = radius
        self.color = color
        self.lifespan = lifespan
        self.alive = True

    def update(self):
        # Move the particle
        self.position[0] += self.direction[0] * self.speed
        self.position[1] += self.direction[1] * self.speed
        # Reduce the lifespan
        self.lifespan -= 1
        if self.lifespan <= 0:
            self.alive = False

    def draw(self, screen):
        # Draw the particle as a circle
        pygame.draw.circle(screen, self.color, self.position, self.radius)

class ParticleEffect:
    def __init__(self, position):
        self.particles = []
        self.position = position

    def start(self):
        # Create several particles with random directions and speeds
        for _ in range(20):  # Number of particles
            direction = [random.uniform(-1, 1), random.uniform(-1, 1)]
            speed = random.uniform(1, 3)
            radius = random.uniform(1, 3)
            color = (255, 255, 255)  # White color
            lifespan = random.randint(20, 50)  # Frames until the particle dies
            self.particles.append(Particle(self.position, direction, speed, radius, color, lifespan))

    def update(self):
        # Update all particles
        for particle in self.particles[:]:
            particle.update()
            if not particle.alive:
                self.particles.remove(particle)

    def draw(self, screen):
        # Draw all particles
        for particle in self.particles:
            particle.draw(screen)

    def is_finished(self):
        # Check if there are no more alive particles
        return len(self.particles) == 0
