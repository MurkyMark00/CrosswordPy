from test_word import TestWord
from create_puzzle import create_puzzle
from word import WordInfo


# 3 nested for loops dont look like the cleanest solution to check every possible combination of letters, but I couldn't write a better algorithm
def horizontal_check(test: TestWord, matrix: list) -> list:
    correct_words = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            temp_word = ""
            for k in range(j, len(matrix[i])):
                temp_word += matrix[i][k]

            if test.check(temp_word) == True:
                temp_word_info = WordInfo(
                    name=temp_word, posY=i, posX=k, direction="horizontally")

                correct_words.append(temp_word_info)

    return correct_words


# I really cannot explain how this works, I don't even know how I thought of this
def vertical_check(test: TestWord, matrix: list) -> list:
    correct_words = []
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            temp_word = ""
            for k in range(j, len(matrix[i])):
                temp_word += matrix[k][i]

            if test.check(temp_word) == True:
                temp_word_info = WordInfo(
                    name=temp_word, posY=k, posX=i, direction="vertically"
                )

                correct_words.append(temp_word_info)

    return correct_words


def main():
    matrix = create_puzzle()
    test = TestWord()
    correct_words = horizontal_check(
        test, matrix) + vertical_check(test, matrix)

    for word in correct_words:
        print(str(word))


if __name__ == "__main__":
    main()
