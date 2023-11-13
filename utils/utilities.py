# utils/utilities.py
import pygame

def load_image(file_name, max_width=None):
    image = pygame.image.load(file_name)
    if max_width and image.get_width() > max_width:
        ratio = max_width / float(image.get_width())
        return pygame.transform.scale(image, (int(image.get_width() * ratio), int(image.get_height() * ratio)))
    return image
