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
