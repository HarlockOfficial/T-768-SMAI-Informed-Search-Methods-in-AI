from Computer import BFSComputer


class BFSComputerMaxDepth(BFSComputer):
    def __init__(self, structure, max_depth):
        super().__init__(structure)
        self.__max_depth = max_depth
        self.__solution_found = False

    def compute(self, start, end):
        if self._computed:
            self._path = []
            self.__solution_found = False
            self._computed = False
        start_node = self._structure.get_node(start)
        end_node = self._structure.get_node(end)
        if start_node is None or end_node is None:
            raise ValueError("Start or end node not found")
        self._setup_structure()
        start_node.add_attribute("distance", 0)
        start_node.add_attribute("parent", None)
        start_node.add_attribute("visited", True)
        assert start_node == self._structure.get_node(start)
        queue = [start_node]
        while len(queue) > 0:
            current = queue.pop(0)
            if current == end_node:
                break
            if current.get_attribute("distance") >= self.__max_depth:
                continue
            for child in self._structure.get_all_children(current):
                if (not child.get_attribute("visited") or
                        child.get_attribute("distance") > current.get_attribute("distance") + 1):
                    child.add_attribute("visited", True)
                    child.add_attribute("distance", current.get_attribute("distance") + 1)
                    child.add_attribute("parent", current)
                    queue.append(child)
        if end_node.get_attribute("distance") is not None and end_node.get_attribute("distance") <= self.__max_depth:
            self.__solution_found = True
        self._max_depth_save_path(start_node, end_node)
        self._computed = True

    def is_solution_found(self):
        if not self._computed:
            raise ValueError("Path not computed")
        return self.__solution_found

    def _max_depth_save_path(self, start, end):
        if not self.__solution_found:
            return
        self._save_path(start, end)
