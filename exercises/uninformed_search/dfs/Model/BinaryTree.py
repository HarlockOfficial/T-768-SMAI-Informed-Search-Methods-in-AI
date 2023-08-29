import math

from Model import GenericDataStructure


class BinaryTree(GenericDataStructure):
    """
        Defines a binary tree as a list
        NOTE: there is no ordering in the tree
    """
    def __init__(self, ordered_nodes: list[object]):
        if not BinaryTree.__no_duplicates(ordered_nodes):
            raise Exception("The list of nodes contains duplicates")

        if len(ordered_nodes) == 0:
            self.__tree = []
        else:
            self.__tree = [BinaryTree.Node(x) for x in ordered_nodes]

    def add_child(self, node):
        if type(node) is not BinaryTree.Node:
            node = BinaryTree.Node(node)
        self.__tree.append(node)

    def get_root(self) -> GenericDataStructure.Node:
        return self.__tree[0]

    def get_next_child(self, node, last_child=None):
        if type(node) is not BinaryTree.Node:
            node = BinaryTree.Node(node)
        index = self.__tree.index(node)
        if index == len(self.__tree) - 1:
            return None
        if last_child is None:
            return self.__tree[2 * index + 1] if 2 * index + 1 < len(self.__tree) else None
        else:
            return self.__tree[2 * index + 2] if 2 * index + 2 < len(self.__tree) else None

    def get_all_children(self, node):
        if type(node) is not BinaryTree.Node:
            node = BinaryTree.Node(node)
        index = self.__tree.index(node)
        if 2 * index + 1 >= len(self.__tree):
            return []
        if 2 * index + 2 >= len(self.__tree):
            return [self.__tree[2 * index + 1]]
        return [self.__tree[2 * index + 1], self.__tree[2 * index + 2]]

    def get_parent(self, node):
        if type(node) is not BinaryTree.Node:
            node = BinaryTree.Node(node)
        index = self.__tree.index(node)
        if index == 0:
            return None
        return self.__tree[(index - 1) // 2]

    def get_height(self, node):
        if type(node) is not BinaryTree.Node:
            node = BinaryTree.Node(node)
        index = self.__tree.index(node)
        return math.floor(math.log2(index + 1))

    def get_number_of_children(self, node):
        if type(node) is not BinaryTree.Node:
            node = BinaryTree.Node(node)
        return len(self.get_all_children(node))

    def set_value(self, node, value_name, value):
        if type(node) is not BinaryTree.Node:
            node = BinaryTree.Node(node)
        index = self.__tree.index(node)
        self.__tree[index].add_attribute(value_name, value)

    def get_value(self, node, value_name):
        if type(node) is not BinaryTree.Node:
            node = BinaryTree.Node(node)
        index = self.__tree.index(node)
        return self.__tree[index].get_attribute(value_name)

    def get_node(self, node):
        if type(node) is not BinaryTree.Node:
            node = BinaryTree.Node(node)
        index = self.__tree.index(node)
        return self.__tree[index]

    @staticmethod
    def __no_duplicates(nodes_list: list[object]):
        """
            Checks if the list of nodes contains duplicates
        """
        return len(nodes_list) == len(set(nodes_list))
