from joker.jokerCommandNode import JokerCommandNode
from joker.jokerCommandNode import sortable_score


class JokerCommandTree:
    def __init__(self):
        self.root = None

    def print_preorder(self, print_func=print):
        JokerCommandTree._print_preorder(self.root, print_func)

    def add(self, cmd):
        joker_cmd = JokerCommandNode(cmd)
        self.root = JokerCommandTree._add(self.root, joker_cmd)

    def find_similar_net(self, inputted_cmd, percent_range=10.0, look_range=10):
        input_sort_value = sortable_score(inputted_cmd)
        return JokerCommandTree._find_similar_net(input_sort_value, self.root,
                                                  percent_range, look_range)

    @staticmethod
    def _print_preorder(node, print_func, space=""):
        if node is None:
            return
        print(space + str(node.cmd) + ":" + str(node.value) + "\n")
        space += "  "
        if node.right is not None:
            JokerCommandTree._print_preorder(node.right, print_func, space)
        if node.left is not None:
            JokerCommandTree._print_preorder(node.left, print_func, space)

    @staticmethod
    def _add(root, joker_cmd):
        if root is None:
            return joker_cmd
        elif root.right is not None:
            if root.value < joker_cmd.value:
                if root.right.right is None:
                    temp = root.right
                    root.right = JokerCommandNode("", (temp.value+joker_cmd.value) / 2)
                    if root.right.value > joker_cmd.value:
                        root.right.right = temp
                        root.right.left = joker_cmd
                    else:
                        root.right.right = joker_cmd
                        root.right.left = temp
                    return root
            else:
                if root.left.left is None:
                    temp = root.left
                    root.left = JokerCommandNode("", (temp.value+joker_cmd.value) / 2)
                    if root.left.value <= joker_cmd.value:
                        root.left.left = temp
                        root.left.right = joker_cmd
                    else:
                        root.left.left = joker_cmd
                        root.left.right = temp
                    return root

        else:
            temp = root
            root = JokerCommandNode("", (temp.value+joker_cmd.value) / 2)
            if root.value > joker_cmd.value:
                root.right = temp
                root.left = joker_cmd
            else:
                root.right = joker_cmd
                root.left = temp
            return root
        if joker_cmd.value >= root.value:
            root.right = JokerCommandTree._add(root.right, joker_cmd)
        else:
            root.left = JokerCommandTree._add(root.left, joker_cmd)
        return root

    @staticmethod
    def _find_similar_net(input_sort_value, node, percent_range, look_range,
                          adding=False, net=[]):
        if node is None or look_range is 0:
            return net
        right = node.right
        left = node.left
        if not adding:
            same_val = input_sort_value is node.value
            right_spot = False
            if right is not None:
                right_spot = find_percent_dif(right.value, input_sort_value) <= percent_range or \
                             find_percent_dif(input_sort_value, left.value) <= percent_range
            if same_val or right_spot:
                JokerCommandTree._find_similar_net(input_sort_value,
                                                   node, percent_range,
                                                   look_range,
                                                   True, net)
            else:
                if input_sort_value >= node.value:
                    JokerCommandTree._find_similar_net(input_sort_value,
                                                       right, percent_range,
                                                       look_range,
                                                       False, net)
                if input_sort_value <= node.value:
                    JokerCommandTree._find_similar_net(input_sort_value,
                                                       left, percent_range,
                                                       look_range,
                                                       False, net)
        else:
            if node.right is None and find_percent_dif(node.value, input_sort_value) <= percent_range:
                net.append(node)
            else:
                JokerCommandTree._find_similar_net(input_sort_value,
                                                   right, percent_range,
                                                   look_range-1,
                                                   True, net)
                JokerCommandTree._find_similar_net(input_sort_value,
                                                   left, percent_range,
                                                   look_range-1,
                                                   True, net)
        return net


def find_percent_dif(num1, num2):
    return abs((num1 - num2) / num1 * 100)
