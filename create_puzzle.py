def create_puzzle() -> list:
    """
        A function that creates a puzzle matrix.
    User inputs the puzzle line by line.
    Function controls if length of the lines are equal.
    Returns the final matrix.
    eg. [['h', 'e', 'y'], ['h', 'i'], ...]
    """

    matrix = []
    line_count = 1
    line_length = 0

    print("Press enter to exit...")
    while True:
        line = list(input(f"Line {line_count}: ").replace(" ", ""))

        if (line_count == 1):
            matrix.append(line)

            line_length = len(line)
            line_count += 1

        elif line_length == len(line):
            matrix.append(line)

            line_count += 1

        elif not line:
            break

        else:
            print("Invalid input, try again.")
            continue

    return matrix
