import abc


class Structure(object, metaclass=abc.ABCMeta):
    class Node(object):
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return str(self.value)

        def __eq__(self, other):
            return self.value == other.value and type(self) == type(other) and type(self.value) == type(other.value)

        def __hash__(self):
            return hash(self.value)

        def __repr__(self):
            return repr(self.value)

        def add_attribute(self, name, value):
            setattr(self, name, value)

        def get_attribute(self, name):
            return getattr(self, name)
    @abc.abstractmethod
    def get_root(self) -> 'Structure.Node':
        """ Return the root of the structure """
        raise NotImplementedError("Structure is an abstract class")

    @abc.abstractmethod
    def get_next_child(self, node):
        """ Return the next child of the node or None if there are no more children """
        raise NotImplementedError("Structure is an abstract class")

    @abc.abstractmethod
    def get_all_children(self, node):
        """ Return all the children of the node """
        raise NotImplementedError("Structure is an abstract class")

    @abc.abstractmethod
    def get_parent(self, node):
        """ Return the parent of the node """
        raise NotImplementedError("Structure is an abstract class")

    @abc.abstractmethod
    def get_height(self, node):
        """ Return the height of the node """
        raise NotImplementedError("Structure is an abstract class")

    @abc.abstractmethod
    def get_number_of_children(self, node):
        """ Return the number of children of the node """
        raise NotImplementedError("Structure is an abstract class")

    @abc.abstractmethod
    def get_node(self, node):
        """ Return the node """
        raise NotImplementedError("Structure is an abstract class")
