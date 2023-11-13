# managers/sound_manager.py
import pygame

class SoundManager:
    def __init__(self):
        self.sounds = {}
        self.music = {}

    def load_sound(self, sound_name):
        # Load a sound effect and store it in the dictionary
        self.sounds[sound_name] = pygame.mixer.Sound(sound_name)

    def play_sound(self, sound_name):
        # Play a sound effect
        if sound_name in self.sounds:
            self.sounds[sound_name].play()
        else:
            raise ValueError(f"Sound {sound_name} not loaded.")

    def load_music(self, music_name):
        # Load a music track and store it in the dictionary
        self.music[music_name] = pygame.mixer.music.load(music_name)

    def play_music(self, music_name):
        # Play background music
        if music_name in self.music:
            pygame.mixer.music.play(-1)  # The -1 means loop indefinitely
        else:
            raise ValueError(f"Music {music_name} not loaded.")

    def stop_music(self):
        # Stop the currently playing music
        pygame.mixer.music.stop()

    def pause_music(self):
        # Pause the currently playing music
        pygame.mixer.music.pause()

    def resume_music(self):
        # Resume the paused music
        pygame.mixer.music.unpause()

    def load_shooting_sound(self, sound_name):
        # Load a shooting sound effect and store it in the dictionary
        self.sounds[sound_name] = pygame.mixer.Sound(sound_name)

    def load_explosion_sound(self, sound_name):
        # Load an explosion sound effect and store it in the dictionary
        self.sounds[sound_name] = pygame.mixer.Sound(sound_name)

    def play_shooting_sound(self, sound_name):
        # Play a shooting sound effect
        if pygame.mixer.get_init() and sound_name in self.sounds:
            self.sounds[sound_name].play()
        elif not pygame.mixer.get_init():
            print(f"{sound_name}, is Muted.")
        else:
            raise ValueError(f"Shooting sound {sound_name} not loaded.")

    def play_explosion_sound(self, sound_name):
        # Play an explosion sound effect only if the mixer is initialized
        if pygame.mixer.get_init() and sound_name in self.sounds:
            self.sounds[sound_name].play()
        elif not pygame.mixer.get_init():
            print(f"{sound_name}, is Muted.")
        else:
            raise ValueError(f"Explosion sound {sound_name} not loaded.")
    
    def toggle_sound(self):
        if pygame.mixer.get_init() is not None:
            pygame.mixer.quit()
        else:
            pygame.mixer.init()
