import unittest

from Computer import BFSComputerMaxDepth
from Model import BinaryTree


class TestBFSComputerMaxDepth(unittest.TestCase):
    def setUp(self) -> None:
        """
        Init the structure
        Init the computer
        """
        tree_list = [1, 2, 3, 4, 5, 6, 7]
        """
        Note, this creates a tree like this:
            1
           / \
          2   3
         / \ / \
        4  5 6  7
        """
        self.structure = BinaryTree(tree_list)

    def test_compute_max_depth(self):
        """
        Test the max depth of the tree
        """
        computer = BFSComputerMaxDepth(self.structure, 1)
        computer.compute(1, 1)
        self.assertEqual(computer.get_path(), [1])
        computer.compute(1, 3)
        self.assertEqual(computer.get_path(), [1, 3])
        computer.compute(1, 2)
        self.assertEqual(computer.get_path(), [1, 2])
        computer.compute(1, 4)
        self.assertEqual(computer.get_path(), [])
        computer = BFSComputerMaxDepth(self.structure, 2)
        computer.compute(2, 1)
        self.assertEqual(computer.get_path(), [])

    def test_is_solution_found(self):
        """
        Test the is_solution_found method
        """
        computer = BFSComputerMaxDepth(self.structure, 1)
        computer.compute(1, 1)
        self.assertTrue(computer.is_solution_found())
        computer.compute(1, 3)
        self.assertTrue(computer.is_solution_found())
        computer.compute(1, 2)
        self.assertTrue(computer.is_solution_found())
        computer.compute(1, 4)
        self.assertFalse(computer.is_solution_found())
        computer = BFSComputerMaxDepth(self.structure, 2)
        computer.compute(2, 1)
        self.assertFalse(computer.is_solution_found())


if __name__ == '__main__':
    unittest.main()
