class WordInfo():
    """
        A class that provides more information about the word.
    Including position, and direction.
    """

    def __init__(self, name: str, posX: int, posY: int, direction: str):
        self.name = name
        self.posX = posX
        self.posY = posY
        self.direction = direction

    def __str__(self):
        return f"Word {self.name} at starting position ({self.posX}, {self.posY}), {self.direction}"
