from stringSearching.arrangedStringNode import ArrangedStringNode
from stringSearching.arrangedStringNode import sortable_score_basic


class ArrangedStringTree:
    def __init__(self):
        self.root = None

    def print_preorder(self, print_func=print):
        ArrangedStringTree._print_preorder(self.root, print_func)

    def add(self, string):
        node = ArrangedStringNode(string)
        self.root = ArrangedStringTree._add(self.root, node)

    def cast_net(self, inputted_str, percent_range=10.0, look_range=10,
                 sorting_score=sortable_score_basic):
        """Used to search the tree for similar strings.

        :param inputted_str: The string that is being looked for.
        :param percent_range: The percentage of difference the strings being
            looked at can differ from the inputted_str.
        :param look_range: An int that is how many levels of the tree it goes down
            after it finds its first similar string.
        :param sorting_score: The score that the tree is sorted with.
        :return: An list of strings similar to the one inputted.
        """
        input_sort_value = sorting_score(inputted_str)
        return ArrangedStringTree._find_similar_net(input_sort_value, self.root,
                                                    percent_range, look_range)

    @staticmethod
    def _print_preorder(node, print_func, space=""):
        if node is None:
            return
        print(space + str(node.cmd) + ":" + str(node.value) + "\n")
        space += "  "
        if node.right is not None:
            ArrangedStringTree._print_preorder(node.right, print_func, space)
        if node.left is not None:
            ArrangedStringTree._print_preorder(node.left, print_func, space)

    @staticmethod
    def _add(root, joker_cmd):
        if root is None:
            return joker_cmd
        elif root.right is not None:
            if root.value < joker_cmd.value:
                if root.right.right is None:
                    temp = root.right
                    root.right = ArrangedStringNode("", (temp.value + joker_cmd.value) / 2)
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
                    root.left = ArrangedStringNode("", (temp.value + joker_cmd.value) / 2)
                    if root.left.value <= joker_cmd.value:
                        root.left.left = temp
                        root.left.right = joker_cmd
                    else:
                        root.left.left = joker_cmd
                        root.left.right = temp
                    return root

        else:
            temp = root
            root = ArrangedStringNode("", (temp.value + joker_cmd.value) / 2)
            if root.value > joker_cmd.value:
                root.right = temp
                root.left = joker_cmd
            else:
                root.right = joker_cmd
                root.left = temp
            return root
        if joker_cmd.value >= root.value:
            root.right = ArrangedStringTree._add(root.right, joker_cmd)
        else:
            root.left = ArrangedStringTree._add(root.left, joker_cmd)
        return root

    @staticmethod
    def _find_similar_net(input_sort_value, node, percent_range, look_range,
                          adding=False, net=[]):
        if node is None or look_range is 0:
            return net
        right = node.right
        left = node.left
        if not adding:
            similar_val = find_percent_dif(node.value, input_sort_value) <= percent_range
            if similar_val:
                ArrangedStringTree._find_similar_net(input_sort_value,
                                                     node, percent_range,
                                                     look_range,
                                                     True, net)
            else:
                if input_sort_value >= node.value:
                    ArrangedStringTree._find_similar_net(input_sort_value,
                                                         right, percent_range,
                                                         look_range,
                                                         False, net)
                if input_sort_value <= node.value:
                    ArrangedStringTree._find_similar_net(input_sort_value,
                                                         left, percent_range,
                                                         look_range,
                                                         False, net)
        else:
            if node.right is None and find_percent_dif(node.value, input_sort_value) <= percent_range:
                net.append(node)
            else:
                ArrangedStringTree._find_similar_net(input_sort_value,
                                                     right, percent_range,
                                                     look_range - 1,
                                                     True, net)
                ArrangedStringTree._find_similar_net(input_sort_value,
                                                     left, percent_range,
                                                     look_range - 1,
                                                     True, net)
        return net


def find_percent_dif(num1, num2):
    return abs((num1 - num2) / num1 * 100.0)
