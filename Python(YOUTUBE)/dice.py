import random
import time

dice_faces = {
    1: ("┌─────┐",
        "│     │",
        "│  ●  │",
        "│     │",
        "└─────┘"),
    2: ("┌─────┐",
        "│ ●   │",
        "│     │",
        "│   ● │",
        "└─────┘"),
    3: ("┌─────┐",
        "│ ●   │",
        "│  ●  │",
        "│   ● │",
        "└─────┘"),
    4: ("┌─────┐",
        "│ ● ● │",
        "│     │",
        "│ ● ● │",
        "└─────┘"),
    5: ("┌─────┐",
        "│ ● ● │",
        "│  ●  │",
        "│ ● ● │",
        "└─────┘"),
    6: ("┌─────┐",
        "│ ● ● │",
        "│ ● ● │",
        "│ ● ● │",
        "└─────┘"),
}

def roll_dice():
    print("Rolling the dice...")
    time.sleep(1)
    result = random.randint(1, 6)
    print(f"You rolled a {result}!\n")
    for line in dice_faces[result]:
        print(line)

while True:
    input("\nPress Enter to roll the dice (or Ctrl+C to quit)...")
    roll_dice()
