# Snake Game

This is a simple implementation of the classic Snake game. The game can be played in both a GUI and CLI interface.

## Features

- **Classic Snake Gameplay:** Navigate the snake to eat fruit and grow longer, but avoid colliding with the walls or yourself.
- **Multiple Interfaces:** Play the game either through a graphical user interface (GUI) using Pygame or through a command-line interface (CLI) using Curses.
- **Customizable Settings:** Adjust the width, height, and speed of the snake in the game.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/RhamzThev/Snake.git
    cd Snake
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
   
   > Note: Make sure you have Python and Pip installed.

## Usage

You can run the game by executing the `main.py` file. 

### GUI Version

```bash
python main.py
```

### CLI Version

To play the game in the command line, modify the `main.py` to use `CLI` instead of `GUI`.

## How to Play

- **Arrow Keys**: Control the direction of the snake (Up, Down, Left, Right).
- **Objective**: Eat the fruit to increase your score and grow the snake. Avoid running into walls or the snake's own body.

## Project Structure

- **main.py**: Entry point for the game.
- **controller/**: Contains the logic for controlling the snake's movements and interactions.
- **model/**: Manages the game's data such as the snake's position, score, and fruit locations.
- **view/**: Provides the user interface for the game, available in both GUI and CLI formats.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to fork the repository and submit pull requests. Any improvements or bug fixes are welcome!
