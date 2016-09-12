from joker.jokerCommandNode import JokerCommandNode
from joker.jokerCommandTree import JokerCommandTree
from joker.jokerUtil import filter_and_pick_joker
import enchant

welcome_cmd_s = "welcome"
exit_cmd_s = "leave"


def get_joker_cmds():
    return {"print name": print_name, welcome_cmd_s: welcome, exit_cmd_s:leave}


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
        net = cmd_tree.find_similar_net(s_cmd, 30.0, 10)
        in_cmd = filter_and_pick_joker(s_cmd, net)
        cmd_reference[in_cmd]()


def diction():
    cmd_tree = JokerCommandTree()
    cmd_reference = get_joker_cmds()
    for cmd in cmd_reference.keys():
        if cmd is not None:
            cmd_tree.add(cmd)

    in_cmd = welcome_cmd_s

    while in_cmd is not exit_cmd_s:
        s_cmd = input("Try and spell a word, and I will guess what it is. ")
        net = cmd_tree.find_similar_net(s_cmd, 30.0, 10)
        in_cmd = filter_and_pick_joker(s_cmd, net)
        print("Are you trying to spell " + in_cmd + "?")
main()
