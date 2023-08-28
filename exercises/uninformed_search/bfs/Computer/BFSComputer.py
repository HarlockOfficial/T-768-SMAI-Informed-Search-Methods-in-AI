from Model import GenericDataStructure


class BFSComputer(object):
    def __init__(self, structure: GenericDataStructure):
        self.__structure = structure
        self.__computed = False
        self.__path = []

    def is_computed(self):
        return self.__computed

    def compute(self, start, end):
        if self.__computed:
            self.__path = []
            self.__computed = False
        start_node = self.__structure.get_node(start)
        end_node = self.__structure.get_node(end)
        if start_node is None or end_node is None:
            raise ValueError("Start or end node not found")
        self.__setup_structure()
        start_node.add_attribute("distance", 0)
        start_node.add_attribute("parent", None)
        start_node.add_attribute("visited", True)
        assert start_node == self.__structure.get_node(start)
        queue = [start_node]
        while len(queue) > 0:
            current = queue.pop(0)
            if current == end_node:
                break
            for child in self.__structure.get_all_children(current):
                if (not child.get_attribute("visited") or
                        child.get_attribute("distance") > current.get_attribute("distance") + 1):
                    child.add_attribute("visited", True)
                    child.add_attribute("distance", current.get_attribute("distance") + 1)
                    child.add_attribute("parent", current)
                    queue.append(child)
        self.__save_path(start_node, end_node)

        self.__computed = True

    def __setup_structure(self, node=None):
        if node is None:
            node = self.__structure.get_root()
        node.add_attribute("visited", False)
        node.add_attribute("parent", None)
        node.add_attribute("distance", None)
        for child in self.__structure.get_all_children(node):
            self.__setup_structure(child)

    def __save_path(self, start_node, end_node):
        current = end_node
        while current is not None:
            self.__path.insert(0, current)
            current = current.get_attribute("parent")
        assert self.__path[0] == start_node
        assert self.__path[-1] == end_node
        assert (self.__path[-1].get_attribute("distance") is not None and
                self.__path[-1].get_attribute("distance") == len(self.__path) - 1)

    def get_path(self):
        if not self.__computed:
            raise ValueError("Path not computed")
        return [x.value for x in self.__path]

    def get_total_distance(self):
        if not self.__computed:
            raise ValueError("Path not computed")
        return len(self.__path) - 1
