# managers/input_manager.py
import pygame

class InputManager:
    def __init__(self):
        self.key_action_map = {
            pygame.K_LEFT: 'move_left',
            pygame.K_RIGHT: 'move_right',
            pygame.K_UP: 'move_up',
            pygame.K_DOWN: 'move_down',
            pygame.K_SPACE: 'special attack',
            pygame.K_p: 'pause',
        }

    def process(self, game_manager):
        pressed_keys = pygame.key.get_pressed()
        for key, action in self.key_action_map.items():
            if pressed_keys[key]:
                getattr(game_manager.player, action)()
