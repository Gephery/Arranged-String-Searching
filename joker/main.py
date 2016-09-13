from joker.jokerCommandNode import sortable_score, JokerCommandNode
from joker.jokerCommandTree import JokerCommandTree
from joker.jokerUtil import filter_and_pick_joker, word_dic_net, filter_and_pick_joker_str
from sys import setrecursionlimit
from time import time

welcome_cmd_s = "welcome"
exit_cmd_s = "leave"


def get_joker_cmds():
    return {"print name": print_name, welcome_cmd_s: welcome, exit_cmd_s:leave}


def word_list():
    return open("words.txt").read().split("\n")


def print_name():
    name = input("What is your name? ")
    print("Hello " + name + "!")


def welcome():
    print("Welcome!")


def leave():
    print("Bye!")


def main():
    cmd_tree = JokerCommandTree()
    cmd_reference = get_joker_cmds()
    for cmd in cmd_reference.keys():
        if cmd is not None:
            cmd_tree.add(cmd)

    in_cmd = welcome_cmd_s

    while in_cmd is not exit_cmd_s:
        s_cmd = input("Welcome! Please enter a command, peasant. ")
        net = cmd_tree.find_similar_net(s_cmd, 20.0, -1)
        in_cmd = filter_and_pick_joker(s_cmd, net)
        cmd_reference[in_cmd]()


def diction():
    setrecursionlimit(150000)
    word_tree = JokerCommandTree()
    start_time = time() * 1000
    word_reference = word_list()
    length = len(word_reference)
    count = 0
    for word in word_reference:
        temp_time = time() * 1000
        if word is not None:
            word_tree.add(word.lower())
        count += 1
        if (temp_time - start_time) >= 1000:
            start_time = time() * 1000
            print("Indexed " + str(count))
            count = 0

    print("Words loaded.\n")
    end_time = time() * 1000
    print("It took: " + str(end_time - start_time))

    in_word = "none"

    while in_word is not "leave":
        s_cmd = input("Try and spell a word, and I will guess what it is. ")
        net = word_tree.find_similar_net(s_cmd, 0, 2)
        in_word = filter_and_pick_joker(s_cmd, net)
        print("Are you trying to spell " + in_word + "?")


def diction_with_dic():
    word_dic = {}
    start_time = time() * 1000
    word_reference = word_list()
    count = 0
    for word in word_reference:
        temp_time = time() * 1000
        if word is not None:
            temp_score = sortable_score(word.lower())
            if word_dic.get(temp_score) is None:
                word_dic[temp_score] = [word.lower()]
            else:
                word_dic[temp_score].append(word.lower())
        count += 1
        if (temp_time - start_time) >= 2000:
            start_time = time() * 1000
            print("Indexed " + str(count))
            count = 0

    print("Words loaded.\n")
    end_time = time() * 1000
    print("It took: " + str(end_time - start_time))
    print("The algorithm lost " + str(len(word_reference) - len(word_dic)) + " words")

    in_word = "none"

    while in_word is not "leave":
        s_cmd = input("Try and spell a word, and I will guess what it is. ")
        net = word_dic_net(s_cmd, word_dic, 10.0, 100000)
        in_word = filter_and_pick_joker_str(s_cmd, net)
        print("Are you trying to spell " + in_word + "?")
diction_with_dic()
