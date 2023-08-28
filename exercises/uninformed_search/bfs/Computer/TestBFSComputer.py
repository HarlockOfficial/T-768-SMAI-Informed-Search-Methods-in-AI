
import unittest
from Computer import BFSComputer
from Model import BinaryTree


class TestBFSComputer(unittest.TestCase):
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
        self.computer = BFSComputer(self.structure)

    def test_is_computed(self):
        """
        Test the is_computed method
        """
        self.assertFalse(self.computer.is_computed())
        self.computer.compute(1, 7)
        self.assertTrue(self.computer.is_computed())

    def test_compute(self):
        """
        Test the compute method
        """
        self.computer.compute(1, 7)
        self.assertEqual(self.computer.get_path(), [1, 3, 7])
        self.computer.compute(1, 4)
        self.assertEqual(self.computer.get_path(), [1, 2, 4])
        self.computer.compute(1, 5)
        self.assertEqual(self.computer.get_path(), [1, 2, 5])
        self.computer.compute(1, 6)
        self.assertEqual(self.computer.get_path(), [1, 3, 6])
        self.computer.compute(1, 2)
        self.assertEqual(self.computer.get_path(), [1, 2])
        self.computer.compute(1, 3)
        self.assertEqual(self.computer.get_path(), [1, 3])
        self.computer.compute(1, 1)
        self.assertEqual(self.computer.get_path(), [1])
        with self.assertRaises(ValueError):
            self.computer.compute(1, 8)
        with self.assertRaises(ValueError):
            self.computer.compute(8, 1)
        with self.assertRaises(ValueError):
            self.computer.compute(8, 8)
        with self.assertRaises(ValueError):
            self.computer.compute(0, 1)
        with self.assertRaises(ValueError):
            self.computer.compute(1, 0)
        with self.assertRaises(ValueError):
            self.computer.compute(0, 0)
        with self.assertRaises(ValueError):
            self.computer.compute(1, -1)
        with self.assertRaises(ValueError):
            self.computer.compute(-1, 1)
        with self.assertRaises(ValueError):
            self.computer.compute(-1, -1)
        with self.assertRaises(ValueError):
            self.computer.compute(1, 1.5)
        with self.assertRaises(ValueError):
            self.computer.compute(1.5, 1)
        with self.assertRaises(ValueError):
            self.computer.compute(1.5, 1.5)
        with self.assertRaises(ValueError):
            self.computer.compute(1, "1")
        with self.assertRaises(ValueError):
            self.computer.compute("1", 1)
        with self.assertRaises(ValueError):
            self.computer.compute("1", "1")
        with self.assertRaises(ValueError):
            self.computer.compute(1, None)
        with self.assertRaises(ValueError):
            self.computer.compute(None, 1)
        with self.assertRaises(ValueError):
            self.computer.compute(None, None)
        with self.assertRaises(ValueError):
            self.computer.compute(1, [1])
        with self.assertRaises(ValueError):
            self.computer.compute([1], 1)
        with self.assertRaises(ValueError):
            self.computer.compute([1], [1])
        with self.assertRaises(ValueError):
            self.computer.compute(1, (1,))
        with self.assertRaises(ValueError):
            self.computer.compute((1,), 1)
        with self.assertRaises(ValueError):
            self.computer.compute((1,), (1,))
        with self.assertRaises(ValueError):
            self.computer.compute(1, {1})
        with self.assertRaises(ValueError):
            self.computer.compute({1}, 1)
        with self.assertRaises(ValueError):
            self.computer.compute({1}, {1})
        with self.assertRaises(ValueError):
            self.computer.compute(1, True)
        with self.assertRaises(ValueError):
            self.computer.compute(True, 1)
        with self.assertRaises(ValueError):
            self.computer.compute(True, True)

    def test_get_path(self):
        """
        Test the get_path method
        """
        self.assertRaises(ValueError, self.computer.get_path)
        self.computer.compute(1, 7)
        self.assertEqual(self.computer.get_path(), [1, 3, 7])
        self.computer.compute(1, 4)
        self.assertEqual(self.computer.get_path(), [1, 2, 4])
        self.computer.compute(1, 5)
        self.assertEqual(self.computer.get_path(), [1, 2, 5])
        self.computer.compute(1, 6)
        self.assertEqual(self.computer.get_path(), [1, 3, 6])
        self.computer.compute(1, 2)
        self.assertEqual(self.computer.get_path(), [1, 2])
        self.computer.compute(1, 3)
        self.assertEqual(self.computer.get_path(), [1, 3])
        self.computer.compute(1, 1)
        self.assertEqual(self.computer.get_path(), [1])

    def test_get_total_distance(self):
        """
        Test the get_total_distance method
        """
        self.assertRaises(ValueError, self.computer.get_total_distance)
        self.computer.compute(1, 7)
        self.assertEqual(self.computer.get_total_distance(), 2)
        self.computer.compute(1, 4)
        self.assertEqual(self.computer.get_total_distance(), 2)
        self.computer.compute(1, 5)
        self.assertEqual(self.computer.get_total_distance(), 2)
        self.computer.compute(1, 6)
        self.assertEqual(self.computer.get_total_distance(), 2)
        self.computer.compute(1, 2)
        self.assertEqual(self.computer.get_total_distance(), 1)
        self.computer.compute(1, 3)
        self.assertEqual(self.computer.get_total_distance(), 1)
        self.computer.compute(1, 1)
        self.assertEqual(self.computer.get_total_distance(), 0)


if __name__ == "__main__":
    unittest.main()
