import unittest

from Computer import DFSComputer
from Model import BinaryTree


class TestDFSComputer(unittest.TestCase):
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
        self.computer = DFSComputer(self.structure)
    
    def test_is_computed(self):
        """
        Test the is_computed method
        """
        self.assertFalse(self.computer.is_computed())
        self.computer.compute_approach_1_stack(1, 7)
        self.assertTrue(self.computer.is_computed())
    
    def test_compute_approach_1_stack(self):
        """
        Test the compute method (approach 1)
        """
        self.computer.compute_approach_1_stack(1, 7)
        self.assertEqual(self.computer.get_path(), [1, 3, 7])
        self.computer.compute_approach_1_stack(1, 4)
        self.assertEqual(self.computer.get_path(), [1, 2, 4])
        self.computer.compute_approach_1_stack(1, 5)
        self.assertEqual(self.computer.get_path(), [1, 2, 5])
        self.computer.compute_approach_1_stack(1, 6)
        self.assertEqual(self.computer.get_path(), [1, 3, 6])
        self.computer.compute_approach_1_stack(1, 2)
        self.assertEqual(self.computer.get_path(), [1, 2])
        self.computer.compute_approach_1_stack(1, 3)
        self.assertEqual(self.computer.get_path(), [1, 3])
        self.computer.compute_approach_1_stack(1, 1)
        self.assertEqual(self.computer.get_path(), [1])
        with self.assertRaises(ValueError):
            self.computer.compute_approach_1_stack(1, 8)
        with self.assertRaises(ValueError):
            self.computer.compute_approach_1_stack(8, 1)
        with self.assertRaises(ValueError):
            self.computer.compute_approach_1_stack(8, 8)
        with self.assertRaises(ValueError):
            self.computer.compute_approach_1_stack(0, 1)
        with self.assertRaises(ValueError):
            self.computer.compute_approach_1_stack(1, 0)
        with self.assertRaises(ValueError):
            self.computer.compute_approach_1_stack(1, -1)
        with self.assertRaises(ValueError):
            self.computer.compute_approach_1_stack(-1, 1)
        with self.assertRaises(ValueError):
            self.computer.compute_approach_1_stack(-1, -1)
        with self.assertRaises(ValueError):
            self.computer.compute_approach_1_stack(1, 1.5)
        with self.assertRaises(ValueError):
            self.computer.compute_approach_1_stack(1.5, 1)
        with self.assertRaises(ValueError):
            self.computer.compute_approach_1_stack(1.5, 1.5)
        with self.assertRaises(ValueError):
            self.computer.compute_approach_1_stack(1, "1")
        with self.assertRaises(ValueError):
            self.computer.compute_approach_1_stack("1", 1)
        with self.assertRaises(ValueError):
            self.computer.compute_approach_1_stack("1", "1")
        with self.assertRaises(ValueError):
            self.computer.compute_approach_1_stack(1, None)
        with self.assertRaises(ValueError):
            self.computer.compute_approach_1_stack(None, 1)
        with self.assertRaises(ValueError):
            self.computer.compute_approach_1_stack(None, None)
        with self.assertRaises(ValueError):
            self.computer.compute_approach_1_stack(1, [1])
        with self.assertRaises(ValueError):
            self.computer.compute_approach_1_stack([1], 1)
        with self.assertRaises(ValueError):
            self.computer.compute_approach_1_stack([1], [1])
        with self.assertRaises(ValueError):
            self.computer.compute_approach_1_stack(1, (1,))
        with self.assertRaises(ValueError):
            self.computer.compute_approach_1_stack((1,), 1)
        with self.assertRaises(ValueError):
            self.computer.compute_approach_1_stack((1,), (1,))
        with self.assertRaises(ValueError):
            self.computer.compute_approach_1_stack(1, {1})
        with self.assertRaises(ValueError):
            self.computer.compute_approach_1_stack({1}, 1)
        with self.assertRaises(ValueError):
            self.computer.compute_approach_1_stack({1}, {1})
        with self.assertRaises(ValueError):
            self.computer.compute_approach_1_stack(1, True)
        with self.assertRaises(ValueError):
            self.computer.compute_approach_1_stack(True, 1)
        with self.assertRaises(ValueError):
            self.computer.compute_approach_1_stack(True, True)

    def test_compute_approach_2_recursive(self):
        """
            Test the compute method (approach 2)
        """
        self.computer.compute_approach_2_recursive(1, 7)
        self.assertEqual(self.computer.get_path(), [1, 3, 7])
        self.computer.compute_approach_2_recursive(1, 4)
        self.assertEqual(self.computer.get_path(), [1, 2, 4])
        self.computer.compute_approach_2_recursive(1, 5)
        self.assertEqual(self.computer.get_path(), [1, 2, 5])
        self.computer.compute_approach_2_recursive(1, 6)
        self.assertEqual(self.computer.get_path(), [1, 3, 6])
        self.computer.compute_approach_2_recursive(1, 2)
        self.assertEqual(self.computer.get_path(), [1, 2])
        self.computer.compute_approach_2_recursive(1, 3)
        self.assertEqual(self.computer.get_path(), [1, 3])
        self.computer.compute_approach_2_recursive(1, 1)
        self.assertEqual(self.computer.get_path(), [1])
        with self.assertRaises(ValueError):
            self.computer.compute_approach_2_recursive(1, 8)
        with self.assertRaises(ValueError):
            self.computer.compute_approach_2_recursive(8, 1)
        with self.assertRaises(ValueError):
            self.computer.compute_approach_2_recursive(8, 8)
        with self.assertRaises(ValueError):
            self.computer.compute_approach_2_recursive(0, 1)
        with self.assertRaises(ValueError):
            self.computer.compute_approach_2_recursive(1, 0)
        with self.assertRaises(ValueError):
            self.computer.compute_approach_2_recursive(1, -1)
        with self.assertRaises(ValueError):
            self.computer.compute_approach_2_recursive(-1, 1)
        with self.assertRaises(ValueError):
            self.computer.compute_approach_2_recursive(-1, -1)
        with self.assertRaises(ValueError):
            self.computer.compute_approach_2_recursive(1, 1.5)
        with self.assertRaises(ValueError):
            self.computer.compute_approach_2_recursive(1.5, 1)
        with self.assertRaises(ValueError):
            self.computer.compute_approach_2_recursive(1.5, 1.5)
        with self.assertRaises(ValueError):
            self.computer.compute_approach_2_recursive(1, "1")
        with self.assertRaises(ValueError):
            self.computer.compute_approach_2_recursive("1", 1)
        with self.assertRaises(ValueError):
            self.computer.compute_approach_2_recursive("1", "1")
        with self.assertRaises(ValueError):
            self.computer.compute_approach_2_recursive(1, None)
        with self.assertRaises(ValueError):
            self.computer.compute_approach_2_recursive(None, 1)
        with self.assertRaises(ValueError):
            self.computer.compute_approach_2_recursive(None, None)
        with self.assertRaises(ValueError):
            self.computer.compute_approach_2_recursive(1, [1])
        with self.assertRaises(ValueError):
            self.computer.compute_approach_2_recursive([1], 1)
        with self.assertRaises(ValueError):
            self.computer.compute_approach_2_recursive([1], [1])
        with self.assertRaises(ValueError):
            self.computer.compute_approach_2_recursive(1, (1,))
        with self.assertRaises(ValueError):
            self.computer.compute_approach_2_recursive((1,), 1)
        with self.assertRaises(ValueError):
            self.computer.compute_approach_2_recursive((1,), (1,))
        with self.assertRaises(ValueError):
            self.computer.compute_approach_2_recursive(1, {1})
        with self.assertRaises(ValueError):
            self.computer.compute_approach_2_recursive({1}, 1)
        with self.assertRaises(ValueError):
            self.computer.compute_approach_2_recursive({1}, {1})
        with self.assertRaises(ValueError):
            self.computer.compute_approach_2_recursive(1, True)
        with self.assertRaises(ValueError):
            self.computer.compute_approach_2_recursive(True, 1)
        with self.assertRaises(ValueError):
            self.computer.compute_approach_2_recursive(True, True)

    def test_get_path(self):
        self.assertRaises(ValueError, self.computer.get_path)
        self.computer.compute_approach_1_stack(1, 7)
        stack_path = self.computer.get_path()
        self.computer.compute_approach_2_recursive(1, 7)
        recursive_path = self.computer.get_path()
        self.assertEqual(stack_path, recursive_path)
        self.assertEqual(stack_path, [1, 3, 7])
        self.computer.compute_approach_1_stack(1, 4)
        stack_path = self.computer.get_path()
        self.computer.compute_approach_2_recursive(1, 4)
        recursive_path = self.computer.get_path()
        self.assertEqual(stack_path, recursive_path)
        self.assertEqual(stack_path, [1, 2, 4])
        self.computer.compute_approach_1_stack(1, 5)
        stack_path = self.computer.get_path()
        self.computer.compute_approach_2_recursive(1, 5)
        recursive_path = self.computer.get_path()
        self.assertEqual(stack_path, recursive_path)
        self.assertEqual(stack_path, [1, 2, 5])
        self.computer.compute_approach_1_stack(1, 6)
        stack_path = self.computer.get_path()
        self.computer.compute_approach_2_recursive(1, 6)
        recursive_path = self.computer.get_path()
        self.assertEqual(stack_path, recursive_path)
        self.assertEqual(stack_path, [1, 3, 6])
        self.computer.compute_approach_1_stack(1, 2)
        stack_path = self.computer.get_path()
        self.computer.compute_approach_2_recursive(1, 2)
        recursive_path = self.computer.get_path()
        self.assertEqual(stack_path, recursive_path)
        self.assertEqual(stack_path, [1, 2])
        self.computer.compute_approach_1_stack(1, 3)
        stack_path = self.computer.get_path()
        self.computer.compute_approach_2_recursive(1, 3)
        recursive_path = self.computer.get_path()
        self.assertEqual(stack_path, recursive_path)
        self.assertEqual(stack_path, [1, 3])
        self.computer.compute_approach_1_stack(1, 1)
        stack_path = self.computer.get_path()
        self.computer.compute_approach_2_recursive(1, 1)
        recursive_path = self.computer.get_path()
        self.assertEqual(stack_path, recursive_path)
        self.assertEqual(stack_path, [1])


if __name__ == '__main__':
    unittest.main()
