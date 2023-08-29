from Model import GenericDataStructure


class DFSComputer(object):
    def __init__(self, structure: GenericDataStructure):
        self._structure = structure
        self._computed = False
        self._path = []

    def is_computed(self):
        return self._computed

    def compute_approach_1_stack(self, start, end):
        if self._computed:
            self._path = []
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
        stack = [start_node]
        while len(stack) > 0:
            current = stack.pop()
            if current == end_node:
                break
            for child in self._structure.get_all_children(current):
                if (not child.get_attribute("visited") or
                        child.get_attribute("distance") > current.get_attribute("distance") + 1):
                    child.add_attribute("visited", True)
                    child.add_attribute("distance", current.get_attribute("distance") + 1)
                    child.add_attribute("parent", current)
                    stack.insert(0, child)
        self._save_path(start_node, end_node)
        self._computed = True

    def compute_approach_2_recursive(self, start, end, current=None):
        if self._computed:
            self._path = []
            self._computed = False
        if current is None:
            current = self._structure.get_node(start)
            self._setup_structure()
            current.add_attribute("distance", 0)
            current.add_attribute("parent", None)
            current.add_attribute("visited", True)
            assert current == self._structure.get_node(start)
        if current == self._structure.get_node(end):
            self._save_path(self._structure.get_node(start), self._structure.get_node(end))
            self._computed = True
            return True
        for child in self._structure.get_all_children(current):
            if (not child.get_attribute("visited") or
                    child.get_attribute("distance") > current.get_attribute("distance") + 1):
                child.add_attribute("visited", True)
                child.add_attribute("distance", current.get_attribute("distance") + 1)
                child.add_attribute("parent", current)
                if self.compute_approach_2_recursive(start, end, child):
                    return True

    def _setup_structure(self, node=None):
        if node is None:
            node = self._structure.get_root()
        node.add_attribute("visited", False)
        node.add_attribute("parent", None)
        node.add_attribute("distance", None)
        for child in self._structure.get_all_children(node):
            self._setup_structure(child)

    def _save_path(self, start_node, end_node):
        current = end_node
        while current is not None:
            self._path.insert(0, current)
            current = current.get_attribute("parent")
        assert self._path[0] == start_node
        assert self._path[-1] == end_node
        assert (self._path[-1].get_attribute("distance") is not None and
                self._path[-1].get_attribute("distance") == len(self._path) - 1)

    def get_path(self):
        if not self._computed:
            raise ValueError("Path not computed")
        return [x.value for x in self._path]

    def get_total_distance(self):
        if not self._computed:
            raise ValueError("Path not computed")
        return len(self._path) - 1
