# objects/textinput.py
import pygame

class TextInput:
    def __init__(self, x, y, width, height, font, max_length=10):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = pygame.Color('dodgerblue2')
        self.text = ""
        self.font = font
        self.max_length = max_length
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = pygame.Color('lightskyblue3') if self.active else pygame.Color('dodgerblue2')
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                self.active = False
                return self.text
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                if len(self.text) < self.max_length:
                    self.text += event.unicode

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 2)
        text_surface = self.font.render(self.text, True, pygame.Color('white'))
        screen.blit(text_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)

    def get_text(self):
        return self.text
