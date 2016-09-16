

class JokerCommandNode:
    """Joker nodes are the

    """
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


def _sortable_score(string):
    score = 0.0
    for letter in "etao":
        score += string.count(letter) * letter_common_score(letter)
    return score + len(string)


def sortable_score(string):
    score = 0.0
    length = len(string)
    for letter in string:
        temp_letter_score = letter_common_score(letter)
        score += prime_eq(temp_letter_score)
    return score + length


def __sortable_score(string):
    score = 0.0
    length = len(string)
    for letter in string:
        temp_letter_score = letter_common_score(letter)
        score += temp_letter_score
    return score + length


def letter_common_score(letter):
    return {'a': 24, 'b': 7, 'c': 15, 'd': 17, 'e': 26, 'f': 11,
            'g': 10, 'h': 19, 'i': 22, 'j': 4, 'k': 5, 'l': 16, 'm': 13,
            'n': 21, 'o': 23, 'p': 8, 'q': 2, 'r': 18, 's': 20, 't': 25,
            'u': 14, 'v': 6, 'w': 12, 'x': 3, 'y': 9, 'z': 1, ' ': 0,
            '1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1,
            '8': 1, '9': 1, '0': 1, '-': 1, '.': 1, ',': 1, '\'': 1,
            '/': 1, '&': 1, '!': 1}.get(letter)


def prime_eq(num):
    return {1: 2, 2: 3, 3: 5, 4: 7, 5: 11, 6: 13, 7: 17, 8: 19, 9: 23, 10: 29,
            11: 31, 12: 37, 13: 41, 14: 43, 15: 47, 16: 53, 17: 59, 18: 61,
            19: 67, 20: 71, 21: 73, 22: 79, 23: 83, 24: 89, 25: 97, 26: 101,
            27: 103, 28: 107, 29: 109, 30: 113, 31: 127, 32: 131, 33: 137, 34: 139,
            35: 149, 36: 151, 37: 157, 38: 163, 39: 167, 40: 173, 41: 179, 42: 181,
            43: 191, 0: 193}.get(num)


def prime_eq_two(num):
    return {1: 197, 2: 199, 3: 211, 4: 223, 5: 227, 6: 229, 7: 233, 8: 239, 9: 241,
            10: 251, 11: 257, 12: 263, 13: 269, 14: 271, 15: 277, 16: 281, 17: 283,
            18: 293, 19: 307, 20: 311, 21: 313, 22: 317, 23: 331, 24: 337, 25: 347,
            26: 349, 27: 353, 28: 359, 29: 367, 30: 373, 31: 379, 32: 383, 33: 389,
            34: 397, 35: 401, 36: 409, 37: 419, 38: 421, 39: 431, 40: 433, 41: 439,
            42: 443, 43: 449, 0: 457}.get(num)
