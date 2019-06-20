class TestWord():
    """
    A class that gets all words from the dictionary(words.txt),
    and checks if given word is one of them
    """

    def __init__(self) -> None:
        self.dictionary = []

        # Read the dictionary
        with open("words.txt", "r") as f:
            self.dictionary = f.readlines()

    def check(self, word: str) -> bool:
        # All words in the dictionary have newlines after them.
        return word + "\n" in self.dictionary
