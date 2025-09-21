# Platformer

A simple 2D platformer game built with Pygame.

## Features

*   Player movement (left, right, jump)
*   Score tracking for unique platforms landed on
*   Randomly generated platforms (static and moving)
*   Camera following the player
*   Basic anti-cheat LOL

## Prerequisites

Before you begin, ensure you have met the following requirements:

*   Python 2.x installed on your system.
*   `pip` (Python package installer) is up to date.

## How to Run Locally

Follow these steps to get the game running on your local machine:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/mintykiera/simple-platformer.git
    cd simple-platformer
    ```
    
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the game:**
    ```bash
    python main.py
    ```

## Game Controls

*   **`A` or `Left Arrow`**: Move Left
*   **`D` or `Right Arrow`**: Move Right
*   **`Spacebar`**: Jump (and to Start Game)

### Getting Started in Game

When the game starts, you'll see a message "Press SPACE to start jumping!". Once you press space, the game session begins, and your score will start tracking.

## Project Structure

*   `config.py`: Game constants and configurations.
*   `main.py`: The entry point for running the game.
*   `entities/`: Contains definitions for game objects like `Player`, `Platform`, `MovingPlatform`.
*   `managers/`: Handles generation and management of game entities, e.g., `PlatformManager`.
*   `scenes/`: Defines different game states, currently `GameScene`.
*   `systems/`: Helper modules for specific functionalities, e.g., `collision.py`.

## License

This project is open-source.
