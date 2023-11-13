import pygame

class Button:
    def __init__(self, screen, pos, text, color='black', font_size=32, bg_color=None):
        self.screen = screen
        self.pos = pos
        self.text = text
        self.color = color
        self.bg_color = bg_color
        self.font = pygame.font.Font(None, font_size)
        self.render_text = self.font.render(text, True, pygame.Color(color))
        self.rect = pygame.Rect(pos[0], pos[1], self.render_text.get_width() + 20, self.render_text.get_height() + 10)

    def draw(self):
        if self.bg_color:
            pygame.draw.rect(self.screen, pygame.Color(self.bg_color), self.rect, border_radius=10)  # Draw the button background with rounded corners
        self.screen.blit(self.render_text, (self.rect.x + 10, self.rect.y + 5))  # Draw the text

    def check_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            return True
        return False
