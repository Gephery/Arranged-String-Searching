from string import ascii_lowercase


def score_by_functions(original_cmd, input_cmd, scoring_functions):
    """Scores a string by the inputted functions.

    :param original_cmd: The idea string.
    :param input_cmd: The string being compared.
    :param scoring_functions: Functions that each return 0.0 to 1.0 scores.
    :return: 0.0 to 100.0, representing the score.
    """
    score = 0.0
    for func in scoring_functions:
        score += func(original_cmd, input_cmd)
    return score / len(scoring_functions) * 100.0


def uniform_letter_score(original_cmd, input_cmd):
    inorder_score = 0.0
    for i in range(min(len(original_cmd), len(input_cmd))):
        if original_cmd[i] is input_cmd[i]:
            inorder_score += 1.0
    inorder_score /= len(original_cmd)
    return inorder_score


def count_letter_score(original_cmd, input_cmd):
    letter_count_score = 0.0
    for letter in ascii_lowercase:
        count_original = original_cmd.count(letter)
        count_input = input_cmd.count(letter)
        if count_original != 0 and count_input != 0 and \
                count_original is count_input:
            letter_count_score += count_original
    letter_count_score /= len(original_cmd)
    return letter_count_score


def length_score(original_cmd, input_cmd):
    length_o = len(original_cmd)
    length_i = len(input_cmd)
    max_num = max(length_o, length_i)
    min_num = min(length_o, length_i)
    return min_num / max_num


def joker_score(original_cmd, input_cmd):
    return score_by_functions(original_cmd, input_cmd,
                              (length_score, uniform_letter_score,
                               count_letter_score))


def filter_by_function(input_cmd, list_cmds, func=joker_score):
    dic_of_scoring = {}
    for cmd in list_cmds:
        dic_of_scoring[cmd] = joker_score(cmd.cmd, input_cmd)
    return dic_of_scoring


def filter_and_pick_joker(input_cmd, list_cmd, filter=filter_by_function):
    dic_of_scoring = filter(input_cmd, list_cmd)
    best_cmd = None
    best_score = 0.0
    for cmd in dic_of_scoring.keys():
        if dic_of_scoring[cmd] > best_score:
            best_cmd = cmd
            best_score = dic_of_scoring[cmd]
    return filter_to_function(best_cmd.cmd)


def filter_to_function(str_cmd):
    return str_cmd
