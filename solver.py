from words import words


class Solver:
    GRAY = '0'
    YELLOW = '1'
    GREEN = '2'

    def __init__(self):
        pass

    def solve(self, answers):
        yellows = {}
        greens = {}
        grays = {}

        for word, colors in answers.items():
            for index, letter in enumerate(word):
                color = colors[index]
                if color == Solver.GRAY:
                    grays = self.setColor(grays, letter, index)
                elif color == Solver.YELLOW:
                    yellows = self.setColor(yellows, letter, index)
                elif color == Solver.GREEN:
                    greens = self.setColor(greens, letter, index)

        for word in words:
            if self.has_yellow(yellows, word):
                continue

            if self.has_gray(grays, word):
                continue

            if self.has_all_greens(greens, word):
                print(word)

    def setColor(self, color, letter, index):
        if letter in color:
            old = color[letter]
            old.append(index)
            color[letter] = old
        else:
            color[letter] = [index]

        return color

    def has_yellow(self, yellows, word):
        num_yellows = 0
        for letter, positions in yellows.items():
            if letter in word:
                num_yellows += 1
                for position in positions:
                    if word[position] == letter:
                        return True
        if num_yellows == len(yellows):
            return False
        else:
            return True

    def has_gray(self, grays, word):
        for letter, indices in grays.items():
            for index in indices:
                if word[index] == letter:
                    return True
        return False

    def has_all_greens(self, greens, word):
        for letter, indices in greens.items():
            for index in indices:
                if word[index] != letter:
                    return False
        return True
