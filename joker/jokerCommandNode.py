

class JokerCommandNode:
    def __init__(self, cmd="", value=None, right=None, left=None):
        self.cmd = cmd
        if value is None:
            self.value = sortable_score(cmd)
        else:
            self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return self.cmd + ":" + str(self.value)


def sortable_score(string):
    score = 0.0
    for letter in string:
        score += letter_common_score(letter)
    return score + len(string)


def letter_common_score(letter):
    return {'a': 24, 'b': 7, 'c': 15, 'd': 17, 'e': 26, 'f': 11,
            'g': 10, 'h': 19, 'i': 22, 'j': 4, 'k': 5, 'l': 16, 'm': 13,
            'n': 21, 'o': 23, 'p': 8, 'q': 2, 'r': 18, 's': 20, 't': 25,
            'u': 14, 'v': 6, 'w': 12, 'x': 3, 'y': 9, 'z': 1, ' ': 0}.get(letter)
