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

        # Get rid of spaces before adding to the matrix
        line = list(input(f"Line {line_count}: ").replace(" ", ""))

        # If it is the first input, set the line_length
        if (line_count == 1):
            matrix.append(line)

            line_length = len(line)
            line_count += 1

        # If it is not the first input, check if it meets previous line length
        elif line_length == len(line):
            matrix.append(line)

            line_count += 1

        # Exit case
        elif not line:
            break

        else:
            print("Invalid input, try again.")
            continue

    return matrix
