class TestWord():
    """
    A class that gets all words from the dictionary(20k.txt),
    and checks if given word is one of them
    """

    def __init__(self) -> None:
        self.dictionary = []

        # Read the dictionary
        with open("20k.txt", "r") as f:
            self.dictionary = f.readlines()

    def check(self, word: str) -> bool:
        return word + "\n" in self.dictionary
