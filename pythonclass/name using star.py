height = 6

for row in range(height):
    # --- Letter P ---
    for col in range(5):
        if (
            row == 0 or row == 2 or
            col == 0 or
            (row == 1 and col == 4)
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("  ", end="")

    # --- Letter R ---
    for col in range(5):
        if (
            row == 0 or row == 2 or
            col == 0 or
            (row == 1 and col == 4) or
            (row == 3 and col == 2) or
            (row == 4 and col == 3) or
            (row == 5 and col == 4)
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("  ", end="")

    # --- Letter A ---
    for col in range(5):
        if (
            (row == 0 and 1 <= col <= 3) or
            (row == 3) or
            (col == 0 and row != 0) or
            (col == 4 and row != 0)
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("  ", end="")

    # --- Letter T ---
    for col in range(5):
        if (
            row == 0 or
            col == 2
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("  ", end="")

    # --- Letter Y ---
    for col in range(5):
        if (
            (row <= 2 and (col == row or col == 4 - row)) or
            (row >= 3 and col == 2)
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("  ", end="")

    # --- Letter U ---
    for col in range(5):
        if (
            (col == 0 and row != 5) or
            (col == 4 and row != 5) or
            (row == 5 and 1 <= col <= 3)
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("  ", end="")

    # --- Letter S ---
    for col in range(5):
        if (
            row == 0 or row == 2 or row == 5 or
            (row == 1 and col == 0) or
            (row == 3 and col == 4) or
            (row == 4 and col == 0)
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("  ", end="")

    # --- Letter H ---
    for col in range(5):
        if (
            col == 0 or col == 4 or
            row == 2
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()  # Move to next line after all letters
