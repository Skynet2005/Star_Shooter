import pygame
from utils.settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Menu:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.menu_items = ['Restart', 'Settings', 'Leaderboard', 'Quit']
        self.active_index = 0  # The index of the currently selected menu item

    def draw(self):
        for index, item in enumerate(self.menu_items):
            if index == self.active_index:
                color = pygame.Color('dodgerblue2')  # Highlight the selected item
            else:
                color = pygame.Color('white')
            menu_text = self.font.render(item, True, color)
            x = SCREEN_WIDTH // 2 - menu_text.get_width() // 2
            y = SCREEN_HEIGHT // 2 - menu_text.get_height() // 2 + index * 50
            self.screen.blit(menu_text, (x, y))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.active_index = (self.active_index - 1) % len(self.menu_items)
            elif event.key == pygame.K_DOWN:
                self.active_index = (self.active_index + 1) % len(self.menu_items)
            elif event.key == pygame.K_RETURN:
                return self.menu_items[self.active_index]
        return None
