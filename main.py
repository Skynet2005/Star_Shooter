# main.py

import pygame
from managers.screen_manager import ScreenManager
from managers.input_manager import InputManager
from managers.sound_manager import SoundManager
from managers.game_manager import GameManager
from managers.leaderboard_manager import LeaderboardManager
from ui.button import Button
from ui.textinput import TextInput 
from utils.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Space Shooter")
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.Font(None, 32)
        
        # Initialize managers
        self.screen_manager = ScreenManager(self.screen, self.font)
        self.sound_manager = SoundManager()
        self.game_manager = GameManager(self.screen, self.font, self.sound_manager)
        self.input_manager = InputManager()
        self.leaderboard_manager = LeaderboardManager('leaderboard.json')
        
        # Initialize buttons
        self.mute_button = Button(self.screen, (10, SCREEN_HEIGHT - 42), 'Mute')
        self.menu_button = Button(self.screen, (SCREEN_WIDTH - 110, SCREEN_HEIGHT - 42), 'Menu')
        self.restart_button = Button(self.screen, (100, SCREEN_HEIGHT // 2 - 100), 'Restart')
        self.settings_button = Button(self.screen, (100, SCREEN_HEIGHT // 2 - 50), 'Settings')
        self.leaderboard_button = Button(self.screen, (100, SCREEN_HEIGHT // 2), 'Leaderboard')
        self.quit_button = Button(self.screen, (100, SCREEN_HEIGHT // 2 + 50), 'Quit')

        # Initialize game state variables
        self.game_over = False
        self.paused = False
        self.text_input = TextInput(100, SCREEN_HEIGHT // 2, 200, 50, self.font, max_length=20)

    def run(self):
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

                if not self.game_over and not self.paused:
                    # Check for button clicks
                    if self.mute_button.check_click(event):
                        self.sound_manager.toggle_sound()
                    if self.menu_button.check_click(event):
                        self.paused = True

            if not self.game_over and not self.paused:
                # Process user input and update game state
                self.input_manager.process(self.game_manager)
                self.game_manager.run(events)
                
                # Draw game elements on the screen
                self.screen_manager.draw(self.game_manager)
                self.game_manager.draw(self.screen)
                
                # Draw buttons
                self.mute_button.draw()
                self.menu_button.draw()
            elif self.paused:
                # Display pause menu
                self.screen.fill((255, 255, 255))  # Menu background
                self.restart_button.draw()
                self.settings_button.draw()
                self.leaderboard_button.draw()
                self.quit_button.draw()
                for event in events:
                    # Check for button clicks in the pause menu
                    if self.restart_button.check_click(event):
                        self.restart_game()
                    elif self.settings_button.check_click(event):
                        self.show_settings()
                    elif self.leaderboard_button.check_click(event):
                        self.show_leaderboard()
                    elif self.quit_button.check_click(event):
                        self.running = False
            elif self.game_over:
                for event in events:
                    # Handle text input for leaderboard entry
                    name_input = self.text_input.handle_event(event)
                    if name_input is not None:  # The user has entered their name
                        self.leaderboard_manager.update_leaderboard(name_input, self.game_manager.player.score)
                        self.leaderboard_manager.save_leaderboard()
                        self.running = False  # Transition to a different state if desired
                        break  # Exit the event loop since we're done here
                self.text_input.draw(self.screen)
                game_over_text = self.font.render("Game Over! Enter your name:", True, pygame.Color('white'))
                self.screen.blit(game_over_text, (100, SCREEN_HEIGHT // 2 - 50))

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()

    def restart_game(self):
        # Reset game state to start over
        self.game_manager = GameManager(self.screen, self.font, self.sound_manager)
        self.paused = False
        self.game_over = False

    def show_settings(self):
        # Placeholder for settings functionality
        print("Show settings")

    def show_leaderboard(self):
        # Placeholder for leaderboard display functionality
        print("Show leaderboard")

if __name__ == '__main__':
    game = Game()
    game.run()
