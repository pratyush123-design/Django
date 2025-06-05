import time
import os

# Choose your snake character!
snake_char = "🐍"

# Terminal width (adjust if needed)
width = 50

def clear():
    # Clear terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

def snake_animation():
    try:
        while True:
            for i in range(width):
                clear()
                print(" " * i + snake_char)
                time.sleep(0.05)
    except OSError:
        print("\nSnake says goodbye! 🐍👋")

if __name__ == "__main__":
    snake_animation()
