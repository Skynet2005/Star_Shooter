# How to Download, Install, and Play the Game

[Download and Install](#download-and-install) | [Game Structure](#game-structure) | [Building the Game](#building-the-game) | [Credits](#credits)

## Download and Install

Follow these steps to download, install, and play the game:

1. Clone the game repository from GitHub. Open your terminal and run the following command:

   ```Bash
   git clone https://github.com/skynet2005/space_shooter.git
   ```

2. Change your current directory to the cloned repository. In your terminal, run:

   ```Bash
   cd space_shooter
   ```

3. Install the necessary dependencies for the game. In your terminal, run:

   ```Bash
   pip install -r requirements.txt
   ```

4. Now, you're ready to play the game! Start the game by running the following command in your terminal:

  ```Bash
  python main.py
  ```

Enjoy the game!

## Game Structure

`STRUCTURE:`

```Bash
space_shooter/
│
├── main.py
├── leaderboard.json
├── README.md
├── requirements.txt
│
├── ui
│   ├── __pycache__
│   ├── button.py
│   ├── menu.py
│   └── textinput.py
|
├── utils
│   ├── __pycache__
│   ├── settings.py
│   └── utilities.py
│
├── managers/
│   ├── __pycache__
│   ├── input_manager.py
│   ├── leaderboard_manager.py
│   ├── screen_manager.py
│   └── sound_manager.py
│
├── objects/
│   ├── __pycache__
│   ├── asteroid.py
│   ├── bullet.py
│   ├── health_pack.py
│   ├── helper_item.py
│   ├── helper_ship.py
│   ├── particle_effect.py
│   └── player.py
│
├── assets/
│   ├── images/
│   │    ├── asteroid.png
│   │    ├── background.png
│   │    ├── bullet.png
│   │    ├── health_pack.png
│   │    ├── helper_item.png
│   │    ├── helper_ship.png
│   │    └── player_ship.png
│   ├── sounds/
│   │    ├── bullet.wav
│   │    ├── collide.wav
│   │    ├── music1.mp3
│   │    └── music2.mp3
```

## Building the Game

Follow these steps to build the game:

1. Create a new repository on GitHub and clone it to your local machine.
2. Set up a new virtual environment for the project.
3. Create a `requirements.txt` file and add the necessary dependencies. The dependencies for this game are:
   - pygame==2.0.1
   - random==1.0.1
4. Create a `main.py` file and import the necessary modules.
5. Create a `settings.py` file and add the necessary constants. Refer to `utils/settings.py` for an example.
6. Create a `utilities.py` file and add the necessary utility functions.
7. Create an `input_manager.py` file and add the InputManager class.
8. Create a `screen_manager.py` file and add the ScreenManager class.
9. Create a `sound_manager.py` file and add the SoundManager class.
10. Create a `leaderboard_manager.py` file and add the LeaderboardManager class.
11. Create a `player.py` file and add the Player class.

## Testing and Debugging

Once you have built the game, it's time to test and debug:

1. Playtest your game extensively. Look for bugs and assess the overall game balance and fun factor.

## Documentation and Readme

As you build and test the game, remember to:

1. Document your code. This will help others understand your code and make it easier for you to make changes in the future.
2. Update the README.md with instructions on how to play the game, how to install requirements from `requirements.txt`, and any other relevant information.

## Sound Implementation

To enhance the gaming experience, add in sound effects and music when you are ready. The game currently supports the following sound files:
      - bullet.wav
      - collide.wav
      - music1.mp3
      - music2.mp3

## Credits

[Sound Effects](https://mixkit.co/free-sound-effects/space-shooter/)
[Images](https://openai.com) - Dalle-3
